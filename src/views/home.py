from dash import html

def home_view() -> html.Div:
    return html.Div([
        html.H1("Home"),
        html.P("Ce site à pour but de visualiser le cours du kamas à travers le temps sur le serveur mono compte dofus rétro"),
    ])