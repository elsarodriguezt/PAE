import json
import pandas as pd
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

#mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

#empresa = yf.Ticker(mensaje) 
def main():
    mensaje = input("Escriu les inicials de una empresa: ").strip().lower()
    empresa = yf.Ticker(mensaje) 
    kpi = prof(empresa)

    # Imprimimos la lista de tuplas
    print(kpi)

def prof(empresa):
    cash = empresa.get_cash_flow()
    capex = cash.loc["CapitalExpenditure"]
    ebitda = empresa.financials.loc["EBITDA"]

    # Cogemos las fechas
    fechas_capex = capex.index.to_list()

    # Creamos una lista para almacenar los KPIs
    kpis = []

    for i in range(3):
        # Calculamos el KPI
        kpi = empresa.info['enterpriseValue']/ebitda.values[i] - capex.values[i]

        # Añadimos el KPI a la lista
        kpis.append((fechas_capex[i], kpi))

    return kpis

main()



