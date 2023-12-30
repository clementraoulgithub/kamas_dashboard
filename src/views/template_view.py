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


"""Main template view for the app."""

import dash

from src import NAME


def header() -> dash.html.Header:
    """
    return the header of the app

    Returns:
        dash.html.Header: the header of the app
    """
    return dash.html.Header(
        children=[
            dash.html.Div(
                [
                    dash.html.A(
                        dash.html.Img(src="/assets/logo.png", className="logo"),
                        href="/",
                        id="logo-link",
                    ),
                    dash.html.Div(
                        [
                            dash.html.H3(children=NAME),
                            dash.html.P("Visualisation de valeurs de kamas"),
                        ],
                        className="header-text",
                    ),
                ],
                className="header-container",
            ),
        ],
        className="header",
    )


def footer() -> dash.html.Footer:
    """
    return the footer of the app

    Returns:
        dash.html.Footer: the footer of the app
    """
    return dash.html.Footer(
        dash.html.P(children=f"© {NAME} 2023, work in progress", className="footer")
    )


def dofus_retro_menu() -> dash.html.Div:
    """
    return the dofus retro menu of the app

    Returns:
        dash.html.Div: the dofus retro menu of the app
    """
    return dash.html.Div(
        dash.html.Div(
            [
                dash.html.Button("Dofus Retro", id="button-top-menu-retro"),
                dash.html.Div(
                    [
                        dash.dcc.Link("Serveur Boune", href="/boune", className="link"),
                        dash.dcc.Link("Serveur Crail", href="/crail", className="link"),
                        dash.dcc.Link("Serveur Eratz", href="/eratz", className="link"),
                        dash.dcc.Link(
                            "Serveur Galgarion", href="/galgarion", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Henual", href="/henual", className="link"
                        ),
                    ],
                    style={"display": "none"},
                    id="top-menu-retro",
                ),
            ]
        )
    )


def dofus_classic_menu() -> dash.html.Div:
    """
    return the dofus classic menu of the app

    Returns:
        dash.html.Div: the dofus retro menu of the app
    """
    return dash.html.Div(
        dash.html.Div(
            [
                dash.html.Button("Dofus 2", id="button-top-menu-classic"),
                dash.html.Div(
                    [
                        dash.dcc.Link(
                            "Serveur Draconiros", href="/draconiros", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur HellMina", href="/hellmina", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Imagiro", href="/imagiro", className="link"
                        ),
                        dash.dcc.Link("Serveur Ombre", href="/ombre", className="link"),
                        dash.dcc.Link(
                            "Serveur Orukam", href="/orukam", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Talkasha", href="/talkasha", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Tylezia", href="/tylezia", className="link"
                        ),
                    ],
                    style={"display": "none"},
                    id="top-menu-classic",
                ),
            ]
        )
    )


def dofus_touch_menu() -> dash.html.Div:
    """
    return the dofus touch menu of the app

    Returns:
        dash.html.Div: the dofus touch menu of the app
    """
    return dash.html.Div(
        dash.html.Div(
            [
                dash.html.Button("Dofus Touch", id="button-top-menu-touch"),
                dash.html.Div(
                    [
                        dash.dcc.Link(
                            "Serveur Brutas", href="/brutas", className="link"
                        ),
                        dash.dcc.Link("Serveur Dodge", href="/dodge", className="link"),
                        dash.dcc.Link(
                            "Serveur Grandapan", href="/grandapan", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Herdegrize", href="/herdegrize", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Oshimo", href="/oshimo", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Terra Cogita",
                            href="/terra-cogita",
                            className="link",
                        ),
                    ],
                    style={"display": "none"},
                    id="top-menu-touch",
                ),
            ]
        )
    )


def top_menu() -> dash.html.Div:
    """
    return the top menu of the app

    Returns:
        dash.html.Div: the top menu of the app

    )
    """

    return dash.html.Div(
        [dofus_retro_menu(), dofus_classic_menu(), dofus_touch_menu()],
        className="top-menu",
    )


def template_view() -> dash.html.Div:
    """
    return the template view of the app

    Returns:
        dash.html.Div: the template view of the app
    """
    content = dash.html.Div(className="main-content", id="main-content")
    return dash.html.Div(
        children=[
            header(),
            dash.dcc.Location(id="url"),
            top_menu(),
            dash.html.Div(
                children=[
                    content,
                    footer(),
                ],
                className="body-container",
            ),
        ],
        className="container",
    )
