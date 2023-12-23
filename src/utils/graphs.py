import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.models.graph_model import GraphModel


def create_bar_graph(
    title: str, description: str, x_title: str, y_title: str, x_values: dict
) -> px.line:
    """
    Create a daily graph

    Args:
        title (str): the title of the graph
        description (str): the description of the graph
        x_title (str): the x title of the graph
        y_title (str): the y title of the graph
        x_values (dict): the x values of the graph

    Returns:
        px.line: the daily graph
    """
    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=list(x_values.values()),
        y_values=list(x_values.keys()),
    )
    average_value = round(np.mean(list(x_values.values())), 2)
    deviation_value = round(np.std(list(x_values.values())), 2)

    dataframe = pd.DataFrame(
        data={
            "Site": list(x_values.keys()),
            "Valeurs": list(x_values.values()),
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

    fig.add_hline(
        y=average_value,
        line_dash="dash",
        line_color="white",
        name="Moyenne",
        annotation=dict(
            text=f"Moyenne: {average_value}",
            xref="paper",
            yref="y",
            x=1.0,
            y=average_value,
            showarrow=False,
            font=dict(family="Courier New, monospace", size=16, color="white"),
        ),
    )
    fig.add_hrect(
        y0=average_value - deviation_value,
        y1=average_value + deviation_value,
        line_width=0,
        fillcolor="rgba(255, 255, 255, 0.2)",
        opacity=0.2,
    )

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    fig.update_traces(
        marker_color=[
            "#00C58E" if value < average_value else "#FA4B3A"
            for value in list(x_values.values())
        ],
    )
    fig.update_xaxes(title_text="Sites de ventes")
    fig.update_yaxes(title_text="Valeurs estimées (million)")

    return fig


def create_line_graph(
    title: str,
    description: str,
    x_title: str,
    y_title: str,
    x_values: list,
    y_values: list,
    y_max_values: list,
    y_min_values: list,
) -> px.line:
    """
    Create a line graph

    Args:
        title (str): the title of the graph
        description (str): the description of the graph
        x_title (str): the x title of the graph
        y_title (str): the y title of the graph
        x_values (list): list of x values
        y_values (list): list of y values
        y_max_values (list): list of y max values
        y_min_values (list): list of y min values

    Returns:
        px.line: the line graph
    """
    x_values = [
        datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z") for date in x_values
    ]

    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=x_values,
        y_values=y_values,
    )
    dataframe = pd.DataFrame(
        data={
            "Date UTC": x_values,
            "Moyenne": y_values,
            "Max": y_max_values,
            "Min": y_min_values,
        }
    )
    fig = px.line(
        dataframe,
        x="Date UTC",
        y=["Moyenne", "Max", "Min"],
        title=f"<b>{model.title}</b>",
    )

    average_value = round(np.mean(y_values), 2)
    min_value = round(min(y_min_values), 2)
    max_value = round(max(y_max_values), 2)

    create_h_line(fig, average_value, label="Moyenne")
    create_h_line(fig, min_value, label="Minimum")
    create_h_line(fig, max_value, label="Maximum")

    fig.update_yaxes(title_text="Valeurs estimées (million)")
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig


def create_gauche_graph(yesterday_value: float, today_value: float) -> go.Figure:
    """
    Create a gauche graph

    Args:
        yesterday_value (float): the yesterday value
        today_value (float): the today value

    Returns:
        go.Figure: the gauche graph
    """

    try:
        value = (today_value - yesterday_value) / yesterday_value * 100
    except ZeroDivisionError:
        value = 0

    value = round(value, 2)
    max_value = max(today_value, yesterday_value)

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=today_value,
            title={
                "text": f"<b>+{value} %/jour</b>"
                if value > 0
                else f"<b>{value} %/jour</b>"
            },
            domain={"x": [0, 1], "y": [0, 1]},
            delta={"reference": yesterday_value},
            gauge={
                "axis": {
                    "range": [None, max_value],
                    "tickwidth": 1,
                    "tickcolor": "white",
                },
                "bar": {"color": "lightgray"},
                "steps": [{"range": [0, yesterday_value], "color": "gray"}],
            },
        ),
    )
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(t=0, b=0, r=5, l=5, pad=0),
        height=250,
        width=250,
    )

    return fig


def create_graphs(day_kamas_dict: dict, yesterday_kamas_dict: dict) -> tuple:
    """
    return all the graph for the server

    Args:
        day_kamas_dict (dict): dict of the day kamas value
        yesterday_kamas_dict (dict): dict of the yesterday kamas value

    Returns:
        tuple: all the graph for the server
    """
    best_price = min(list(day_kamas_dict["kamas_dict"].values()))
    deviation_value = round(np.std(list(day_kamas_dict["kamas_dict"].values())), 2)

    fig_day = create_bar_graph(
        "Valeur journalière du million de kamas",
        "",
        "Jour",
        "Valeur estimée journalière",
        day_kamas_dict["kamas_dict"],
    )

    if yesterday_kamas_dict:
        fig_gauge = create_gauche_graph(
            yesterday_kamas_dict["average"], day_kamas_dict["average"]
        )
    else:
        fig_gauge = create_gauche_graph(
            day_kamas_dict["average"], day_kamas_dict["average"]
        )

    return fig_day, fig_gauge, best_price, deviation_value


def create_h_line(fig: go.Figure, value: float, label: str) -> None:
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
        line_color="white",
        name=label,
        annotation=dict(
            text=f"{label}: {value}",
            xref="paper",
            yref="y",
            x=1.0,
            y=value,
            showarrow=False,
            font=dict(family="Courier New, monospace", size=16, color="white"),
        ),
    )
