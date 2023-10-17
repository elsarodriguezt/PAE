import json
from functools import reduce
from stocksymbol import StockSymbol
import yfinance as yf

def average(empresa): #per fer average mensual del preu del stock
    #empresa = yf.Ticker(simbol)  
    historial = empresa.history(start = "2018-09-05", end= "2023-09-05")
    # Calcula el promedio de la columna 'Close' por mes
    average_df = historial['Close'].resample('M').mean()
    return average_df.to_string()

def profitability(empresa):
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

        # Convertimos el timestamp a una cadena de formato ISO 8601
        fecha_capex_str = fechas_capex[i].isoformat()

        # Añadimos el KPI a la lista
        kpis.append({"fecha": fecha_capex_str, "kpi": kpi})

    return kpis


def tickermap(item):
    return item["symbol"]

def r(a, country):
    try:
        symbol_list = ss.get_symbol_list(market=country)
        return a+list(map(tickermap, symbol_list))
    except:
        return a

api_key = '720a7eb1-c7e4-4db0-ac30-75711eec9686'
ss = StockSymbol(api_key)

countries = ['GB', 'DE', 'AT', 'IT', 'LU', 'FR', 'BE', 'ES', 'CH', 'PT', 'NL', 'SE', 'IE', 'DK', 'NO', 'FI', 'CZ', 'HU', 'PL', 'GR','RO','HR', 'SI', 'SK', 'EE', 'RS']
            
output = reduce(r, countries, [])

print(len(output))

def buildFinal(a, ticker):
    data = yf.Ticker(ticker)
    industries = ["Auto Parts", "Auto Manufacturers", "Telecom Services", "Communication Equipment", "Software - Infrastructure", "Information Technology Services", "Drug Manufacturers - Specialty & Generic", "Biotechnology", "Drug Manufacturers - General"]
    try:
        if(data.info["industry"] in industries):
            a.append({"symbol": data.info['symbol'], "name": data.info["shortName"], "country": data.info["country"], "sector": data.info["sector"], "industry": data.info["industry"],
                      "ev": str(data.info['enterpriseValue']), "employees" : str(data.info['fullTimeEmployees']), "stock price": average(data), "# of shares" : str(data.info['sharesOutstanding']), 
                      "revenue": data.financials.loc["Total Revenue"].to_string(), "ebitda": data.financials.loc["EBITDA"].to_string(), "profitability": profitability(data)})
    except:
        print(data.info)
    finally:
       return a

l = reduce(buildFinal, output, [])
f = open('dump.json', 'a')
f.write(json.dumps(l))



# get symbol list based on index
# symbol_list_spx = ss.get_symbol_list(index="SPX")

# show a list of available market
# market_list = ss.market_list

# show a list of available index
# index_list = ss.index_list
