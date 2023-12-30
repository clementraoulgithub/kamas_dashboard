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

    is_less_avg = yesterday_kamas_dict["average"] > day_kamas_dict["average"]
    is_less_min = yesterday_kamas_dict["min"] > day_kamas_dict["min"]

    return server_view(
        name,
        description_lst,
        fig_day,
        fig_gauge,
        best_price,
        best_price_server_name,
        website_link,
        is_less_avg,
        is_less_min,
        average=day_kamas_dict["average"] if day_kamas_dict else 0,
        mediane=mediane,
        deviation=deviation,
        nb_site=len(day_kamas_dict["kamas_dict"]) if day_kamas_dict else 0,
    )
