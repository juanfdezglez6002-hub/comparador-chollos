import json

# LISTA DE PRODUCTOS (Solo lo que quieres que se vea)
PRODUCTOS = [
    {
        "asin": "B0071Z164V",
        "nombre": "Coca-Cola Zero Azúcar (Pack 12)",
        "cat": "Alimentación",
        "precio": "10,80€",
        "resumen": "La opción sin cafeína perfecta para casa."
    },
    {
        "asin": "B08H7SRTZ8",
        "nombre": "Console PlayStation 5 Slim",
        "cat": "Gaming",
        "precio": "499,00€",
        "resumen": "La versión más compacta con lector de discos."
    }
]

ID_AFILIADO = "tu-tag-21"

def build():
    lista_final = []
    for p in PRODUCTOS:
        lista_final.append({
            "nombre": p["nombre"],
            "categoria": p["cat"],
            "precio": p["precio"],
            "resumen": p["resumen"],
            "url": f"https://www.amazon.es/dp/{p['asin']}?tag={ID_AFILIADO}",
            "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL400_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
        })
    
    data = {
        "last_updated": "Hoy",
        "categorias": sorted(list(set(p["cat"] for p in PRODUCTOS))),
        "productos": lista_final
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    build()
