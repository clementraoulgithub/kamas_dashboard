"""The Dash application."""

import dash

from src import NAME

# This import are needed to make the app work
# pylint: disable=unused-import
from src.controllers.graph_line_controller import graph_line_controller
from src.controllers.routers_controller import routers
from src.controllers.top_menu_buttons_controller import (
    toggle_menu_dofus_classic,
    toggle_menu_dofus_retro,
    toggle_menu_dofus_touch,
)
from src.views.template_view import template_view

app = dash.Dash(
    __name__, suppress_callback_exceptions=True, update_title="Chargement ..."
)
app.title = NAME
server = app.server
app.layout = template_view()
