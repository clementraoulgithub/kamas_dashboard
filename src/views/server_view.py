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


def create_svg_metrics(
    is_less_avg: bool | None, is_less_min: bool | None, evolution: float
) -> tuple:
    """
    Return the icons img for the left metrics

    Args:
        is_less_avg (bool | None): is less than average
        is_less_min (bool | None): is less than min
        evolution (float): evolution

    Returns:
        tuple: the html.Div for the left metrics
    """
    if is_less_avg is not None:
        avg_icon = html.Img(
            src="/assets/svg/arrow-down.svg"
            if is_less_avg
            else "/assets/svg/arrow-up.svg",
            className="svg",
        )
    else:
        avg_icon = None

    if is_less_min is not None:
        min_icon = html.Img(
            src="/assets/svg/arrow-down.svg"
            if is_less_min
            else "/assets/svg/arrow-up.svg",
            className="svg",
        )
    else:
        min_icon = None

    if evolution != 0:
        evo_icon = html.Img(
            src="/assets/svg/arrow-down.svg"
            if evolution < 0
            else "/assets/svg/arrow-up.svg",
            className="svg",
        )
    else:
        evo_icon = None

    return avg_icon, min_icon, evo_icon


# pylint: disable=too-many-arguments
def left_metrics(
    average: float,
    mediane: float,
    deviation: float,
    deviation_related_to_average: str,
    best_price: float,
    best_price_server: str,
    website_link: str,
    is_less_avg: bool,
    is_less_min: bool,
    evolution: float,
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
    avg_icon, min_icon, evo_icon = create_svg_metrics(
        is_less_avg, is_less_min, evolution
    )
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Moyenne"),
                            html.Div(
                                [html.H1(f"{average}"), avg_icon],
                                className="best-price-server",
                            ),
                            html.H2("Eur/m"),
                        ],
                        className="graph-info",
                    ),
                    html.Div(
                        [
                            html.P("Ecart-type"),
                            html.Div(
                                [
                                    html.H1(f"{deviation}"),
                                    html.P(deviation_related_to_average),
                                ],
                                className="deviation-related-to-average",
                            ),
                            html.H2("Eur/m"),
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
                            html.H2("Eur/m"),
                        ],
                        className="graph-info",
                    ),
                    html.Div(
                        [
                            html.P("Meilleur prix"),
                            html.Div(
                                [html.H1(f"{best_price}"), min_icon],
                                className="best-price-server",
                            ),
                            html.H2("Eur/m"),
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
                                        evo_icon,
                                        href=website_link,
                                    ),
                                ],
                                className="best-price-server",
                            ),
                            html.H2("Lien"),
                        ],
                        className="graph-info",
                    ),
                    html.Div(
                        [
                            html.P("Evolution journalière"),
                            html.Div(
                                [
                                    html.H1(f"{evolution}%"),
                                ],
                                className="best-price-server",
                            ),
                            html.H2("%/m"),
                        ],
                        className="graph-info",
                    ),
                ],
                className="graph-info-avg",
            ),
        ],
        className="graph-info-container",
    )


def right_daily_graph(fig_day: go.Figure) -> html.Div:
    """
    Return the html.Div for the right daily graph

    Args:
        fig_day (go.Figure): the figure for the day

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
            0: "Cette Année",
            1: "-6 mois",
            2: "-3 mois",
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
                style={"display": "none"},
            ),
            slider,
        ],
        className="graph-line-container",
    )


# pylint: disable=too-many-arguments
def server_view(
    name: str,
    fig_day: go.Figure,
    best_price: float,
    best_price_server: str,
    website_link: str,
    is_less_avg: bool,
    is_less_min: bool,
    average: float,
    mediane: float,
    deviation: float,
    deviation_related_to_average: str,
    evolution: float,
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
                    html.Div(
                        [
                            html.Img(
                                src="/assets/svg/arrow-right.svg",
                                className="svg",
                                id="arrow-left",
                            ),
                            html.H2(f"Serveur {name.capitalize()}"),
                        ],
                        className="title-server",
                    ),
                    html.H3("Cours instantané du kamas", className="title-graph"),
                    html.Div(
                        [
                            left_metrics(
                                average,
                                mediane,
                                deviation,
                                deviation_related_to_average,
                                best_price,
                                best_price_server,
                                website_link,
                                is_less_avg,
                                is_less_min,
                                evolution,
                            ),
                            right_daily_graph(fig_day),
                        ],
                        className="graphs-container",
                    ),
                    html.H3("Cours du kamas sur période", className="title-graph"),
                    html.Div(
                        id="period-metrics",
                    ),
                    bottom_line_graph(),
                ],
                className="graph-main-content",
            ),
        ],
        className="graph-body-content",
    )
