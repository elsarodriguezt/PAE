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

countries = ['DK']
             #'DE', 'AT', 'LU', 'FR', 'BE', 'ES', 'CH', 'PT', 'NL', 'SE', 'IE', 'DK', 'NO', 'FI', 'CZ', 'HU', 'PL', 'GR','RO','HR']
# get symbol list based on market
output = reduce(r, countries, [])

print(len(output))

def buildFinal(a, ticker):
    data = yf.Ticker(ticker)
    industries = ["Auto Parts", "Auto Manufacturers", "Telecom Services", "Communication Equipment", "Software - Infrastructure", "Information Technology Services", "Drug Manufacturers - Specialty & Generic", "Biotechnology", "Drug Manufacturers - General"]
    try:
        if(data.info["industry"] in industries):
            a.append({"symbol": data.info['symbol'], "name": data.info["shortName"], "country": data.info["country"], "sector": data.info["sector"], "industry": data.info["industry"],
                      "ev": str(data.info['enterpriseValue']), "employees" : str(data.info['fullTimeEmployees']), "stock price": average(data), "# of shares" : str(data.info['sharesOutstanding']), 
                      "revenue": data.financials.loc["Total Revenue"].to_string(), "ebitda": data.financials.loc["EBITDA"].to_string()})
    except:
        print(data.info)
    finally:
       return a

l = reduce(buildFinal, output, [])
f = open('dump.json', 'a')
f.write(json.dumps(l))




# if(data.info["sector"] == "Technology" or data.info["sector"] == "Healthcare" or data.info["industry"] == "Auto Parts" or data.info["industry"] == "Auto Manufacturers"):
#if(data.info["industry"]== "Auto Parts" or data.info["industry"] == "Auto Manufacturers" or data.info["industry"] == "Telecom Services" or data.info["industry"] == "Communication Equipment"
#or data.info["industry"] == "Software - Infrastructure" or data.info["industry"] == "Information Technology Services" or data.info["industry"] == "Drug Manufacturers - Specialty & Generic" 
#or data.info["industry"] == "Biotechnology" or data.info["industry"] == "Drug Manufacturers - General")


# get symbol list based on index
# symbol_list_spx = ss.get_symbol_list(index="SPX")

# show a list of available market
# market_list = ss.market_list

# show a list of available index
# index_list = ss.index_list
