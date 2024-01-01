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


"""Module for plotly graphs."""

import datetime
from typing import Dict

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.models.graph_model import GraphModel
from src.utils.enums import Website


def create_graphs(day_kamas_dict: dict) -> tuple:
    """
    return all the graph for the server

    Args:
        day_kamas_dict (dict): dict of the day kamas value
        yesterday_kamas_dict (dict): dict of the yesterday kamas value

    Returns:
        tuple: all the graph for the server
    """
    bar_graph = BarGraph(
        "Valeur journalière<br>du million de kamas",
        "",
        "Jour",
        "Valeur estimée journalière",
        day_kamas_dict["kamas_dict"],
    )
    return bar_graph.create_bar_graph()


class BarGraph:
    """
    Daily bar graph, with average value and deviation value
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self, title: str, description: str, x_title: str, y_title: str, x_values: dict
    ):
        self.title = title
        self.description = description
        self.x_title = x_title
        self.y_title = y_title
        self.x_values = x_values

    def create_links(self) -> None:
        """
        Create links for the graph
        """
        web_dict: Dict[str, float] = {}
        for key, value in self.x_values.items():
            try:
                key = Website[key.upper().replace(" ", "_")]
                web_dict[f'<a href="{key.value[1]}">{key.value[0]}</a>'] = value
            except KeyError:
                web_dict[key] = value

        self.x_values = web_dict

    def create_bar_graph(
        self,
    ) -> px.line:
        """
        Create a daily graph
        Returns:
            px.line: the daily graph
        """
        self.create_links()
        model = GraphModel(
            title=self.title,
            description=self.description,
            x_title=self.x_title,
            y_title=self.y_title,
            x_values=list(self.x_values.values()),
            y_values=list(self.x_values.keys()),
        )
        average_value = round(np.mean(list(self.x_values.values())), 2)

        dataframe = pd.DataFrame(
            data={
                "Site": list(self.x_values.keys()),
                "Valeurs": list(self.x_values.values()),
                "Moyenne": average_value,
            }
        )
        fig = px.bar(
            dataframe,
            x="Site",
            y="Valeurs",
            title=f"<b>{model.title}</b>",
            text="Valeurs",
            labels={"Valeurs": "Valeurs estimées (million)"},
        )
        self.add_price_annotations(fig)
        self.update_layout(fig, average_value)

        return fig

    def add_average_values(
        self, fig: go.Figure, average_value: float, deviation_value: float
    ) -> None:
        """
        Add average values to the graph

        Args:
            fig (go.Figure): the figure
            average_value (float): the average value
            deviation_value (float): the deviation value
        """
        # Add average value
        fig.add_hline(
            y=average_value,
            line_dash="dash",
            line_color="red",
            name="Moyenne",
            annotation={
                "text": f"Moy: {average_value}",
                "xref": "paper",
                "yref": "y",
                "x": 1.0,
                "y": average_value,
                "showarrow": False,
            },
        )
        # Add deviation rectangle value
        fig.add_hrect(
            y0=average_value - deviation_value,
            y1=average_value + deviation_value,
            line_width=0,
            fillcolor="rgba(255, 255, 255, 0.2)",
            opacity=0.2,
        )

    def add_price_annotations(self, fig: go.Figure) -> None:
        """
        Add price annotations to the graph

        Args:
            fig (go.Figure): the figure
        """
        min_value, max_value = min(self.x_values.values()), max(self.x_values.values())
        min_lst = [key for key, value in self.x_values.items() if value == min_value]
        max_lst = [key for key, value in self.x_values.items() if value == max_value]

        if min_value and max_value and min_value != max_value:
            for value in min_lst:
                fig.add_annotation(
                    text="Vendeur le moins cher",
                    x=value,
                    y=min_value,
                    arrowhead=1,
                    showarrow=True,
                )
            for value in max_lst:
                fig.add_annotation(
                    text="Vendeur le plus cher",
                    x=value,
                    y=max_value,
                    arrowhead=1,
                    showarrow=True,
                )

    def update_layout(self, fig: go.Figure, average_value: float) -> None:
        """
        Update the layout of the graph

        Args:
            fig (go.Figure): the figure
            average_value (float): the average value
        """
        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0, 0, 0, 0)",
            paper_bgcolor="rgba(0, 0, 0, 0)",
        )

        fig.update_traces(
            marker_color=[
                "#00C58E" if value < average_value else "#FA4B3A"
                for value in list(self.x_values.values())
            ],
        )
        fig.update_xaxes(title_text="Sites de ventes")
        fig.update_yaxes(title_text="Valeurs estimées (million)")


class LineGraph:
    """
    Line graph, with average value and deviation value
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        title: str,
        description: str,
        x_title: str,
        y_title: str,
        x_values: list,
        y_avg_values: list,
        y_min_values: list,
    ):
        self.title = title
        self.description = description
        self.x_title = x_title
        self.y_title = y_title
        self.x_values = x_values
        self.y_avg_values = y_avg_values
        self.y_min_values = y_min_values

    def create_line_graph(self) -> px.line:
        """
        Create a line graph

        Returns:
            px.line: the line graph
        """
        x_values = [
            datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
            for date in self.x_values
        ]

        fig = go.Figure()
        fig.add_scatter(
            x=x_values,
            y=self.y_avg_values,
            name="Prix moyen",
        )

        fig.add_scatter(
            x=x_values,
            y=self.y_min_values,
            name="Prix minimum",
        )
        metrics = self.create_metrics()
        self.update_layout(fig)

        return fig, metrics

    def create_h_line(self, fig: go.Figure, value: float, label: str) -> None:
        """
        Create a horizontal line

        Args:
            fig (go.Figure): the figure
            value (float): the value of the line
            label (str): the label of the line
        """
        fig.add_hline(
            y=value,
            line_dash="dash",
            line_color="red",
            name=label,
            annotation={
                "text": f"{label}: {value}",
                "xref": "paper",
                "yref": "y",
                "x": 1.0,
                "y": value,
                "showarrow": False,
                "font": {
                    "family": "Courier New, monospace",
                    "size": 16,
                    "color": "white",
                },
            },
        )

    def create_metrics(self) -> None:
        """
        Add average values to the graph

        Args:
            fig (go.Figure): the figure
        """
        metrics: list[str] = []
        for average in (self.y_avg_values, self.y_min_values):
            average_value = np.mean(average)
            deviation = np.std(average)
            try:
                deviation_related_to_average = (deviation / average_value) * 100
            except ZeroDivisionError:
                deviation_related_to_average = 0
            deviation_related_to_average = round(deviation_related_to_average, 2)

            if len(average) > 1:
                increase_rate = (average[-1] - average[0]) / average[0] * 100
            else:
                increase_rate = 0

            metrics.append(
                f"Valeur moyenne: {round(average_value, 2)} - "
                f"Ecart-type: {round(deviation, 2)} - "
                f"Ecart-type relatif à la moyenne: {deviation_related_to_average} % - "
                f"Taux de croissance: {round(increase_rate, 2)} %"
            )
        return metrics

    def update_layout(self, fig: go.Figure) -> None:
        """
        Update the layout of the graph

        Args:
            fig (go.Figure): the figure
        """
        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(22,24,51,0)",
            paper_bgcolor="rgba(22,24,51,0)",
            title=f"<b>{self.title}</b>",
        )
        fig.update_yaxes(title_text=self.y_title)
        fig.update_xaxes(title_text=self.x_title)
