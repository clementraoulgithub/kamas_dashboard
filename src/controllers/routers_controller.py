import dash

from src.controllers.servers_controller import server
from src.utils.tools import Server
from src.views.error_view import error_view


@dash.callback(dash.Output("main-content", "children"), [dash.Input("url", "pathname")])
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
            return server(Server.BOUNE.value)
        case "/boune":
            return server(Server.BOUNE.value)
        case "/crail":
            return server(Server.CRAIL.value)
        case "/eratz":
            return server(Server.ERATZ.value)
        case "/galgarion":
            return server(Server.GALGARION.value)
        case "/henual":
            return server(Server.HENUAL.value)
        case _:
            return error_view()
