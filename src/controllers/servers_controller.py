"""Server controller"""


from dash import html

from src.utils.graphs import view_graph
from src.utils.scraping import (
    get_all_kamas_value,
    get_daily_kamas_value,
    get_yesterday_kamas_value,
)
from src.views.server_view import server_view


def server(name: str) -> html.Div:
    """
    return the html.Div for server

    Returns:
        html.Div: the html.Div for the boune server
    """
    description = f"Ces graphiques représentent les valeurs estimée du kamas en euros pour le serveur {name}"
    kamas_dict = get_all_kamas_value(server=name)
    day_kamas_dict = get_daily_kamas_value(server=name)
    yesterday_kamas_dict = get_yesterday_kamas_value(server=name)

    if not day_kamas_dict:  # Case for the first fetch of the day
        day_kamas_dict = yesterday_kamas_dict

    fig_day, fig_avg, fig_gauge, best_price, deviation = view_graph(
        day_kamas_dict, yesterday_kamas_dict, kamas_dict
    )

    return server_view(
        name,
        description,
        fig_day,
        fig_avg,
        fig_gauge,
        best_price,
        average=day_kamas_dict["average"] if day_kamas_dict else 0,
        deviation=deviation,
        nb_site=len(day_kamas_dict["kamas_dict"]) if day_kamas_dict else 0,
    )
