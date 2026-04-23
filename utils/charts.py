import plotly.express as px
import plotly.graph_objects as go


def line_chart(df, x, y, title):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=title,
        template="plotly_dark"
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def bar_chart(df, x, y, title, color=None):
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        title=title,
        template="plotly_dark"
    )
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    return fig


def gauge_chart(value, title, min_value=0, max_value=100):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title},
        gauge={
            "axis": {"range": [min_value, max_value]},
            "bar": {"thickness": 0.3}
        }
    ))
    fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=50, b=20))
    return fig