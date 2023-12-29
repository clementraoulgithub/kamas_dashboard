"""Return Index view."""

from dash import html

from src import NAME


def index_view() -> tuple[html.Div, dict[str, str], dict[str, str]]:
    """
    Return the html.Div for index page

    Returns:
        tuple[html.Div, dict[str, str], dict[str, str]]: the html.Div for index
    """

    description = f"Votre Source fiable pour le suivi quotidien du cours du kamas. \
    Découvrez la dynamique du marché du kamas avec {NAME}. \
    Ce site se consacre à fournir des graphiques intuitifs et des mises à jour en temps réel\
    sur l'évolution quotidienne du cours du Kamas. Que vous soyez un investisseur aguerri, \
    un joueur passionné ou simplement curieux des tendances économiques de Dofus, {NAME} \
    est l'outil indispensable pour rester informé et prendre des décisions éclairées."

    please_return_info = "Si vous avez quelques minutes à consacrer, \
    je serais ravis de connaître votre opinion sur le site."

    warning = "Ce site n'est pas affilié à Ankama Games. \
    Toutes les marques commerciales et marques déposées appartiennent \
    à leurs propriétaires respectifs."

    return (
        html.Div(
            [
                html.H2(f"Bienvenue sur {NAME}"),
                html.P("Choisissez un serveur dans le menu en haut à gauche"),
                html.Div(
                    [
                        html.H1(NAME),
                        html.P(f"Bienvenue sur {NAME},"),
                        html.P(description),
                        html.P(warning),
                        html.P(please_return_info),
                        html.P(
                            [
                                html.A(
                                    "@Muti",
                                    href="https://discord.com/users/446356755061145612",
                                )
                            ]
                        ),
                    ],
                    className="graph-info",
                ),
            ],
            className="graph-main-content",
        ),
        {"display": "none"},
        {"display": "none"},
        {"display": "none"},
    )
