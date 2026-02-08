import json
from datetime import datetime

# CONFIGURACIÓN MANUAL DE PRODUCTOS
# Aquí añades todo lo que quieras recomendar
PRODUCTOS = [
    # ALIMENTACIÓN
    {"asin": "B0071Z164V", "nombre": "Coca-Cola Zero Azúcar (Pack 12)", "cat": "Alimentación", "precio": "10,80€", "resumen": "Pack ahorro ideal para casa."},
    # GAMING
    {"asin": "B08H7SRTZ8", "nombre": "Consola PlayStation 5 Slim", "cat": "Gaming", "precio": "494,99€", "resumen": "La mejor experiencia de juego actual."},
    # ELECTRÓNICA
    {"asin": "B09G96TTFG", "nombre": "Apple iPhone 13 (128 GB)", "cat": "Electrónica", "precio": "619,00€", "resumen": "Potencia y cámara en un diseño icónico."},
    # HOGAR
    {"asin": "B08C1KN5CH", "nombre": "Freidora de Aire COSORI 5.5L", "cat": "Hogar", "precio": "109,00€", "resumen": "Cocina sano y rápido todos los días."},
    # LIBROS
    {"asin": "8408270481", "nombre": "Hábitos Atómicos - James Clear", "cat": "Libros", "precio": "18,90€", "resumen": "El libro nº1 para cambiar tus rutinas."},
    # DEPORTE
    {"asin": "B07P8929S3", "nombre": "Mancuernas Ajustables (Par)", "cat": "Deporte", "precio": "85,00€", "resumen": "Entrena en casa con equipo profesional."},
    # JUGUETES
    {"asin": "B08W9N669L", "nombre": "LEGO Star Wars Halcón Milenario", "cat": "Juguetes", "precio": "145,00€", "resumen": "Pieza de coleccionista imprescindible."},
    # BELLEZA
    {"asin": "B06Y5P4Z5M", "nombre": "Desodorante en crema LANCASTER", "cat": "Belleza", "precio": "7,08€", "resumen": "Piel radiante y protegida diariamente."},
    # ROPA
    {"asin": "B01N266I09", "nombre": "Sudadera Levi's con Capucha", "cat": "Ropa", "precio": "45,00€", "resumen": "Clásico cómodo que nunca pasa de moda."}
]

ID_AFILIADO = "chukukfuku01-21"

def generar_data_json():
    lista_final = []
    
    for p in PRODUCTOS:
        # CONSTRUCCIÓN DEL ENLACE DE IMAGEN LEGAL (MÉTODO 1)
        # Este enlace llama a la imagen oficial de Amazon sin descargarla
        url_imagen_amazon = f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL400_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
        
        # CONSTRUCCIÓN DEL ENLACE DE AFILIADO
        url_final = f"https://www.amazon.es/dp/{p['asin']}?tag={ID_AFILIADO}"
        
        lista_final.append({
            "nombre": p["nombre"],
            "categoria": p["categoria"],
            "precio": p["precio"],
            "resumen": p["resumen"],
            "url": url_final,
            "imagen": url_imagen_amazon
        })
    
    # 3. GUARDAR EL ARCHIVO JSON
    data_estructurada = {
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "productos": lista_final
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data_estructurada, f, indent=4, ensure_ascii=False)
    
    print(f"✅ data.json generado con {len(lista_final)} productos.")

if __name__ == "__main__":
    generar_data_json()
