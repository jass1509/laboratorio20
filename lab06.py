import math

def normalizar_py(lista, modo):
    """
    Normaliza una lista de números reales usando Python puro.

    Args:
        lista (list): La lista de números a normalizar.
        modo (str): El modo de normalización ('minmax', 'zscore', 'unit').

    Returns:
        list: La lista normalizada.
    """
    # 1. Validación del modo
    if modo not in ["minmax", "zscore", "unit"]:
        print(f"Error: Modo de normalización '{modo}' no válido.")
        return []

    # Se trabaja con una copia de la lista para no modificar la original
    datos = lista[:] 
    
    # Manejo de listas vacías
    if not datos:
        return []

    # -------------------
    # MODO MINMAX
    # -------------------
    if modo == "minmax":
        min_val = min(datos)
        max_val = max(datos)
        
        rango = max_val - min_val
        
        # Manejo de división por cero (si todos los valores son iguales)
        if rango == 0:
            return [0.0] * len(datos) # Retorna ceros si todos son iguales
        
        return [(x - min_val) / rango for x in datos]

    # -------------------
    # MODO ZSCORE
    # -------------------
    elif modo == "zscore":
        
        # Cálculo de la media
        media = sum(datos) / len(datos)
        
        # Cálculo de la varianza (suma de cuadrados de las diferencias)
        varianza = sum([(x - media)**2 for x in datos]) / len(datos)
        
        # Cálculo de la desviación estándar
        desv_est = math.sqrt(varianza)
        
        # Manejo de división por cero (si todos los valores son iguales)
        if desv_est == 0:
            return [0.0] * len(datos) # Retorna ceros si todos son iguales
        
        return [(x - media) / desv_est for x in datos]

    # -------------------
    # MODO UNIT (Vector Unitario)
    # -------------------
    elif modo == "unit":
        
        # Cálculo de la norma (magnitud o longitud del vector)
        # ||v|| = sqrt(x1^2 + x2^2 + ... + xn^2)
        norma = math.sqrt(sum([x**2 for x in datos]))
        
        # Manejo de división por cero (si la norma es cero, es un vector cero)
        if norma == 0:
            return [0.0] * len(datos) # Retorna un vector cero
        
        return [x / norma for x in datos]


# --- Pruebas con los datos proporcionados ---
datos = [10, 20, 30]

print("--- Versión Python Puro ---")
print(f"Datos Originales: {datos}")

# Prueba 1: MinMax
resultado_minmax = normalizar_py(datos, "minmax")
print(f"Modo 'minmax': {resultado_minmax}") 

# Prueba 2: ZScore
resultado_zscore = normalizar_py(datos, "zscore")
print(f"Modo 'zscore': {resultado_zscore}")

# Prueba 3: Unit
resultado_unit = normalizar_py(datos, "unit")
print(f"Modo 'unit': {resultado_unit}")

# Prueba de validación de modo
normalizar_py(datos, "otro")

# Prueba de manejo de división por cero
datos_cero = [5, 5, 5]
print(f"\nDivisión por cero (MinMax, ZScore): {normalizar_py(datos_cero, 'minmax')}")