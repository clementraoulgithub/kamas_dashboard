import os

import dash

from src import PATH
from src.controllers.buttons_callback import toggle_graph
from src.controllers.routers import routers
from src.views.index import index_view

app = dash.Dash(
    __name__,
    assets_folder=os.path.join(PATH, "assets"),
    suppress_callback_exceptions=True,
)

app.layout = index_view()
