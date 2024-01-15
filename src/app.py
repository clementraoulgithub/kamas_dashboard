# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""The Dash application."""

import os
import dash

from src import NAME, PATH

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

css_files = os.listdir(os.path.join(PATH, "assets", "css"))
external_css = [f for f in css_files if f.endswith(".css")]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    update_title="Chargement ...",
    external_stylesheets=external_css,
)
app.title = NAME
server = app.server
app.layout = template_view()
