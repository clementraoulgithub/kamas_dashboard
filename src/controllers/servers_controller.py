"""Server controller"""


import dash

from src.utils.graphs import create_graphs
from src.utils.scraping import get_daily_kamas_value, get_yesterday_kamas_value
from src.views.server_view import server_view


def server(name: str) -> dash.html.Div:
    """
    return the html.Div for server

    Returns:
        html.Div: the html.Div for the boune server
    """
    description = f"Ces graphiques représentent les valeurs estimée du kamas en euros pour le serveur {name}"

    day_kamas_dict = get_daily_kamas_value(server=name)
    yesterday_kamas_dict = get_yesterday_kamas_value(server=name)

    if not day_kamas_dict:  # Case for the first fetch of the day
        day_kamas_dict = yesterday_kamas_dict

    fig_day, fig_gauge, best_price, deviation = create_graphs(
        day_kamas_dict, yesterday_kamas_dict
    )

    slider = dash.dcc.Slider(
        id="graph-slider",
        min=0,
        max=2,
        step=1,
        value=1,
        marks={0: "30 jours", 1: "7 jours", 2: "Aujourd'hui"},
        vertical=True,
    )

    return server_view(
        name,
        description,
        fig_day,
        fig_gauge,
        best_price,
        average=day_kamas_dict["average"] if day_kamas_dict else 0,
        deviation=deviation,
        nb_site=len(day_kamas_dict["kamas_dict"]) if day_kamas_dict else 0,
        graph_slider=slider,
    )
