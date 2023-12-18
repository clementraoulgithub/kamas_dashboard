import numpy as np
import pandas as pd
from src.models.graph_model import GraphModel
import plotly.express as px
import plotly.graph_objects as go

fr_months = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre",
]


def create_daily_graph(
    title: str, description: str, x_title: str, y_title: str, x_values: dict
) -> px.line:
    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=list(x_values.values()),
        y_values=list(x_values.keys()),
    )

    average_value = round(np.mean(list(x_values.values())), 2)
    fig = px.bar(
        x=list(x_values.keys()),
        y=list(x_values.values()),
        title=model.title,
        color=["< moy" if value < average_value else "> moy" for value in list(x_values.values())],
    )
    fig.add_hline(
        y=average_value,
        line_dash="dash",
        annotation_text=f"Moyenne = {average_value}€",
        annotation_position="top left",
        line_color="red",
    )
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    fig.update_xaxes(title_text="Site de vente")
    fig.update_yaxes(title_text="Valeur estimée")

    return fig


def create_graph(
    title: str,
    description: str,
    x_title: str,
    y_title: str,
    x_values: list,
    y_values: list,
    y_max_values: list,
    y_min_values: list,
) -> px.line:
    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=x_values,
        y_values=y_values,
    )
    dataframe = pd.DataFrame(
        data={"Date": x_values, "Moyenne": y_values, "Max": y_max_values, "Min": y_min_values}
    )
    fig = px.line(
        dataframe,
        x="Date",
        y=["Moyenne", "Max", "Min"],
        title=model.title,
    )
    fig.update_yaxes(title_text="Valeurs estimées")
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    return fig


def create_gauche_graph(yesterday_value: float, today_value: float):
    value = (today_value - yesterday_value) / yesterday_value * 100
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": "Variation (%)"},
            delta={"reference": yesterday_value},
        ),
    )
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        height=200,
        width=200,
    )

    return fig
