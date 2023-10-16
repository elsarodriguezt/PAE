import json
import pandas as pd
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

empresa = yf.Ticker(mensaje) 

cash = empresa.get_cash_flow()
print(cash.loc)
capex = cash.loc["Capital Expenditure"][0]

print(capex.to_string())



