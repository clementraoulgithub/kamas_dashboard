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


"""Return Server view."""

import plotly.graph_objs as go
from dash import dcc, html


# pylint: disable=too-many-arguments
def left_metrics(
    average: float,
    mediane: float,
    deviation: float,
    best_price: float,
    best_price_server: str,
    website_link: str,
    fig_gauge: go.Figure,
    is_less_avg: bool,
    is_less_min: bool,
) -> html.Div:
    """
    Return the html.Div for the left metrics

    Args:
        average (float): average price
        deviation (float): deviation price
        best_price (float): best price
        fig_gauge (go.Figure): the figure for the gauge

    Returns:
        html.Div: the html.Div for the left metrics
    """
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Moyenne"),
                            html.Div(
                                [
                                    html.H1(f"{average}"),
                                    html.Img(
                                        src="/assets/svg/arrow-down.svg"
                                        if is_less_avg
                                        else "/assets/svg/arrow-up.svg",
                                        className="svg",
                                    ),
                                ],
                                className="best-price-server",
                            ),
                            html.H2("EUR/m"),
                        ],
                        className="graph-info",
                    ),
                    html.Div(
                        [
                            html.P("Ecart-type"),
                            html.H1(f"{deviation}"),
                            html.H2("EUR/m"),
                        ],
                        className="graph-info",
                    ),
                ],
                className="graph-info-avg",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Médiane"),
                            html.H1(f"{mediane}"),
                            html.H2("EUR/m"),
                        ],
                        className="graph-info",
                    ),
                    html.Div(
                        [
                            html.P("Meilleur prix"),
                            html.Div(
                                [
                                    html.H1(f"{best_price}"),
                                    html.Img(
                                        src="/assets/svg/arrow-down.svg"
                                        if is_less_min
                                        else "/assets/svg/arrow-up.svg",
                                        className="svg",
                                    ),
                                ],
                                className="best-price-server",
                            ),
                            html.H2("EUR/m"),
                        ],
                        className="graph-info",
                    ),
                ],
                className="graph-info-avg",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Vendeur le moins cher"),
                            html.Div(
                                [
                                    html.H1(f"{best_price_server}"),
                                    html.A(
                                        html.Img(
                                            src="/assets/svg/external-link.svg",
                                            className="svg",
                                            id="external-link",
                                        ),
                                        href=website_link,
                                    ),
                                ],
                                className="best-price-server",
                            ),
                        ],
                        className="graph-info",
                    ),
                    dcc.Graph(
                        figure=fig_gauge,
                        config={
                            "displayModeBar": False,
                            "displaylogo": False,
                        },
                        className="graph-info",
                    ),
                ],
                className="graph-info-avg-vertical",
            ),
        ],
        className="graph-info-container",
    )


def right_daily_graph(fig_day: go.Figure, nb_site: int) -> html.Div:
    """
    Return the html.Div for the right daily graph

    Args:
        fig_day (go.Figure): the figure for the day
        nb_site (int): the number of site

    Returns:
        html.Div: the html.Div for the right daily graph
    """
    return html.Div(
        [
            html.Div(
                [
                    dcc.Graph(
                        figure=fig_day,
                        config={
                            "displayModeBar": False,
                            "displaylogo": False,
                        },
                        id="graph-day",
                    ),
                    html.Div(
                        [
                            html.P("Nombre de sites"),
                            html.H1(nb_site, id="nb-site"),
                        ],
                        className="graph-info",
                    ),
                ],
                className="graph-day-container",
            ),
        ],
        className="graphs-content",
    )


def bottom_line_graph() -> html.Div:
    """
    Return the html.Div for the bottom line graph

    Returns:
        html.Div: the html.Div for the bottom line graph
    """
    slider = dcc.Slider(
        id="graph-slider",
        min=0,
        max=5,
        step=1,
        value=3,
        marks={
            0: "Année",
            1: "6 mois",
            2: "3 mois",
            3: "Ce mois",
            4: "Cette semaine",
            5: "Aujourd'hui",
        },
        vertical=False,
    )

    return html.Div(
        [
            dcc.Graph(
                config={
                    "displayModeBar": False,
                    "displaylogo": False,
                },
                id="graph-line",
            ),
            slider,
        ],
        className="graph-line-container",
    )


# pylint: disable=too-many-arguments
def server_view(
    name: str,
    model_description_lst: list,
    fig_day: go.Figure,
    fig_gauge: go.Figure,
    best_price: float,
    best_price_server: str,
    website_link: str,
    is_less_avg: bool,
    is_less_min: bool,
    average: float,
    mediane: float,
    deviation: float,
    nb_site: int,
) -> html.Div:
    """
    Return the html.Div for server

    Args:
        name (str): the server name
        model_description_lst (list): the model description
        fig_day (go.Figure): the figure for the day
        fig_gauge (go.Figure): the figure for the gauge
        best_price (float): the best price
        average (float): the average price
        mediane (float): the mediane price
        deviation (float): the deviation price
        nb_site (int): the number of site

    Returns:
        html.Div: the html.Div for the server
    """
    return html.Div(
        [
            html.Div(
                [
                    html.H2(f"Serveur {name.capitalize()}"),
                    html.P(model_description_lst),
                    html.Div(
                        [
                            left_metrics(
                                average,
                                mediane,
                                deviation,
                                best_price,
                                best_price_server,
                                website_link,
                                fig_gauge,
                                is_less_avg,
                                is_less_min,
                            ),
                            right_daily_graph(fig_day, nb_site),
                        ],
                        className="graphs-container",
                    ),
                    bottom_line_graph(),
                ],
                className="graph-main-content",
            ),
        ],
        className="graph-body-content",
    )
