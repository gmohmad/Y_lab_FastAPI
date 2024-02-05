from fastapi.routing import APIRoute

from src.main import app


def reverse(route_name: str, **path_params: str) -> str:
    """Возвращает url по имени и аргументам эндпойнта"""
    for route in app.routes:
        if isinstance(route, APIRoute) and route.name == route_name:
            path = route.path
            return path.format(**path_params)
