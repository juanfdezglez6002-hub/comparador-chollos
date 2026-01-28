import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# 1. AQUÍ AÑADES TUS PRODUCTOS Y TUS CATEGORÍAS
PRODUCTOS = [
    {"asin": "B08H75RTZ8", "nombre": "PS5 Spiderman", "cat": "Gaming", "comp": 549},
    {"asin": "B09G96TFFG", "nombre": "iPhone 13", "cat": "Electrónica", "comp": 720},
    {"asin": "B07PMLGP77", "nombre": "Cápsulas Café", "cat": "Comida", "comp": 32},
]

ID_AFILIADO = "chukufluku01-21"

def obtener_precio(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Buscamos el precio en el código de la página
        precio_str = soup.find("span", {"class": "a-price-whole"}).text.replace(',', '').replace('.', '')
        return float(precio_str)
    except:
        return None

# Lógica de comparación
resultados = []
for p in PRODUCTOS:
    precio_amz = obtener_precio(p['asin'])
    if precio_amz and precio_amz < p['comp']:
        ahorro = int((1 - (precio_amz / p['comp'])) * 100)
        resultados.append({
            "nombre": p['nombre'],
            "categoria": p['cat'],
            "precio_amazon": precio_amz,
            "precio_competencia": p['comp'],
            "ahorro_porcentaje": ahorro,
            "url_afiliado": f"https://www.amazon.es/dp/{p['asin']}/?tag={ID_AFILIADO}",
            "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL250_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
        })

# Guardar en el almacén data.json
with open('data.json', 'w') as f:
    json.dump({"last_updated": datetime.now().strftime("%Y-%m-%d %H:%M"), "productos": resultados}, f)
