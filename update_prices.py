import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

# --- TU LISTA DE PRODUCTOS ---
PRODUCTOS = [
    {"asin": "B08H75RTZ8", "nombre": "Consola PlayStation 5", "cat": "Gaming", "comp": 549.99},
    {"asin": "B09G96TFFG", "nombre": "Apple iPhone 13 (128 GB)", "cat": "Electrónica", "comp": 729.00},
    {"asin": "B07PMLGP77", "nombre": "Cápsulas Café L'Or", "cat": "Comida", "comp": 35.50}
]

ID_AFILIADO = "chukufluku01-21"

def obtener_precio_real(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    # Cabeceras que imitan a un navegador real (Chrome en Windows)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Intentar capturar el precio de varias formas (Amazon cambia las etiquetas a menudo)
        span_precio = soup.find("span", {"class": "a-price-whole"})
        span_decimal = soup.find("span", {"class": "a-price-fraction"})
        
        if span_precio:
            # Limpiamos el texto de puntos, comas y espacios raros
            entero = span_precio.text.replace('.', '').replace(',', '').strip()
            decimal = span_decimal.text.strip() if span_decimal else "00"
            return float(f"{entero}.{decimal}")
            
        return None
    except Exception as e:
        print(f"Error con ASIN {asin}: {e}")
        return None

resultados = []
for p in PRODUCTOS:
    print(f"Buscando precio real para: {p['nombre']}...")
    precio_amz = obtener_precio_real(p['asin'])
    
    # Si Amazon nos bloquea (precio_amz es None), usamos el precio de competencia 
    # pero pondremos un aviso para que sepas que falló la lectura real.
    if precio_amz is None:
        precio_final = p['comp'] # Usamos el de competencia para no inventar
        ahorro = 0
        tag_error = " (Ver precio en Amazon)"
    else:
        precio_final = precio_amz
        ahorro = int((1 - (precio_final / p['comp'])) * 100)
        tag_error = ""

    resultados.append({
        "nombre": p['nombre'] + tag_error,
        "categoria": p['cat'],
        "precio_amazon": precio_final,
        "precio_competencia": p['comp'],
        "ahorro_porcentaje": ahorro,
        "url_afiliado": f"https://www.amazon.es/dp/{p['asin']}/?tag={ID_AFILIADO}",
        "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL250_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
    })
    # Pausa de 2 segundos para que Amazon no nos banee por ir rápido
    time.sleep(2)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "productos": resultados
    }, f, ensure_ascii=False, indent=4)
