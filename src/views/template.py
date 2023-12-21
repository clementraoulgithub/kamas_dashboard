from dash import dcc, html

from src import NAME


def index_view() -> html.Div:
    # Header
    header = html.Header(
        children=[
            html.Div(
                [
                    html.Img(src="/assets/ressources/logo.png", className="logo"),
                    html.H3(children=NAME.capitalize()),
                ],
                className="header-container",
            ),
            html.P("Visualisation de valeurs de kamas"),
        ],
        className="header",
    )

    # Footer
    footer = html.Footer(
        html.P(children=f"© {NAME} 2023, work in progress", className="footer")
    )

    # Top Menu
    top_menu = html.Div(
        [
            dcc.Link("Serveur Boune", href="/boune", className="link"),
            dcc.Link("Serveur Crail", href="/crail", className="link"),
            dcc.Link("Serveur Eratz", href="/eratz", className="link"),
            dcc.Link("Serveur Galgarion", href="/galgarion", className="link"),
            dcc.Link("Serveur Henual", href="/henual", className="link"),
        ],
        className="top-menu",
    )

    content = html.Div(className="main-content", id="main-content")

    # Layout with all components
    return html.Div(
        children=[
            header,
            dcc.Location(id="url"),
            top_menu,
            content,
            footer,
        ],
        className="body",
    )
