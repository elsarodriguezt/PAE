import json
import pandas as pd
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

empresa = yf.Ticker(mensaje) 

def prof(empresa):
    cash = empresa.get_cash_flow()
    capex = cash.iloc[-1]['CapitalExpenditure']
    print( cash.loc["Capital Expenditure"].to_numpy().take(0))
    print(capex.to_string())
    #kpi = empresa.info['enterpriseValue']/empresa.financials.loc["EBITDA"].to_numpy().take(0) - cash.loc["Capital Expenditure"].to_numpy().take(0)
    return kpi

kpi = prof(empresa)
#print(kpi.to_string())

"""""
def prof(empresa):
    info = empresa.get_cash_flow()
    capex = info.loc["Capital Expenditure"]
    df = pd.DataFrame(info)
    kpi1 = df["enterpriseValue"] / df["EBITDA"][0] - capex
    kpi2 = df["enterpriseValue"] / df["EBITDA"][1] - capex
    kpi3 = df["enterpriseValue"] / df["EBITDA"][2] - capex
    return kpi1.to_string() + ", " + kpi2.to_string() + ", " + kpi3.to_string()

print(prof(empresa))
"""
