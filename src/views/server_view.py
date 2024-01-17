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
from dash import html

from src.views.instant_price_view.instant_graph_view import InstantGraphView
from src.views.instant_price_view.instant_metrics_view import InstantMetricsView
from src.views.periodic_price_view.periodic_graph_view import PeriodicGraphView


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
                    html.H2(f"Serveur {name.capitalize()}"),
                    html.Div(className="graph-separator"),
                    html.Div(
                        [
                            html.Img(
                                src="/assets/svg/arrow-bottom.svg",
                                className="svg",
                                id="arrow-bottom",
                            ),
                            html.H3(
                                "Cours instantané du kamas", className="title-graph"
                            ),
                        ],
                        className="title-server",
                    ),
                    html.Div(
                        [
                            InstantMetricsView.create_instant_metrics_view(
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
                            InstantGraphView.create_instant_graph_view(fig_day),
                        ],
                        className="graphs-container",
                    ),
                    html.Div(className="graph-separator"),
                    html.Div(
                        [
                            html.Img(
                                src="/assets/svg/arrow-bottom.svg",
                                className="svg",
                                id="arrow-bottom",
                            ),
                            html.H3(
                                "Cours du kamas sur période", className="title-graph"
                            ),
                        ],
                        className="title-server",
                    ),
                    html.Div(
                        id="period-metrics",
                    ),
                    PeriodicGraphView.create_periodic_graph_view(),
                ],
                className="graph-main-content",
            ),
        ],
        className="graph-body-content",
    )
