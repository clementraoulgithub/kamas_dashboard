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


"""Routers controller module."""

import dash

from src.controllers.servers_controller import server
from src.utils import global_variables
from src.utils.enums import ServerClassic, ServerRetro, ServerTouch
from src.views.error_view import error_view
from src.views.index_view import index_view


def set_server(
    server_name: str,
) -> dash.html.Div:
    """
    Set the current server name

    Args:
        server_name (str): the server name
    """
    global_variables.current_server_name = server_name
    return server(server_name)


# pylint: disable=too-many-return-statements
@dash.callback(
    dash.Output("main-content", "children"),
    [dash.Input("url", "pathname")],
    prevent_initial_call=True,
)
def routers(pathname: str) -> dash.html.Div:
    """
    Route the url to the correct server

    Args:
        pathname (str): the url pathname

    Returns:
        dash.html.Div: the html.Div for the correct server
    """
    match pathname:
        case "/":
            return index_view()
        case "/boune":
            return set_server(ServerRetro.BOUNE.value)
        case "/crail":
            return set_server(ServerRetro.CRAIL.value)
        case "/eratz":
            return set_server(ServerRetro.ERATZ.value)
        case "/galgarion":
            return set_server(ServerRetro.GALGARION.value)
        case "/henual":
            return set_server(ServerRetro.HENUAL.value)
        case "/draconiros":
            return set_server(ServerClassic.DRACONIROS.value)
        case "/hellmina":
            return set_server(ServerClassic.HELLMINA.value)
        case "/imagiro":
            return set_server(ServerClassic.IMAGIRO.value)
        case "/ombre":
            return set_server(ServerClassic.OMBRE.value)
        case "/orukam":
            return set_server(ServerClassic.ORUKAM.value)
        case "/talkasha":
            return set_server(ServerClassic.TALKASHA.value)
        case "/tylezia":
            return set_server(ServerClassic.TYLEZIA.value)
        case "/brutas":
            return set_server(ServerTouch.BRUTAS.value)
        case "/dodge":
            return set_server(ServerTouch.DODGE.value)
        case "/grandapan":
            return set_server(ServerTouch.GRANDAPAN.value)
        case "/herdegrize":
            return set_server(ServerTouch.HERDEGRIZE.value)
        case "/oshimo":
            return set_server(ServerTouch.OSHIMO.value)
        case "/terra-cogita":
            return set_server(ServerTouch.TERRA_COGITA.value)
        case _:
            return error_view()
