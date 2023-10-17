import yfinance as yf
import pandas as pd
import json

mensaje = input("Escriu les inicials de una empresa: ").strip().lower()

empresa = yf.Ticker(mensaje) 


pais = empresa.info['country']
sector = empresa.info['sector']
industry = empresa.info['industry']
precio_accion = empresa.info['bid']
numero_acciones = empresa.info['sharesOutstanding']
ventas = empresa.info['totalRevenue']
ev = empresa.info['enterpriseValue']
ebitda = empresa.info['ebitda']
num_trabajadores = empresa.info['fullTimeEmployees']

datos = {
        "Compañia": mensaje,
        "Pais": pais,
        "Sector": sector ,
        "Industry": industry,
        "Precio acción": precio_accion,
        "Num. acciones": numero_acciones,
        "Ventas": ventas,
        "EV": ev,
        "Ebitda": ebitda,
        "Num. trabajadores": num_trabajadores
  }
print(datos)