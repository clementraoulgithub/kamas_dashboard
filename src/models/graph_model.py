import dataclasses

@dataclasses.dataclass
class GraphModel():
    title: str
    description: str
    x_title: str
    y_title: str
    x_values: list
    y_values: list