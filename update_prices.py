import json
from datetime import datetime

# 1. Tu lista de productos a vigilar (puedes ampliarla)
PRODUCTOS_A_MONITORIZAR = [
    {"id": "B08N5WRWJ6", "nombre": "MacBook Air M1", "url": "..." },
    {"id": "B09G96T6CC", "nombre": "Sony WH-1000XM5", "url": "..." }
]

def comparar_y_filtrar():
    ganadores = []
    
    for item in PRODUCTOS_A_MONITORIZAR:
        # Aquí el robot consultaría las APIs reales
        precio_amz = obtener_precio_amazon(item["id"])
        precio_comp, tienda_comp = obtener_precio_competencia(item["nombre"])
        
        # EL FILTRO: Solo si Amazon es más barato
        if precio_amz < precio_comp:
            ahorro = round(((precio_comp - precio_amz) / precio_comp) * 100)
            
            ganadores.append({
                "id": item["id"],
                "nombre": item["nombre"],
                "precio_amazon": precio_amz,
                "precio_competencia": precio_comp,
                "tienda_competencia": tienda_comp,
                "ahorro_porcentaje": ahorro,
                "url_afiliado": f"https://www.amazon.es/dp/{item['id']}?tag=TU_TAG_AFILIADO",
                "imagen": "url_obtenida_por_api"
            })
    
    # 2. Crear el objeto final con la fecha de hoy
    resultado = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "productos": ganadores
    }
    
    # 3. Guardar en el archivo data.json que usará tu web
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

def obtener_precio_amazon(asin):
    # Aquí iría la llamada a la PA-API de Amazon
    return 929.00  # Ejemplo

def obtener_precio_competencia(nombre):
    # Aquí iría la búsqueda en Google Shopping u otras tiendas
    return 1020.00, "MediaMarkt" # Ejemplo

if __name__ == "__main__":
    comparar_y_filtrar()
