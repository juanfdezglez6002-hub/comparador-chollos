import json
from datetime import datetime

# CONFIGURACIÓN MANUAL DE PRODUCTOS
# Aquí añades todo lo que quieras recomendar
PRODUCTOS = [
    # ALIMENTACIÓN
    {"asin": "B07B81842Y", "nombre": "Estrella Galicia Especial (Pack 24 latas de 33 cl)", "cat": "Alimentación", "precio_manual": "14,99€", "resumen": "Pack ahorro ideal para los amantes de la cerveza."},
    # GAMING
    {"asin": "B08H7SRTZ8", "nombre": "Consola PlayStation 5 Slim", "cat": "Gaming", "precio_manual": "494,99€", "resumen": "La mejor experiencia de juego actual."},
    # ELECTRÓNICA
    {"asin": "B09G96TTFG", "nombre": "Apple iPhone 13 (128 GB)", "cat": "Electrónica", "precio_manual": "619,00€", "resumen": "Potencia y cámara en un diseño icónico."},
    # HOGAR
    {"asin": "B08C1KN5CH", "nombre": "Freidora de Aire COSORI 5.5L", "cat": "Hogar", "precio_manual": "109,00€", "resumen": "Cocina sano y rápido todos los días."},
    # LIBROS
    {"asin": "8408270481", "nombre": "Hábitos Atómicos - James Clear", "cat": "Libros", "precio_manual": "18,90€", "resumen": "El libro nº1 para cambiar tus rutinas."},
    # DEPORTE
    {"asin": "B07P8929S3", "nombre": "Mancuernas Ajustables (Par)", "cat": "Deporte", "precio_manual": "85,00€", "resumen": "Entrena en casa con equipo profesional."},
    # JUGUETES
    {"asin": "B08W9N669L", "nombre": "LEGO Star Wars Halcón Milenario", "cat": "Juguetes", "precio_manual": "145,00€", "resumen": "Pieza de coleccionista imprescindible."},
    # BELLEZA
    {"asin": "B06Y5P4Z5M", "nombre": "Desodorante en crema LANCASTER", "cat": "Belleza", "precio_manual": "7,08€", "resumen": "Piel radiante y protegida diariamente."},
    # ROPA
    {"asin": "B01N266I09", "nombre": "Sudadera Levi's con Capucha", "cat": "Ropa", "precio_manual": "45,00€", "resumen": "Clásico cómodo que nunca pasa de moda."}
]

ID_AFILIADO = "chukukfuku01-21"

def generar_data_json():
    resultados = []
    
    for p in PRODUCTOS:
        # 1. Definimos la variable limpia
        asin_limpio = str(p.get("asin", "")).strip()
        
        # 2. Construimos los datos para el HTML
        resultados.append({
            "nombre": p.get("nombre"),
            "categoria": p.get("cat"),
            "precio": p.get("precio_manual"),
            "resumen": p.get("resumen"),
            "url": f"https://www.amazon.es/dp/{asin_limpio}?tag={ID_AFILIADO}",
            "imagen": f"https://images.amazon.com/images/P/{asin_limpio}.01._SL400_.jpg"
        })
    
    # 3. Creamos el objeto final (AQUÍ ESTABA TU ERROR DE ESPACIOS)
    data = {
        "last_updated": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "productos": resultados
    }
    
    # 4. Escribimos el archivo
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Hecho. He metido {len(resultados)} productos con tus precios.")

if __name__ == "__main__":
    generar_data_json()
