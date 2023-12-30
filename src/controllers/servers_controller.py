# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

"""Server controller"""


import dash
import numpy as np

from src.utils.enums import Website
from src.utils.graphs import create_graphs
from src.utils.scraping.scraping import get_daily_kamas_value, get_yesterday_kamas_value
from src.views.server_view import server_view


def get_best_price_server(day_kamas_dict: dict, best_price: float) -> tuple:
    """
    Return the best price server name and link

    Args:
        day_kamas_dict (dict): dictionnary of the day kamas
        best_price (float): best price

    Returns:
        tuple: best price server name and link
    """
    best_price_server_name = next(
        (
            site
            for site, price in day_kamas_dict["kamas_dict"].items()
            if price == best_price
        ),
        "",
    )

    if best_price_server_name:
        website = best_price_server_name.upper().replace(" ", "_")
        website_link = Website[website].value[1]
    else:
        website_link = ""

    return best_price_server_name, website_link


def server(name: str) -> dash.html.Div:
    """
    return the html.Div for server

    Returns:
        html.Div: the html.Div for the boune server
    """
    # pylint: disable=line-too-long
    description_lst = [
        "Les graphiques suivants illustrent les estimations du kamas en euros pour le serveur ",
        dash.html.B(name.capitalize()),
        " sur les différents sites de vente de kamas.",
        dash.html.Br(),
        "Les valeurs sont évaluées en se basant sur ",
        dash.html.B("les offres de vente les plus basses."),
        dash.html.Br(),
        dash.html.B(
            "Les sites avec plusieurs vendeurs ne prennent en compte que les vendeurs connectés."
        ),
    ]

    day_kamas_dict = get_daily_kamas_value(server=name)
    yesterday_kamas_dict = get_yesterday_kamas_value(server=name)

    if not day_kamas_dict:  # Case for the first fetch of the day
        day_kamas_dict = yesterday_kamas_dict

    fig_day, fig_gauge, best_price, deviation = create_graphs(
        day_kamas_dict, yesterday_kamas_dict
    )

    mediane = (
        round(np.median(list(day_kamas_dict["kamas_dict"].values())), 2)
        if day_kamas_dict
        else 0
    )

    best_price_server_name, website_link = get_best_price_server(
        day_kamas_dict, best_price
    )

    return server_view(
        name,
        description_lst,
        fig_day,
        fig_gauge,
        best_price,
        best_price_server_name,
        website_link,
        average=day_kamas_dict["average"] if day_kamas_dict else 0,
        mediane=mediane,
        deviation=deviation,
        nb_site=len(day_kamas_dict["kamas_dict"]) if day_kamas_dict else 0,
    )
