"""
Created on Sat Mar 27 10:42:58 2025

@author: Cristhianne
"""

import pandas as pd
import numpy as np
from dash import Dash, dcc, html
import plotly.graph_objs as go

# Cargar datos simulados
df = pd.read_csv("dashboard_reliance_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

def plot_candlestick(df):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Velas"
    ))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA20'], mode='lines', name='SMA20'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['EMA20'], mode='lines', name='EMA20'))
    fig.update_layout(title="Precio con Velas Japonesas + SMA/EMA", xaxis_title="Fecha", yaxis_title="Precio")
    return fig

def plot_macd(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD'], mode='lines', name='MACD'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD_signal'], mode='lines', name='Señal'))
    fig.update_layout(title="MACD", xaxis_title="Fecha", yaxis_title="MACD")
    return fig

def plot_rsi(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], mode='lines', name='RSI'))
    fig.update_layout(title="RSI", xaxis_title="Fecha", yaxis=dict(range=[0, 100]))
    return fig

def plot_prediction(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Close"], mode="lines", name="Real"))
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Predicted_Close"], mode="lines", name="Predicción LSTM (Simulada)"))
    fig.update_layout(title="Predicción de Precios con LSTM (Simulada)", xaxis_title="Fecha", yaxis_title="Precio")
    return fig

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Tablero de Trading Interactivo - Completo"),
    dcc.Graph(figure=plot_candlestick(df)),
    dcc.Graph(figure=plot_macd(df)),
    dcc.Graph(figure=plot_rsi(df)),
    dcc.Graph(figure=plot_prediction(df)),
])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
