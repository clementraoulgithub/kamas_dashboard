from dash import dcc
from dash import html
import plotly.graph_objs as go


def boune_view(
    model_description: str, fig_day: go.Figure, fig_average: go.Figure, slider
) -> html.Div:
    return html.Div(
        [
            html.Div(
                [
                    html.H4("Devises:"),
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
                    html.H3("> Serveur Monocompte"),
                    html.P(model_description),
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(
                                        figure=fig_day,
                                        config={
                                            "displayModeBar": True,
                                            "displaylogo": False,
                                        },
                                    )
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
