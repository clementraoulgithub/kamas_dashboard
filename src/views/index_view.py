# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
    je serais ravis de connaître votre opinion sur le site via Discord."

    warning = "Ce site n'est pas affilié à Ankama Games. \
    Toutes les marques commerciales et marques déposées appartiennent \
    à leurs propriétaires respectifs."

    # pylint: disable=line-too-long
    description_lst = [
        "Les graphiques illustrent les estimations du kamas en euros pour chaque serveur ",
        "sur les différents sites de vente de kamas.",
        html.Br(),
        "Les valeurs sont évaluées en se basant sur ",
        html.B("les offres de vente les plus basses."),
        html.Br(),
        html.B(
            "Les sites avec plusieurs vendeurs ne prennent en compte que les vendeurs connectés."
        ),
    ]

    return (
        html.Div(
            [
                html.H2(f"Bienvenue sur {NAME}"),
                html.P("Choisissez un serveur dans le menu en haut à gauche"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H1(NAME, className="title"),
                                html.P(f"Bienvenue sur {NAME},"),
                                html.P(description, className="description white-p"),
                                html.P(
                                    description_lst, className="description white-p"
                                ),
                                html.P(warning, className="description white-p"),
                                html.P(please_return_info),
                                html.P(
                                    html.A(
                                        "Discord",
                                        href="https://discord.gg/C8yfV92Bpu",
                                        target="_blank",
                                        className="discord-link",
                                    )
                                ),
                            ],
                        ),
                        html.Iframe(
                            src="https://discord.com/widget?id=1190426977535008768&theme=dark",
                            width="350",
                            height="350",
                            sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts",
                            className="discord",
                        ),
                    ],
                    className="graph-info",
                    id="index-info",
                ),
            ],
            className="graph-main-content",
        ),
        {"display": "none"},
        {"display": "none"},
        {"display": "none"},
    )
