"""Return Error view."""

from dash import html


def error_view() -> tuple[html.Div, dict[str, str], dict[str, str]]:
    """
    Return the html.Div for error

    Returns:
        tuple[html.Div, dict[str, str], dict[str, str]]: the html.Div for error
    """
    return (
        html.Div(
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
        ),
        {"display": "none"},
        {"display": "none"},
        {"display": "none"},
    )
