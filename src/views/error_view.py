"""Return Error view."""

from dash import html


def error_view() -> html.Div:
    """
    Return the html.Div for error

    Returns:
        html.Div: the html.Div for error
    """
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Erreur 404"),
                    html.P("La page que vous cherchez n'existe pas"),
                ],
                className="graph-info-container",
            ),
        ],
        className="graph-info",
    )
