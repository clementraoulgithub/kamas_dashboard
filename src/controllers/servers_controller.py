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


def calculate_metrics(day_kamas_dict: dict, yesterday_kamas_dict: dict) -> tuple:
    """
    Calculate the metrics

    Args:
        day_kamas_dict (dict): dictionnary of the day kamas
        yesterday_kamas_dict (dict): dictionnary of the yesterday kamas

    Returns:
        tuple: metrics
    """
    best_price = min(list(day_kamas_dict["kamas_dict"].values()))
    deviation = round(np.std(list(day_kamas_dict["kamas_dict"].values())), 2)
    average = day_kamas_dict["average"] if day_kamas_dict else 0

    deviation_related_to_average = (deviation / average) * 100 if average else 0
    deviation_related_to_average = round(deviation_related_to_average, 2)
    deviation_related_to_average = f"{deviation_related_to_average}%"

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

    evolution = (
        round(
            (day_kamas_dict["average"] - yesterday_kamas_dict["average"])
            / yesterday_kamas_dict["average"]
            * 100,
            2,
        )
        if day_kamas_dict
        else 0
    )

    return (
        best_price,
        best_price_server_name,
        website_link,
        is_less_avg,
        is_less_min,
        average,
        mediane,
        deviation,
        deviation_related_to_average,
        evolution,
    )


# pylint: disable=too-many-locals
def server(name: str) -> dash.html.Div:
    """
    return the html.Div for server

    Returns:
        html.Div: the html.Div for the boune server
    """
    day_kamas_dict = get_daily_kamas_value(server=name)
    yesterday_kamas_dict = get_yesterday_kamas_value(server=name)

    if not day_kamas_dict:  # Case for the first fetch of the day
        day_kamas_dict = yesterday_kamas_dict

    fig_day = create_graphs(day_kamas_dict)

    (
        best_price,
        best_price_server_name,
        website_link,
        is_less_avg,
        is_less_min,
        average,
        mediane,
        deviation,
        deviation_related_to_average,
        evolution,
    ) = calculate_metrics(day_kamas_dict, yesterday_kamas_dict)

    return server_view(
        name,
        fig_day,
        best_price,
        best_price_server_name,
        website_link,
        is_less_avg,
        is_less_min,
        average=average,
        mediane=mediane,
        deviation=deviation,
        deviation_related_to_average=deviation_related_to_average,
        evolution=evolution,
    )
