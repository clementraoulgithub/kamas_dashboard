import dash


@dash.callback(
    dash.Output("graph-day-container", "style"),
    [dash.Input("toggle-button", "n_clicks")],
)
def toggle_graph(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return {"display": "none"}
    else:
        return {"display": "block"}
