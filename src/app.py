import os

import dash

from src import NAME
from src.controllers.layout import create_layout
from src.controllers.routers import routers
from src.views.template import index_view

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)
app.title = NAME
server = app.server
app.layout = create_layout()
