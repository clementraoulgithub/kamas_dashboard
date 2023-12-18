from dash import html
from dash import dcc
from src import NAME


def index_view() -> html.Div:
    # Header
    header = html.Header(
        children=[
            html.Img(src="assets/ressources/logo.png", className="logo"),
            html.H1(children=NAME.upper()),
        ],
        className="header",
    )

    # Footer
    footer = html.Footer(html.P(children=f"© {NAME} 2023, work in progress", className="footer"))

    # Left Menu
    top_menu = html.Div(
        [
            dcc.Link("Home", href="/"),
            dcc.Link("Serveur Boune", href="/mono_server"),
        ],
        className="top-menu",
    )

    content = html.Div(className="main-content", id="main-content")

    # Layout with all components
    return html.Div(
        children=[header, dcc.Location(id="url", refresh=False), top_menu, content, footer],
        className="body",
    )
