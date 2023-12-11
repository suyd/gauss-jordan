import PySimpleGUI as sg      
import matriz as matrix_defs
import numpy as np
#variable global
flag = [False]

def modify_flag(flag):
    flag[0] = True
    
def return_value(text):
    layout = [[sg.Text(text, size=(15,1)), sg.InputText()],
              [sg.Submit("Siguiente"), sg.Cancel("Cancelar")]]

    window = sg.Window("Reducción Gauss Jordan", layout)
    event, values = window.read()

    input = 0

    if values[0] == '':
        modify_flag(flag)
        return 0

    if event == "Siguiente":
        input = values[0]

    if event == "Cancelar":
        window.close

    window.close()
    return int(input)

def display_matrix(matrix, msg):
    layout = [[sg.Text(msg, font='Default 25')],
             [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]

    max_row, max_column = matrix.shape
    #row, col are for the gui
    layout += [[sg.Text(str(matrix[row][col]), size=(4,2), pad=(1,1), border_width=2, key=(row,col)) for col in range(int(max_column))] for row in range(int(max_row))]

    layout += [[sg.Button("Siguiente")]]
    
    window = sg.Window("", layout)

    event, values = window.read()

    window.close() 

def display_string(string):
    layout = [[sg.Text(string)], [sg.Button("Continuar")]]
    window = sg.Window("", layout)
    event, values = window.read()
    window.close()



def window_modify_matrix(matrix, max_row, max_column, flag):
    layout = [[sg.Text('Matriz | Soluciones', font='Default 25')],
             [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]

    #row, col are for the gui
    layout += [[sg.Button(str(matrix[row][col]), size=(4,2), pad=(1,1), border_width=2, key=(row,col)) for col in range(int(max_column))] for row in range(int(max_row))]

    layout += [[sg.Button("Gauss")],[sg.Button("Inversa")],[sg.Cancel("Cerrar")]]

    window = sg.Window("Reducción Gauss Jordan", layout)

    event, values = window.read()

    if event == "Inversa":
        window.close()
        inverse_matrix = matrix_defs.calculate_inverse(matrix[:, :-1])
        msg = "La matriz inversa es: "
        display_matrix(inverse_matrix, msg)


    if event == "Gauss":
        window.close()
        #display_matrix(matrix, max_row, max_column)
        reduction_steps, solutions, infinite_solutions, rango_A, rango_B = matrix_defs.gauss_jordan_reduction(matrix)
        for step in reduction_steps:
            display_string(step)
        if(infinite_solutions):
            msg_soluciones = "El sistema tiene soluciones infinitas"
        else:
            msg_soluciones = "El sistema tiene soluciones finitas"

        display_string(msg_soluciones)
        
        msg_rango = "El rango de la matriz original es: " + str(rango_A) + "\nEl rango de la matriz ampliada es: " + str(rango_B) 
        display_string(msg_rango)
        modify_flag(flag)
            

    if event == "Exit" or event == sg.WIN_CLOSED or event == "Cerrar":
        modify_flag(flag)
        window.close()
    print(event)
    if isinstance(event, tuple):
        msg = str(str(event[0]+1) + " , " + str(event[1]+1) + ":")
        matrix[event[0], event[1]] = return_value(msg)

    window.close()
    return matrix

def event_loop():
    matriz_A = np.array([])
    matriz_B = np.array([])
    msg = "Ingrese la cantidad de variables:"
    size = return_value(msg)
    matriz_A = matrix_defs.gen_matrix(matriz_A, size, size)
    matriz_B = matrix_defs.gen_matrix(matriz_B, size, 1)
    matriz_ampliada = np.concatenate((matriz_A, matriz_B), axis=1)

    while flag[0] == False:
        matriz_ampliada = window_modify_matrix(matriz_ampliada, size, size+1, flag)
    
