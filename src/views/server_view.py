"""Return Server view."""

import plotly.graph_objs as go
from dash import dcc, html


def left_metrics(
    average: float, deviation: float, best_price: float, fig_gauge: go.Figure
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
                            html.H1(f"{average}"),
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
                    html.P("Meilleur prix"),
                    html.H1(f"{best_price}", id="best-price"),
                    html.H2("EUR/m", id="best-price"),
                ],
                className="graph-info",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig_gauge,
                    config={
                        "displayModeBar": False,
                        "displaylogo": False,
                    },
                ),
                className="graph-info",
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
        vertical=True,
    )

    return html.Div(
        [
            slider,
            dcc.Graph(
                config={
                    "displayModeBar": False,
                    "displaylogo": False,
                },
                id="graph-line",
            ),
        ],
        className="graph-line-container",
    )


# pylint: disable=too-many-arguments
def server_view(
    name: str,
    model_description: str,
    fig_day: go.Figure,
    fig_gauge: go.Figure,
    best_price: float,
    average: float,
    deviation: float,
    nb_site: int,
) -> html.Div:
    """
    Return the html.Div for server

    Args:
        name (str): the server name
        model_description (str): the model description
        fig_day (go.Figure): the figure for the day
        fig_gauge (go.Figure): the figure for the gauge
        best_price (float): the best price
        average (float): the average price
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
                    html.P(model_description),
                    html.Div(
                        [
                            left_metrics(average, deviation, best_price, fig_gauge),
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
