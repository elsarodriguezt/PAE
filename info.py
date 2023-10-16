import yfinance as yf
import pandas as pd
import json

mensaje = input("Escriu les inicials de una empresa: ")

empresa = yf.Ticker(mensaje)  

historial = empresa.history(start = "2023-09-01", end= "2023-09-30")
print(historial)

""""
sector = empresa.info['sector']
indus = empresa.info['industry']
ev = str(empresa.info['enterpriseValue'])

print(sector + indus + ev) """

""" info = empresa.info['country']

print("INFO: ")
print(info ) """

#print(ebitda)
#ebitda_dict = ebitda.to_dict()

#with open("ebitda.json", "w") as json_file:
    #json.dump(ebitda_dict, json_file)

    