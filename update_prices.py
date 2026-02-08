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
    resultados = []
    
    for p in PRODUCTOS:
        # Usamos .get() por seguridad y p["precio_real"] que es como lo tienes arriba
        resultados.append({
            "nombre": p.get("nombre", "Producto sin nombre"),
            "categoria": p.get("cat", "General"),
            "precio": str(p.get("precio_real", "Consultar")), # Usamos precio_real
            "resumen": p.get("resumen", "Recomendado por su calidad-precio."),
            "url": f"https://www.amazon.es/dp/{p['asin']}?tag={ID_AFILIADO}",
            "imagen": f"https://ws-eu.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN={p['asin']}&Format=_SL400_&ID=AsinImage&MarketPlace=ES&ServiceVersion=20070822"
        })
    
    # Generar el JSON final
    data = {
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "productos": resultados
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"✅ JSON actualizado con {len(resultados)} productos.")

# ESTO DEBE IR FUERA DE LA FUNCIÓN (SIN ESPACIOS AL PRINCIPIO)
if __name__ == "__main__":
    generar_data_json()
