from dash import dcc
from dash import html
import plotly.graph_objs as go

def boune_view(model_description: str, fig_average: go.Figure, fig_pic: go.Figure, slider) -> html.Div:
    warning_message = html.Div(
        [
            html.H3("ATTENTION"),
            html.P("Ce site est en cours de développement, les données affichées sont donc fausses"),
        ], className="warning-message"
    )
    return html.Div(
        [
            html.Div(
                [
                    html.H4("Devises:"),
                    dcc.RadioItems(
                        id='radio-items',
                        className="radio-items",
                        options=[
                            {'label': 'Euros', 'value': 'OPT1'},
                            {'label': 'Bitcoins', 'value': 'OPT2'},
                        ],
                        value='OPT1',
                    )
                ], className="radio-items-container"
            ),
            html.Div(
                [           
                    warning_message,
                    html.H1("> Serveur Monocompte"),
                    html.P(model_description),
                    html.Div(
                        [html.Div(
                            [
                                dcc.Graph(figure=fig_average, config={
                                    'displayModeBar': True,
                                    'displaylogo': False,
                                }),
                                slider
                            ]
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=fig_pic, config={
                                    'displayModeBar': True,
                                    'displaylogo': False,
                                }),
                            ]
                        )
                        ], className="graphs-content"
                    )
                ], className="graph-main-content"
            )
        ], className="graph-body-content"
    )