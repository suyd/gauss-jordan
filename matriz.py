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

    
def test():
    matrix_A = np.array([])
    matrix_B = np.array([])

    size = 2

    matrix_A = gen_matrix(matrix_A, size, size)
    matrix_B = gen_matrix(matrix_B, size, 1)

    matrix_B = fill_matrix_manual(matrix_B, size, 1)

    print (matrix_A,matrix_B)
    #ask user for the matrix, and the solutions
    matrix_ampliada = np.concatenate((matrix_A, matrix_B), axis=1)
    print(matrix_ampliada)
