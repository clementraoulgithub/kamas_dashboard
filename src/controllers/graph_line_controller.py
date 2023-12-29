# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

"""Controller for the line graph."""

import dash

from src.utils import global_variables
from src.utils.enums import LineGraphScope
from src.utils.graphs import LineGraph
from src.utils.scraping.scraping import get_scope_kamas_value


@dash.callback(
    dash.Output("graph-line", "figure"), [dash.Input("graph-slider", "value")]
)
def graph_line_controller(value: int):
    """
    Controller for the line graph.

    Args:
        value (int): the value of the slider

    Returns:
        px.line: the line graph
    """
    scope = LineGraphScope(value).name.lower()
    kamas_dict = get_scope_kamas_value(
        server=global_variables.current_server_name,
        scope=scope,
    )

    line_graph = LineGraph(
        "Evolution moyenne<br>du million de kamas",
        "",
        "Tps",
        "Valeur estimée moyenne",
        [dict["timestamp"] for dict in kamas_dict],
        [dict["average"] for dict in kamas_dict],
    )

    return line_graph.create_line_graph()
