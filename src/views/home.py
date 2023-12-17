from dash import html

def home_view() -> html.Div:
    return html.Div([
        html.H1("Home"),
        html.P("home"),
    ])