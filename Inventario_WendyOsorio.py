# Problema 3 - Inventario
# Estudiante: Wendy Katherine Osorio
# Grupo: 213022_770 - Ingeniería de Sistemas
# Centro: CCAV San Vicente - UNAD

# Matriz: [Codigo, Nombre, Stock actual, Stock minimo]
inventario = [
    [101, "Cuadernos", 3, 10],
    [102, "Lapices", 15, 10],
    [103, "Borradores", 2, 5],
    [104, "Reglas", 8, 8],
    [105, "Colores", 0, 12]
]

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

print("=== LISTA DE REABASTECIMIENTO ===")
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    actual = articulo[2]
    minimo = articulo[3]
    pedido = calcular_pedido(actual, minimo)
    print(f"Codigo {codigo} - {nombre} - Stock actual: {actual} - Stock minimo: {minimo} - Debe pedir: {pedido}")
