# Resuelve Sudoku - Informatica Aplicada
# Autor: [daniel omar andrade barraza]

def es_valido(tablero, fila, col, num):
    if num in tablero[fila]: return False
    for i in range(9):
        if tablero[i][col] == num: return False
    inicio_fila, inicio_col = 3*(fila//3), 3*(col//3)
    for i in range(inicio_fila, inicio_fila+3):
        for j in range(inicio_col, inicio_col+3):
            if tablero[i][j] == num: return False
    return True

def encontrar_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0: return (i,j)
    return None

def resolver(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio: return True
    fila, col = vacio
    for num in range(1,10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            if resolver(tablero): return True
            tablero[fila][col] = 0
    return False

def imprimir(tablero):
    for i in range(9):
        if i % 3 == 0 and i!= 0: print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j!= 0: print(" | ", end="")
            print(tablero[i][j] if tablero[i][j]!=0 else ".", end=" ")
        print()

# Ejemplo - puedes cambiarlo
tablero = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]

print("=== SUDOKU ORIGINAL ===")
imprimir(tablero)
if resolver(tablero):
    print("\n=== SUDOKU RESUELTO ===")
    imprimir(tablero)