
from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

df = pd.DataFrame({
    "Date": pd.date_range(start="2022-01-01", periods=100),
    "Open": np.random.rand(100) * 1000,
    "High": np.random.rand(100) * 1000,
    "Low": np.random.rand(100) * 1000,
    "Close": np.random.rand(100) * 1000,
    "SMA20": np.random.rand(100) * 1000,
    "EMA20": np.random.rand(100) * 1000,
    "MACD": np.random.rand(100),
    "MACD_signal": np.random.rand(100),
    "RSI": np.random.rand(100) * 100,
    "Predicted_Close": np.random.rand(100) * 1000,
})

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Tablero de Trading Interactivo - Simulado"),
    dcc.Graph(figure={
        "data": [go.Scatter(x=df["Date"], y=df["Close"], mode="lines", name="Close")],
        "layout": go.Layout(title="Precio Simulado", xaxis={"title": "Fecha"}, yaxis={"title": "Precio"})
    })
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
