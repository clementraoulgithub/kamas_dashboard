import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.models.graph_model import GraphModel


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

    dataframe = pd.DataFrame(
        data={
            "Sites": list(x_values.keys()),
            "Valeurs": list(x_values.values()),
            "Moyenne": average_value,
        }
    )

    fig = px.bar(dataframe, x="Sites", y="Valeurs", title=model.title, text="Valeurs")
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

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    fig.update_traces(
        marker_color=[
            "#00C58E" if value < average_value else "#FA4B3A" for value in list(x_values.values())
        ]
    )
    fig.update_xaxes(title_text="Sites de ventes")
    fig.update_yaxes(title_text="Valeurs estimées")

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
    value = round(value, 2)
    max_value = max(today_value, yesterday_value)
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=today_value,
            title={"text": f"{value} %"},
            domain={"x": [0, 1], "y": [0, 1]},
            delta={"reference": yesterday_value},
            gauge={
                "axis": {"range": [None, max_value], "tickwidth": 1, "tickcolor": "white"},
                "bar": {"color": "#00C58E" if max_value == yesterday_value else "#FA4B3A"},
            },
        ),
    )
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(t=0, b=0, r=0, l=0, pad=0),
        height=250,
        width=250,
    )

    return fig
