import yfinance as yf
import pandas as pd
import datetime

mensaje = input("Escriu les inicials de una empresa: ")

empresa = yf.Ticker(mensaje)  

historial = empresa.history(start = "2018-09-05", end= "2023-09-05")

# Calcula el promedio de la columna 'Close' por mes
average_df = historial['Close'].resample('M').mean()

print(average_df.to_string())
