import os
import dash
from src import PATH
from src.views.index import index_view
from src.controllers.callbacks import callback

app = dash.Dash(
    __name__,
    assets_folder=os.path.join(PATH, 'assets'),
)
app.layout = index_view()

