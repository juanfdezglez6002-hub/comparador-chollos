import json
from datetime import datetime

# CONFIGURACIÓN MANUAL DE PRODUCTOS
# Aquí añades todo lo que quieras recomendar
PRODUCTOS = [
    # ALIMENTACIÓN
    {"asin": "B07B81842Y", "nombre": "Estrella Galicia Especial (Pack 24 latas de 33 cl)", "cat": "Alimentación", "precio_manual": "14,99€", "resumen": "Pack ahorro ideal para los amantes de la cerveza."},
    {"asin": "B0049U0DMC", "nombre": "Lavazza, Qualità Oro, Café en Grano Natural,Paquete de 1 kg", "cat": "Alimentación", "precio_manual": "29,79€", "resumen": "Un café con cuerpo e intenso con una buena relación calidad precio."},
    {"asin": "B013W8QZXM", "nombre": "NESCAFÉ Dolce Gusto Café con Leche - Cápsulas de Café, 90 Cápsulas", "cat": "Alimentación", "precio_manual": "24,75€", "resumen": "Un café en cápsulas de calidad con rapidez de preparación, pack duradero."},
    {"asin": "B00DPKUKPC", "nombre": "Coca Cola Sabor Original Pack de 24 Latas 330 ml", "cat": "Alimentación", "precio_manual": "15,79€", "resumen": "Tu refresco de Cola de  siempre a un buen precio y con el sabor de siempre."},
    {"asin": "B00UI1R6M6", "nombre": "NESTLÉ Caja Roja Bombones de Chocolate con leche", "cat": "Alimentación", "precio_manual": "5,95€", "resumen": " Deliciosos bombones con buena relación calidad-precio. Ideales para realizar un buen regalo."},
    {"asin": "B01LZIMTSC", "nombre": "Leche Entera Central Lechera Asturiana Pack 6 x 1L", "cat": "Alimentación", "precio_manual": "7,38€", "resumen": "Leche de buena calidad con gran sabor con un buen precio mereciendo la pena"},
    {"asin": "B01IU8MJ7K", "nombre": "Caldo Casero de Pollo 100% Natural GALLINA BLANCA", "cat": "Alimentación", "precio_manual": "6,99€", "resumen": "Caldo muy sabroso y rico en sabor. Buena relación calidad-precio ya que ofrece un pack de ahorro."},
    {"asin": "B00JBWHJ5C", "nombre": "Chicle Sin Azúcar PUR Gum con Xilitol, Vegano, Sin Aspartamo y Sin Gluten (Paquede de 1 unidad con 55 unidades", "cat": "Alimentación", "precio_manual": "4,49€", "resumen": "Chicles buenos y espectaculares en términos de calidad. Sin azúcar ni aditivos raros, no tienen edulcorantes dañinos."},
    {"asin": "B09XR5YFFM", "nombre": "Salsa Sriracha Mayo Go-Tan 215ml", "cat": "Alimentación", "precio_manual": "3,22€", "resumen": "Salsa con un punto perfecto de picante y sabor, ideal para acompañar tacos y sushi."},
    {"asin": "B0FLQC89LM", "nombre": "ColaCao Original, Cacao Soluble Natural sin Aditivos, Formato Ahorro XXL, 5,9 kg", "cat": "Alimentación", "precio_manual": "36,99€", "resumen": "Precio genial manteniendo la calidad característica de la marca con un sabor genial y maravilloso."},

    

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
