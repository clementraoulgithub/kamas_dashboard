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
