"""Return Server view."""

import plotly.graph_objs as go
from dash import dcc, html


def server_view(
    name: str,
    model_description: str,
    fig_day: go.Figure,
    fig_average: go.Figure,
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
        fig_average (go.Figure): the figure for the average
        fig_gauge (go.Figure): the figure for the gauge
        best_price (float): the best price
        average (float): the average price
        deviation (float): the deviation price
        nb_site (int): the number of site

    Returns:
        html.Div: the html.Div for the server
    """
    #TODO: split this function
    return html.Div(
        [
            html.Div(
                [
                    html.H2(f"Serveur {name.capitalize()}"),
                    html.P(model_description),
                    html.Div(
                        [
                            html.Div(
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
                                                    html.P("Ecart type"),
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
                            ),
                            html.Div(
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
                            ),
                        ],
                        className="graphs-container",
                    ),
                    html.Div(
                        [
                            dcc.Graph(
                                figure=fig_average,
                                config={
                                    "displayModeBar": False,
                                    "displaylogo": False,
                                },
                            ),
                        ]
                    ),
                ],
                className="graph-main-content",
            ),
        ],
        className="graph-body-content",
    )
