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

"""This module create the div containing the metrics."""

from dash import html


class InstantMetricsView:
    """
    Create the div containing the metrics.
    """

    @staticmethod
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
    @classmethod
    def create_instant_metrics_view(
        cls,
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
        avg_icon, min_icon, evo_icon = cls.create_svg_metrics(
            is_less_avg, is_less_min, evolution
        )
        return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H1(f"{best_price}€"), min_icon],
                                    className="best-price-server",
                                ),
                                html.P("Meilleur prix"),
                            ],
                            className="graph-info",
                        ),
                        html.Div(
                            [
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
                                            target="_blank",
                                        ),
                                    ],
                                    className="best-price-server",
                                ),
                                html.P("Vendeur le moins cher"),
                            ],
                            className="graph-info-right",
                        ),
                    ],
                    className="graph-info-avg",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H1(f"{average}€"), avg_icon],
                                    className="best-price-server",
                                ),
                                html.P("Moyenne"),
                            ],
                            className="graph-info",
                        ),
                        html.Div(
                            [
                                html.H1(f"{mediane}€"),
                                html.P("Médiane"),
                            ],
                            className="graph-info-right",
                        ),
                    ],
                    className="graph-info-avg",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H1(f"{deviation}€"),
                                        html.P(deviation_related_to_average),
                                    ],
                                    className="deviation-related-to-average",
                                ),
                                html.P("Ecart-type"),
                            ],
                            className="graph-info",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [html.H1(f"{evolution}%"), evo_icon],
                                    className="best-price-server",
                                ),
                                html.P("Evolution journalière"),
                            ],
                            className="graph-info-right",
                        ),
                    ],
                    className="graph-info-avg",
                ),
            ],
            className="graph-info-container",
        )
