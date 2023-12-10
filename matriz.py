import numpy as np

class Matrix():
    def __init__(self):
        self.Matrix = np.array([])
        self.MAX_ROWS = 0
        self.MAX_COL = 0


def square_matrix(m, size):
    m.MAX_ROWS = m.MAX_COL = size
    m.Matrix = np.zeros( (m.MAX_ROWS, m.MAX_COL) )
    return m

#Rellenar por filas
def fill_matrix_manual(m):
    for i in range(m.MAX_COL):
        a = 0
        for j in range(m.MAX_ROWS):
            msg = "Fila " + str(i+1) + " Columna " + str(j+1) + ": "
            a = int(input(msg))
            m.Matrix[i][j] = a
    return m

def gauss_jordan():
    pass

#m = Matrix
#size = 2
#m = square_matrix(m, size)
#
#m = fill_matrix_manual(m)


#print(m.Matrix)
