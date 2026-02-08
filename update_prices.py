import json

# Tus recomendaciones organizadas por categorías
PRODUCTOS = [
    {"asin": "B08H7SRTZ8", "cat": "Gaming", "nombre": "Console PlayStation 5 Slim", "precio": "499,00€", "resumen": "La mejor consola para exclusivos."},
    {"asin": "B0071Z164V", "cat": "Alimentación", "nombre": "Coca-Cola Zero (Pack 12)", "precio": "10,80€", "resumen": "Stock perfecto para casa."},
    {"asin": "B09G96TTFG", "cat": "Electrónica", "nombre": "Apple iPhone 13 (128 GB)", "precio": "619,00€", "resumen": "Gran rendimiento y cámara."},
    {"asin": "B09G96TTFG", "cat": "Electrónica", "nombre": "AirPods Pro 2", "precio": "239,00€", "resumen": "Cancelación de ruido líder."}
]

ID_AFILIADO = "tu-tag-21"

def build():
    # Agrupar automáticamente por categoría
    categorias_dict = {}
    for p in PRODUCTOS:
        cat = p["cat"]
        if cat not in categorias_dict:
            categorias_dict[cat] = []
        
        categorias_dict[cat].append({
            "nombre": p["nombre"],
            "precio": p["precio"],
            "resumen": p["resumen"],
            "url": f"https://www.amazon.es/dp/{p['asin']}?tag={ID_AFILIADO}",
            "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL400_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
        })
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(categorias_dict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    build()
