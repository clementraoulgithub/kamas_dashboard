from dash import html

from src.utils.backend.backend import backend_get_kamas_value
from src.utils.scraping import get_daily_kamas_value, get_yesterday_kamas_value
from src.utils.utils import create_daily_graph, create_gauche_graph, create_graph
from src.views.boune_server import boune_view


def monocompte_server() -> html.Div:
    description = "Ces graphiques représentent les valeurs estimée du kamas en euros pour le serveur mono compte dofus rétro"
    kamas_dict = backend_get_kamas_value()
    day_kamas_dict = get_daily_kamas_value()
    yesterday_kamas_dict = get_yesterday_kamas_value()

    best_price = min(list(day_kamas_dict["kamas_dict"].values()))

    fig_avg = create_graph(
        "Evolution du cours du kamas",
        "",
        "Tps",
        "Valeur estimée moyenne",
        [dict["timestamp"] for dict in kamas_dict],
        [dict["average"] for dict in kamas_dict],
        [dict["max"] for dict in kamas_dict],
        [dict["min"] for dict in kamas_dict],
    )

    fig_day = create_daily_graph(
        "Valeur journalière du kamas",
        "",
        "Jour",
        "Valeur estimée journalière",
        day_kamas_dict["kamas_dict"],
    )

    fig_gauge = create_gauche_graph(yesterday_kamas_dict["average"], day_kamas_dict["average"])

    return boune_view(
        description,
        fig_day,
        fig_avg,
        fig_gauge,
        best_price,
        average=day_kamas_dict["average"],
        nb_site=len(day_kamas_dict["kamas_dict"]),
    )
