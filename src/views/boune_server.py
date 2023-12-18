import plotly.graph_objs as go
from dash import dcc, html


def boune_view(
    model_description: str,
    fig_day: go.Figure,
    fig_average: go.Figure,
    fig_gauge: go.Figure,
    best_price: float,
    slider: dcc.Slider,
    average: float,
    nb_site: int,
) -> html.Div:
    return html.Div(
        [
            html.Div(
                [
                    html.H4("Devises"),
                    dcc.RadioItems(
                        id="radio-items",
                        className="radio-items",
                        options=[
                            {"label": "Euros", "value": "OPT1"},
                        ],
                        value="OPT1",
                    ),
                ],
                className="radio-items-container",
            ),
            html.Div(
                [
                    html.H3("Serveur Boune"),
                    html.P(model_description),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("Moyenne:"),
                                            html.H1(f"{average} €"),
                                        ],
                                        className="graph-info",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Meilleur prix:"),
                                            html.H1(f"{best_price} €"),
                                        ],
                                        className="graph-info",
                                    ),
                                    html.Div(
                                        dcc.Graph(
                                            figure=fig_gauge,
                                        ),
                                        className="graph-info",
                                    ),
                                ],
                                className="graph-info-container",
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        figure=fig_day,
                                        config={
                                            "displayModeBar": True,
                                            "displaylogo": False,
                                        },
                                    ),
                                    html.Div(
                                        [
                                            html.P("Nombre de sites"),
                                            html.H1(nb_site),
                                        ],
                                        className="graph-info",
                                    ),
                                ]
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        figure=fig_average,
                                        config={
                                            "displayModeBar": True,
                                            "displaylogo": False,
                                        },
                                    ),
                                    slider,
                                ]
                            ),
                        ],
                        className="graphs-content",
                    ),
                ],
                className="graph-main-content",
            ),
        ],
        className="graph-body-content",
    )
