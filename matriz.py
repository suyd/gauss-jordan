import numpy as np

def gen_matrix(matrix, rows, columns):
    matrix = np.zeros([rows, columns])
    return matrix

#Rellenar por filas
def fill_matrix_manual(matrix, rows, columns):
    for i in range(columns):
        a = 0
        for j in range(rows):
            msg = "Fila " + str(i+1) + " Columna " + str(j+1) + ": "
            a = int(input(msg))
            matrix[j][i] = a
    return matrix

#def gauss_jordan_reduction(matrix, const_vector):
def gauss_jordan_reduction(aug_matrix):
    rows, cols = aug_matrix.shape
    steps = []  # Almacenar los pasos de reducción

    for i in range(rows):
        # Normalizar la fila para tener un 1 en la diagonal
        diagonal_element = aug_matrix[i, i]
        aug_matrix[i] = aug_matrix[i] / diagonal_element
        steps.append(f"Paso {i + 1}: Normalizar fila {i + 1} ->\n{aug_matrix}\n")

        # Hacer ceros en las otras filas en la misma columna
        for j in range(rows):
            if i != j:
                factor = aug_matrix[j, i]
                aug_matrix[j] = aug_matrix[j] - factor * aug_matrix[i]
                steps.append(f"Paso {i + 1}: Hacer ceros en fila {j + 1} ->\n{aug_matrix}\n")

    # Obtener el vector de soluciones
    solutions = aug_matrix[:, -1]
    # Verificar si hay filas con ceros en la parte de coeficientes y un valor no cero en el lado derecho
    infinite_solutions = any(np.all(aug_matrix[:, :-1] == 0, axis=1) & (aug_matrix[:, -1] != 0))

    rango_A = np.linalg.matrix_rank(aug_matrix[:, :-1])
    rango_B = np.linalg.matrix_rank(aug_matrix)
    return steps, solutions, infinite_solutions, rango_A, rango_B

def calculate_inverse(matrix):
    # Calcular la matriz inversa si es cuadrada
    inverse_matrix = None
    if matrix.shape[0] == matrix.shape[1]:  # Verificar si es cuadrada
        inverse_matrix = np.linalg.inv(matrix)

    return inverse_matrix
   
def test():
    matrix_A = np.array([])
    matrix_B = np.array([])

    size = 2

    matrix_A = gen_matrix(matrix_A, size, size)
    matrix_B = gen_matrix(matrix_B, size, 1)

    matrix_A = fill_matrix_manual(matrix_A, size, size)
    matrix_B = fill_matrix_manual(matrix_B, size, 1)

    aug_matrix = np.concatenate((matrix_A, matrix_B), axis=1)

    #ask user for the matrix, and the solutions
    reduction_steps, solutions = gauss_jordan_reduction(aug_matrix)

    print(reduction_steps)
    for step in reduction_steps:
        print(step)

# Imprimir el vector de soluciones
    print("Vector de soluciones:", solutions)
    
#test()
