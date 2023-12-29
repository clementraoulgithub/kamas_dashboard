"""Routers controller module."""

import dash

from src.controllers.servers_controller import server
from src.utils import global_variables
from src.utils.enums import ServerClassic, ServerRetro, ServerTouch
from src.views.error_view import error_view
from src.views.index_view import index_view


def set_server(
    server_name: str,
) -> tuple[dash.html.Div, dict[str, str], dict[str, str]]:
    """
    Set the current server name

    Args:
        server_name (str): the server name
    """
    global_variables.current_server_name = server_name
    return (
        server(server_name),
        {"display": "none"},
        {"display": "none"},
        {"display": "none"},
    )


# pylint: disable=too-many-return-statements
@dash.callback(
    [
        dash.Output("main-content", "children"),
        dash.Output("top-menu-retro", "style", allow_duplicate=True),
        dash.Output("top-menu-classic", "style", allow_duplicate=True),
        dash.Output("top-menu-touch", "style", allow_duplicate=True),
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
            return index_view()
        case "/boune":
            return set_server(ServerRetro.BOUNE.value)
        case "/crail":
            return set_server(ServerRetro.CRAIL.value)
        case "/eratz":
            return set_server(ServerRetro.ERATZ.value)
        case "/galgarion":
            return set_server(ServerRetro.GALGARION.value)
        case "/henual":
            return set_server(ServerRetro.HENUAL.value)
        case "/draconiros":
            return set_server(ServerClassic.DRACONIROS.value)
        case "/hellmina":
            return set_server(ServerClassic.HELLMINA.value)
        case "/imagiro":
            return set_server(ServerClassic.IMAGIRO.value)
        case "/ombre":
            return set_server(ServerClassic.OMBRE.value)
        case "/orukam":
            return set_server(ServerClassic.ORUKAM.value)
        case "/talkasha":
            return set_server(ServerClassic.TALKASHA.value)
        case "/tylezia":
            return set_server(ServerClassic.TYLEZIA.value)
        case "/brutas":
            return set_server(ServerTouch.BRUTAS.value)
        case "/dodge":
            return set_server(ServerTouch.DODGE.value)
        case "/grandapan":
            return set_server(ServerTouch.GRANDAPAN.value)
        case "/herdegrize":
            return set_server(ServerTouch.HERDEGRIZE.value)
        case "/oshimo":
            return set_server(ServerTouch.OSHIMO.value)
        case "/terra-cogita":
            return set_server(ServerTouch.TERRA_COGITA.value)
        case _:
            return error_view()
