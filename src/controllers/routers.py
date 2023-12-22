import dash

from src.controllers.server import server
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
            return server("boune")
        case "/boune":
            return server("boune")
        case "/crail":
            return server("crail")
        case "/eratz":
            return server("eratz")
        case "/galgarion":
            return server("galgarion")
        case "/henual":
            return server("henual")
        case _:
            return error_view()
