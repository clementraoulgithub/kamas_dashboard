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


"""Controller for the line graph."""

from typing import List

import dash

from src.utils import global_variables
from src.utils.enums import LineGraphScope
from src.utils.graphs import LineGraph
from src.utils.scraping.scraping import get_scope_kamas_value
from src.views.periodic_price_view.periodic_metrics_view import PeriodicMetricsView


def create_div_metrics(metric_lst: List[dict]) -> dash.html.Div:
    """
    Create indivual div for each metric.

    Args:
        metric_lst (List[dict]): each dict contains the metrics
    Returns:
        dash.html.Div: the div containing the metrics
    """
    return_lst: List[dash.html.Div] = [
        PeriodicMetricsView.create_metrics_view(metric_dict)
        for metric_dict in metric_lst
    ]
    return return_lst


@dash.callback(
    [
        dash.Output("graph-line", "figure"),
        dash.Output("graph-line", "style"),
        dash.Output("period-metrics", "children"),
    ],
    [dash.Input("graph-slider", "value")],
)
def graph_line_controller(value: int):
    """
    Controller for the line graph.

    Args:
        value (int): the value of the slider

    Returns:
        px.line: the line graph
    """
    scope = LineGraphScope(value).name.lower()
    kamas_dict = get_scope_kamas_value(
        server=global_variables.current_server_name,
        scope=scope,
    )

    line_graph = LineGraph(
        "Evolutions <br>du million de kamas",
        "",
        "Date UTC",
        "Valeurs estimées",
        [dict["timestamp"] for dict in kamas_dict],
        [dict["average"] for dict in kamas_dict],
        [dict["min"] for dict in kamas_dict],
    )

    graph, metrics = line_graph.create_line_graph()
    div_lst = create_div_metrics(metrics)

    metrics = PeriodicMetricsView.create_metrics_container_view(div_lst)

    return graph, {"display": "flex"}, metrics
