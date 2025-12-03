def generar_matriz_espiral(N):
   
    # validacoin
    if not isinstance(N, int) or N < 3:
        print(f"Error: N debe ser un número entero mayor o igual a 3. Se recibió: {N}")
        return

    
    matriz = [[0] * N for _ in range(N)]
    
    # dimensiones de matrix
    top, bottom = 0, N - 1
    left, right = 0, N - 1
    
    
    contador = 1
    
    # valor amximo del contador
    N_cuadrado = N * N

   
    while contador <= N_cuadrado:
        
        if top <= bottom:
            for j in range(left, right + 1):
                matriz[top][j] = contador
                contador += 1
            top += 1 
        if contador > N_cuadrado:
            break
            
        if left <= right:
            for i in range(top, bottom + 1):
                matriz[i][right] = contador
                contador += 1
            right -= 1 

        if contador > N_cuadrado:
            break
            
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matriz[bottom][j] = contador
                contador += 1
            bottom -= 1 

        if contador > N_cuadrado:
            break

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matriz[i][left] = contador
                contador += 1
            left += 1 

    imprimir_matriz(matriz, N)


def imprimir_matriz(matriz, N):
    max_ancho = len(str(N * N))
    
    print(f"\nMatriz Espiral {N}x{N}:")
    for fila in matriz:
        print(" ".join(f"{num:>{max_ancho}}" for num in fila))


generar_matriz_espiral(4)

generar_matriz_espiral(5)

generar_matriz_espiral(2)