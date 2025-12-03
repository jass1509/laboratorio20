def generar_matriz_espiral(N):
    """
    Genera e imprime una matriz N x N con números de 1 a N^2 ordenados en espiral.

    Args:
        N (int): El tamaño de la matriz (N filas y N columnas). Debe ser >= 3.
    """
    # 1. Validación de la entrada
    if not isinstance(N, int) or N < 3:
        print(f"Error: N debe ser un número entero mayor o igual a 3. Se recibió: {N}")
        return

    # 2. Inicialización de la matriz y variables
    # Crear una matriz N x N inicializada con ceros
    matriz = [[0] * N for _ in range(N)]
    
    # Punteros para los límites de la capa exterior actual
    # top: fila superior, bottom: fila inferior
    # left: columna izquierda, right: columna derecha
    top, bottom = 0, N - 1
    left, right = 0, N - 1
    
    # El número que se va a colocar en la matriz, empezando en 1
    contador = 1
    
    # El valor máximo que debe alcanzar el contador (N^2)
    N_cuadrado = N * N

    # 3. Llenado iterativo en espiral
    while contador <= N_cuadrado:
        
        # === Paso 1: Moverse de izquierda a derecha (fila superior) ===
        if top <= bottom:
            for j in range(left, right + 1):
                matriz[top][j] = contador
                contador += 1
            top += 1 # La fila superior ya está llena, se mueve hacia abajo

        # Si ya hemos llenado todos los números, rompemos
        if contador > N_cuadrado:
            break
            
        # === Paso 2: Moverse de arriba a abajo (columna derecha) ===
        if left <= right:
            for i in range(top, bottom + 1):
                matriz[i][right] = contador
                contador += 1
            right -= 1 # La columna derecha ya está llena, se mueve hacia la izquierda

        # Si ya hemos llenado todos los números, rompemos
        if contador > N_cuadrado:
            break
            
        # === Paso 3: Moverse de derecha a izquierda (fila inferior) ===
        # Se requiere verificar de nuevo si top <= bottom en caso de que N sea impar y 
        # la condición de la espiral anterior haya llenado la última fila/columna restante.
        if top <= bottom:
            # Usamos 'reversed' o un rango decreciente
            for j in range(right, left - 1, -1):
                matriz[bottom][j] = contador
                contador += 1
            bottom -= 1 # La fila inferior ya está llena, se mueve hacia arriba

        # Si ya hemos llenado todos los números, rompemos
        if contador > N_cuadrado:
            break

        # === Paso 4: Moverse de abajo a arriba (columna izquierda) ===
        if left <= right:
            # Usamos 'reversed' o un rango decreciente
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = contador
                contador += 1
            left += 1 # La columna izquierda ya está llena, se mueve hacia la derecha

    # 4. Impresión del resultado
    imprimir_matriz(matriz, N)


def imprimir_matriz(matriz, N):
    """
    Función auxiliar para imprimir la matriz de forma legible.
    """
    # Determinar el ancho máximo para la alineación (N^2 puede ser de varios dígitos)
    max_ancho = len(str(N * N))
    
    print(f"\nMatriz Espiral {N}x{N}:")
    for fila in matriz:
        # Usamos f-string con formato >{max_ancho} para alinear a la derecha
        print(" ".join(f"{num:>{max_ancho}}" for num in fila))


# --- Ejemplos de uso ---
# Ejemplo del problema (N=4)
generar_matriz_espiral(4)

# Otro ejemplo (N=5)
generar_matriz_espiral(5)

# Ejemplo de validación de entrada (N<3)
generar_matriz_espiral(2)