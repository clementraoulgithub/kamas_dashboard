# Nom du Projet: Kamas Dashboard
# Auteur: RAOUL Clément
# Date de Création: 17-12-2023
# Description: Ce projet à pour unique but de visualer le cours d'une devise virtuelle
# Licence: MIT License

"""Model for the graph"""

import dataclasses


@dataclasses.dataclass
class GraphModel:
    """
    Model for the graph
    """

    title: str
    description: str
    x_title: str
    y_title: str
    x_values: list
    y_values: list
