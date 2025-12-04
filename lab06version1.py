import numpy as np

def normalizar_np(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        print("Modo inválido.")
        return None

    datos = np.array(lista, dtype=float)

    if modo == "minmax":
        minimo = datos.min()
        maximo = datos.max()
        rango = maximo - minimo
        if rango == 0:
            return np.zeros_like(datos)
        return (datos - minimo) / rango

    elif modo == "zscore":
        media = datos.mean()
        desviacion = datos.std()
        if desviacion == 0:
            return np.zeros_like(datos)
        return (datos - media) / desviacion

    elif modo == "unit":
        norma = np.linalg.norm(datos)
        if norma == 0:
            return np.zeros_like(datos)
        return datos / norma


# Ejemplo dado
valores = [10, 20, 30]

print(normalizar_np(valores, "minmax"))
print(normalizar_np(valores, "zscore"))
print(normalizar_np(valores, "unit"))

print("Original:", valores)
