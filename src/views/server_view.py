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
    nb_site: int,
) -> html.Div:
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
                                            html.P("Moyenne"),
                                            html.H1(f"{average}"),
                                            html.H2("EUR/m"),
                                        ],
                                        className="graph-info",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Meilleur prix"),
                                            html.H1(f"{best_price}"),
                                            html.H2("EUR/m"),
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
