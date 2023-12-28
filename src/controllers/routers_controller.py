"""Routers controller module."""

import dash

from src.controllers.servers_controller import server
from src.utils import global_variables
from src.utils.tools import Server
from src.views.error_view import error_view


def set_server(
    server_name: str,
) -> tuple[dash.html.Div, dict[str, str], dict[str, str]]:
    """
    Set the current server name

    Args:
        server_name (str): the server name
    """
    global_variables.current_server_name = server_name
    return server(server_name), {"display": "none"}, {"display": "none"}


# pylint: disable=too-many-return-statements
@dash.callback(
    [
        dash.Output("main-content", "children"),
        dash.Output("top-menu-retro", "style", allow_duplicate=True),
        dash.Output("top-menu-classic", "style", allow_duplicate=True),
    ],
    [dash.Input("url", "pathname")],
    prevent_initial_call=True,
)
def routers(pathname: str) -> dash.html.Div:
    """
    Route the url to the correct server

    Args:
        pathname (str): the url pathname

    Returns:
        dash.html.Div: the html.Div for the correct server
    """
    match pathname:
        case "/":
            return set_server(Server.BOUNE.value)
        case "/boune":
            return set_server(Server.BOUNE.value)
        case "/crail":
            return set_server(Server.CRAIL.value)
        case "/eratz":
            return set_server(Server.ERATZ.value)
        case "/galgarion":
            return set_server(Server.GALGARION.value)
        case "/henual":
            return set_server(Server.HENUAL.value)
        case _:
            return error_view()
