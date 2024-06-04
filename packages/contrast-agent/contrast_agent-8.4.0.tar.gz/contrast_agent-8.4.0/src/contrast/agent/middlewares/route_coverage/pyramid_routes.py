# Copyright © 2024 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from contrast.api import Route
from contrast.utils.decorators import fail_quietly
from contrast.agent.middlewares.route_coverage.common import (
    DEFAULT_ROUTE_METHODS,
    build_args_from_function,
    build_key,
    get_normalized_uri,
)
from pyramid.interfaces import IView, IViewClassifier, IRouteRequest, IRoutesMapper
from zope.interface import Interface

from contrast_vendor import structlog as logging

logger = logging.getLogger("contrast")


def get_iface_for_route(registry, pyramid_route):
    return registry.queryUtility(IRouteRequest, name=pyramid_route.name)


def _get_view_func(registry, pyramid_route):
    request_iface = get_iface_for_route(registry, pyramid_route)

    if request_iface is None:
        view_func = None
    else:
        view_func = registry.adapters.lookup(
            (IViewClassifier, request_iface, Interface), IView, name="", default=None
        )
    return view_func


def create_pyramid_routes(registry):
    """
    Returns all the routes registered to an app as a dict

    The Pyramid Request object holds a reference to the url route registry

    :param registry: Pyramid Registry
    :return: Returns a dict of key = id, value = api.Route.
    """
    routes = {}
    mapper = registry.queryUtility(IRoutesMapper)

    if mapper is None:
        return routes

    for pyramid_route in mapper.get_routes():
        view_func = _get_view_func(registry, pyramid_route)

        if view_func is not None:
            route = build_pyramid_route(pyramid_route.name, view_func)
            route_id = str(id(view_func))

            methods = pyramid_route.predicates or DEFAULT_ROUTE_METHODS

            for method_type in methods:
                key = build_key(route_id, method_type)

                url = get_normalized_uri(pyramid_route.path)
                routes[key] = Route(
                    verb=method_type, url=url, route=route, framework="Pyramid"
                )
        else:
            logger.debug("Unable to add %s to route coverage.", pyramid_route.path)

    return routes


def build_pyramid_route(pyramid_route_name, view_func):
    method_arg_names = build_args_from_function(view_func)

    return pyramid_route_name + method_arg_names


@fail_quietly("Unable to find new routes")
def get_view_func(request_path, routes_list, registry):
    if not request_path:
        logger.debug("No path info for pyramid request")
        return None

    # Ideally we would like to call get_route but
    # there is no direct relationship between the wsgi
    # request path and the name of the route so we must
    # iterate over all the routes to find it by the path
    # pyramid_route = mapper.get_route(name)

    matching_routes = [x for x in routes_list if x.path == request_path]
    if not matching_routes:
        return None

    return _get_view_func(registry, matching_routes[0])


@fail_quietly("Unable to build route", return_value="")
def build_route(view_func, url):
    route_name = url.replace("/", "")
    return build_pyramid_route(route_name, view_func)
