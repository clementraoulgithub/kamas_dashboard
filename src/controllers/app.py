import os

import dash

from src import PATH
from src.controllers.callbacks import callback
from src.views.index import index_view

app = dash.Dash(
    __name__,
    assets_folder=os.path.join(PATH, "assets"),
)
app.layout = index_view()
