import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# 1. LISTA DE PRODUCTOS
PRODUCTOS = [
    {"asin": "B08H75RTZ8", "nombre": "PS5 Spiderman", "cat": "Gaming", "comp": 999},
    {"asin": "B09G96TFFG", "nombre": "iPhone 13", "cat": "Electronica", "comp": 999},
    {"asin": "B07PMLGP77", "nombre": "Capsulas Cafe", "cat": "Comida", "comp": 99}
]

ID_AFILIADO = "chukufluku01-21"

def obtener_precio(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        precio_entero = soup.find("span", {"class": "a-price-whole"})
        if precio_entero:
            clean_price = precio_entero.text.replace(',', '').replace('.', '').replace('\xa0', '').strip()
            return float(clean_price)
        return None
    except:
        return None

resultados = []
for p in PRODUCTOS:
    precio_amz = obtener_precio(p['asin'])
    if precio_amz:
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

# AQUÍ ESTABA EL FALLO, AHORA ESTÁ BIEN ALINEADO:
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M"), 
        "productos": resultados
    }, f, ensure_ascii=False, indent=4)
