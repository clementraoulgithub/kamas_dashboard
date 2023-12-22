import os

import dash

from src import NAME, PATH
from src.controllers.routers import routers
from src.views.template import index_view

app = dash.Dash(
    __name__,
    assets_folder=os.path.join(PATH, "assets"),
    suppress_callback_exceptions=True,
)
app.title = NAME
server = app.server

# Header
header = dash.html.Header(
    children=[
        dash.html.Div(
            [
                dash.html.Img(src="/assets/ressources/logo.png", className="logo"),
                dash.html.H3(children=NAME.capitalize()),
            ],
            className="header-container",
        ),
        dash.html.P("Visualisation de valeurs de kamas"),
    ],
    className="header",
)

# Footer
footer = dash.html.Footer(
    dash.html.P(children=f"© {NAME} 2023, work in progress", className="footer")
)

# Top Menu
top_menu = dash.html.Div(
    [
        dash.dcc.Link("Serveur Boune", href="/boune", className="link"),
        dash.dcc.Link("Serveur Crail", href="/crail", className="link"),
        dash.dcc.Link("Serveur Eratz", href="/eratz", className="link"),
        dash.dcc.Link("Serveur Galgarion", href="/galgarion", className="link"),
        dash.dcc.Link("Serveur Henual", href="/henual", className="link"),
    ],
    className="top-menu",
)

content = dash.html.Div(className="main-content", id="main-content")

app.layout = dash.html.Div(
    children=[
        header,
        dash.dcc.Location(id="url"),
        top_menu,
        content,
        footer,
    ],
    className="body",
)
