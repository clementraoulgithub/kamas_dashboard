import dash

from src.controllers.boune_server import boune_server
from src.controllers.crail_server import crail_server
from src.controllers.eratz_server import eratz_server
from src.controllers.galgarion_server import galgarion_server
from src.controllers.henual_server import henual_server
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
            return boune_server()
        case "/boune":
            return boune_server()
        case "/crail":
            return crail_server()
        case "/eratz":
            return eratz_server()
        case "/galgarion":
            return galgarion_server()
        case "/henual":
            return henual_server()
        case _:
            return error_view()
