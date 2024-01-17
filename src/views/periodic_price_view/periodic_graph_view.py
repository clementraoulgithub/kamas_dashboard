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

"""This module create the div containing the periodic line graph view."""

import dash


# pylint: disable=too-few-public-methods
class PeriodicGraphView:
    """
    Periodic Graph View.
    """

    @staticmethod
    def create_periodic_graph_view() -> dash.html.Div:
        """
        Return the html.Div for the bottom line graph

        Returns:
            html.Div: the html.Div for the bottom line graph
        """
        slider = dash.dcc.Slider(
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

        return dash.html.Div(
            [
                slider,
                dash.dcc.Graph(
                    config={
                        "displayModeBar": False,
                        "displaylogo": False,
                    },
                    id="graph-line",
                    style={"display": "none"},
                ),
            ],
            className="graph-line-container",
        )
