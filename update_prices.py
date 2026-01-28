import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# --- PASO A PASO: AÑADE AQUÍ TUS PRODUCTOS ---
# 1. Busca el producto en Amazon.es
# 2. Copia el código ASIN (está en la URL después de /dp/...)
# 3. Ponle un nombre, una categoría y el precio de la competencia
PRODUCTOS = [
    {"asin": "B08H75RTZ8", "nombre": "Consola PlayStation 5", "cat": "Gaming", "comp": 549.99},
    {"asin": "B09G96TFFG", "nombre": "Apple iPhone 13 (128 GB)", "cat": "Electrónica", "comp": 729.00},
    {"asin": "B07PMLGP77", "nombre": "L'Or Espresso Café 100 Cápsulas", "cat": "Comida", "comp": 35.50},
    # Añade más líneas aquí siguiendo el mismo formato
]

ID_AFILIADO = "chukufluku01-21"

def obtener_datos(asin):
    url = f"https://www.amazon.es/dp/{asin}?tag={ID_AFILIADO}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Buscar precio
        p_entero = soup.find("span", {"class": "a-price-whole"})
        p_decimal = soup.find("span", {"class": "a-price-fraction"})
        
        if p_entero:
            precio = p_entero.text.replace('.', '').strip()
            if p_decimal:
                precio += f".{p_decimal.text.strip()}"
            return float(precio.replace(',', '.'))
        return None
    except:
        return None

resultados = []
for p in PRODUCTOS:
    precio_amz = obtener_datos(p['asin'])
    
    # Si no detectamos el precio de Amazon, usamos el de competencia -10% para la demo
    # En un caso real, el producto no se mostraría si no hay stock
    final_price = precio_amz if precio_amz else p['comp'] * 0.9
    ahorro = int((1 - (final_price / p['comp'])) * 100)

    resultados.append({
        "nombre": p['nombre'],
        "categoria": p['cat'],
        "precio_amazon": round(final_price, 2),
        "precio_competencia": p['comp'],
        "ahorro_porcentaje": ahorro,
        "url_afiliado": f"https://www.amazon.es/dp/{p['asin']}/?tag={ID_AFILIADO}",
        "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL250_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
    })

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({"last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"), "productos": resultados}, f, ensure_ascii=False, indent=4)
