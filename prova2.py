"""import json
import pandas as pd
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

empresa = yf.Ticker(mensaje) 

cash = empresa.get_cash_flow()
capex = cash.loc["CapitalExpenditure"]
print(capex)


#financials.loc["EBITDA"].to_string()
#capex = cash.loc["Capital Expenditure"][0]

#print(capex.to_string()) """

import json
import pandas as pd
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

empresa = yf.Ticker(mensaje)

cash = empresa.get_cash_flow()
capex = cash.loc["CapitalExpenditure"]
ebitda = empresa.financials.loc["EBITDA"]

#print(f"capex: {capex}")
#print(f"capex0: {capex.values[0]}")
#print(f"ebitda: {ebitda}")
#print(f"ebitda0: {ebitda.values[0]}")
#print(f"ev: {empresa.info['enterpriseValue']}")

kpi = kpi = empresa.info['enterpriseValue']/ebitda.values[0] - capex.values[0]
fechas_capex = capex.index.to_list()

for i in range(3):
    # Calculamos el KPI
    kpi = empresa.info['enterpriseValue']/ebitda.values[i] - capex.values[i]
    kpi1 = fechas_capex[i] + kpi

    # Imprimimos las fechas y el KPI
    print(kpi1)


#print(f"{fechas_capex[0]} kpi: {kpi}")




