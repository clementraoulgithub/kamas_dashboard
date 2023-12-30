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


"""Module for buttons controlle of the top menu."""

import dash


def toggle(n_clicks: int, style: dict) -> tuple[dict[str, str]]:
    """
    Toggle the display of the top menu.

    Args:
        n_clicks (int): number of clicks
        style (dict): style of the top menu

    Returns:
        tuple[dict[str, str]]: the style of the top menu
    """
    if n_clicks and (style["display"] == "none"):
        return (
            {
                "display": "flex",
                "flex-direction": "column",
                "position": "absolute",
            },
            {"display": "none"},
            {"display": "none"},
        )
    return {"display": "none"}, {"display": "none"}, {"display": "none"}


@dash.callback(
    [
        dash.Output("top-menu-retro", "style", allow_duplicate=True),
        dash.Output("top-menu-classic", "style", allow_duplicate=True),
        dash.Output("top-menu-touch", "style", allow_duplicate=True),
    ],
    [dash.Input("button-top-menu-retro", "n_clicks")],
    [dash.State("top-menu-retro", "style")],
    prevent_initial_call=True,
)
def toggle_menu_dofus_retro(n_clicks: int, style: dict) -> tuple[dict[str, str]]:
    """
    Toggle the display of the top menu.

    Args:
        n_clicks (int): number of clicks
        style (dict): style of the top menu

    Returns:
        tuple[dict[str, str]]: the style of the top menu
    """
    return toggle(n_clicks, style)


@dash.callback(
    [
        dash.Output("top-menu-classic", "style", allow_duplicate=True),
        dash.Output("top-menu-retro", "style", allow_duplicate=True),
        dash.Output("top-menu-touch", "style", allow_duplicate=True),
    ],
    [dash.Input("button-top-menu-classic", "n_clicks")],
    [dash.State("top-menu-classic", "style")],
    prevent_initial_call=True,
)
def toggle_menu_dofus_classic(n_clicks: int, style: dict) -> tuple[dict[str, str]]:
    """
    Toggle the display of the top menu.

    Args:
        n_clicks (int): number of clicks
        style (dict): style of the top menu

    Returns:
        tuple[dict[str, str]]: the style of the top menu
    """
    return toggle(n_clicks, style)


@dash.callback(
    [
        dash.Output("top-menu-touch", "style", allow_duplicate=True),
        dash.Output("top-menu-retro", "style", allow_duplicate=True),
        dash.Output("top-menu-classic", "style", allow_duplicate=True),
    ],
    [dash.Input("button-top-menu-touch", "n_clicks")],
    [dash.State("top-menu-touch", "style")],
    prevent_initial_call=True,
)
def toggle_menu_dofus_touch(n_clicks: int, style: dict) -> tuple[dict[str, str]]:
    """
    Toggle the display of the top menu.

    Args:
        n_clicks (int): number of clicks
        style (dict): style of the top menu

    Returns:
        tuple[dict[str, str]]: the style of the top menu
    """
    return toggle(n_clicks, style)
