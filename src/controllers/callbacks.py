import dash
from src.controllers.monocompte import monocompte_server
from src.controllers.home import home


@dash.callback(dash.Output("main-content", "children"), [dash.Input("url", "pathname")])
def callback(pathname):
    match pathname:
        case "/mono_server":
            return monocompte_server()
        case _:
            return home()
