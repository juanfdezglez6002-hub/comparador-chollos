import json
from datetime import datetime

# --- CONFIGURACIÓN MANUAL DE PRODUCTOS ---
# Aquí controlas tú el 100% de la información
PRODUCTOS = [
    {
        "asin": "B08H75RTZ8", 
        "nombre": "Consola PlayStation 5", 
        "cat": "Gaming", 
        "precio_real": 494.99, # Pon aquí el precio que ves en Amazon hoy
        "precio_comp": 549.99  # Pon aquí el precio anterior/competencia
    },
    {
        "asin": "B09G96TFFG", 
        "nombre": "Apple iPhone 13 (128 GB)", 
        "cat": "Electrónica", 
        "precio_real": 619.00, 
        "precio_comp": 729.00
    },
    {
        "asin": "B07PMLGP77", 
        "nombre": "Cápsulas Café L'Or x100", 
        "cat": "Comida", 
        "precio_real": 27.50, 
        "precio_comp": 35.50
    }
]

ID_AFILIADO = "chukufluku01-21"

resultados = []
for p in PRODUCTOS:
    # Cálculo matemático exacto del ahorro
    ahorro = int((1 - (p['precio_real'] / p['precio_comp'])) * 100)

    resultados.append({
        "nombre": p['nombre'],
        "categoria": p['cat'],
        "precio_amazon": p['precio_real'],
        "precio_competencia": p['precio_comp'],
        "ahorro_porcentaje": ahorro,
        "url_afiliado": f"https://www.amazon.es/dp/{p['asin']}/?tag={ID_AFILIADO}",
        # Imagen legal de Amazon (Explicación abajo)
        "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL400_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
    })

# Generar el JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "productos": resultados
    }, f, ensure_ascii=False, indent=4)

print("¡JSON actualizado manualmente con éxito!")
