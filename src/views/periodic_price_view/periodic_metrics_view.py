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

"""This module create each periodic metrics div."""

import dash


class PeriodicMetricsView:
    """
    This class create each periodic metrics div.
    """

    @staticmethod
    def create_metrics_view(metric_dict: dict[str, str]) -> dash.html.Div:
        """
        Create indivual div for each metric.

        Args:
            metric_dict (dict[str, str]): each dict contains the metrics

        Returns:
            dash.html.Div: the div containing the metrics
        """
        return dash.html.Div(
            [
                dash.html.Div(
                    [
                        dash.html.H1(metric_dict["average_value"]),
                        dash.html.P("Moyenne"),
                    ],
                    className="graph-info",
                ),
                dash.html.Div(
                    [
                        dash.html.H1(metric_dict["deviation"]),
                        dash.html.P("Ecart-type"),
                    ],
                    className="graph-info",
                ),
                dash.html.Div(
                    [
                        dash.html.H1(metric_dict["deviation_related_to_average"]),
                        dash.html.P("Ecart-type relatif"),
                    ],
                    className="graph-info",
                ),
                dash.html.Div(
                    [
                        dash.html.H1(metric_dict["increase_rate"]),
                        dash.html.P("Taux de croissance"),
                    ],
                    className="graph-info-right",
                ),
            ],
            className="graph-info-avg",
        )

    @staticmethod
    def create_metrics_container_view(div_lst: list[dash.html.Div]) -> dash.html.Div:
        """
        Create the div containing the metrics.

        Args:
            div_lst (list[dash.html.Div]): the list of div containing the metrics

        Returns:
            dash.html.Div: the div containing the metrics
        """
        return dash.html.Div(
            [
                dash.html.P("Prix moyen", className="graph-info-title"),
                div_lst[0],
                dash.html.P("Prix minimum", className="graph-info-title"),
                div_lst[1],
            ],
            className="graph-info-container-period",
        )
