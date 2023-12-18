import os

import dash

from src import PATH
from src.controllers.routers import routers # this import is necessary to register callbacks
from src.views.index import index_view

app = dash.Dash(
    __name__,
    assets_folder=os.path.join(PATH, "assets"),
)
app.layout = index_view()
