

def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        print("Modo inválido.")
        return None
    
    # Copia para no modificar el original
    datos = lista[:]
    
    if modo == "minmax":
        minimo = min(datos)
        maximo = max(datos)
        rango = maximo - minimo
        if rango == 0:
            return [0 for _ in datos]  # evitar división por cero
        return [(x - minimo) / rango for x in datos]

    elif modo == "zscore":
        media = sum(datos) / len(datos)
        varianza = sum((x - media) ** 2 for x in datos) / len(datos)
        desviacion = varianza ** 0.5
        if desviacion == 0:
            return [0 for _ in datos]
        return [(x - media) / desviacion for x in datos]

    elif modo == "unit":
        norma = sum(x**2 for x in datos) ** 0.5
        if norma == 0:
            return [0 for _ in datos]
        return [x / norma for x in datos]


# Ejemplo dado
valores = [10, 20, 30]

print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))

print("Original:", valores)
