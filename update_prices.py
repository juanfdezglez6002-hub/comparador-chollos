import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

PRODUCTOS = [
    {"asin": "B08H75RTZ8", "nombre": "PS5 Spiderman", "cat": "Gaming", "comp": 549},
    {"asin": "B09G96TFFG", "nombre": "iPhone 13", "cat": "Electrónica", "comp": 720},
    {"asin": "B07PMLGP77", "nombre": "Cápsulas Café", "cat": "Comida", "comp": 32}
]

ID_AFILIADO = "chukufluku01-21"

def obtener_precio(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        precio_entero = soup.find("span", {"class": "a-price-whole"})
        if precio_entero:
            return precio_entero.text.replace(',', '').replace('.', '').replace('\xa0', '').strip()
        return None
    except:
        return None

resultados = []
for p in PRODUCTOS:
    precio_amz = obtener_precio(p['asin'])
    
    # Si Amazon nos bloquea, ponemos "Oferta" para que el producto no desaparezca
    final_price = f"{precio_amz}€" if precio_amz else "Ver precio"
    ahorro = int((1 - (float(precio_amz if precio_amz else 0) / p['comp'])) * 100) if precio_amz else "TOP"

    resultados.append({
        "nombre": p['nombre'],
        "categoria": p['cat'],
        "precio_amazon": final_price,
        "precio_competencia": f"{p['comp']}€",
        "ahorro": f"{ahorro}%",
        "url": f"https://www.amazon.es/dp/{p['asin']}/?tag={ID_AFILIADO}",
        "img": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL250_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
    })

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({"last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"), "productos": resultados}, f, ensure_ascii=False, indent=4)
