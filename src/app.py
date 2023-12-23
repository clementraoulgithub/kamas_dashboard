"""The Dash application."""

import dash

from src import NAME
from src.controllers.graph_line_controller import graph_line_controller

# This import is needed to make the app work with Dash
from src.controllers.routers_controller import routers
from src.views.template_view import template_view

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)
app.title = NAME
server = app.server
app.layout = template_view()
