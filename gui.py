import PySimpleGUI as sg      
import matriz as matrix

def change_value():
    layout = [[sg.Text("Entrar valor", size=(15,1)), sg.InputText()],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window("Reducción Gauss Jordan", layout)
    event, values = window.read()

    input = 0

    if event == "Submit":
        input = values[0]

    
    window.close()
    return int(input)

def window_modify_matrix(m):
    layout = [[sg.Text('Matriz', font='Default 25')],
             [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]

    layout += [[sg.Button(str(m.Matrix[row][col]), size=(4,2), pad=(1,1), border_width=2, key=(row,col)) for col in range(int(m.MAX_COL))] for row in range(int(m.MAX_ROWS))]

    layout += [[sg.Cancel()]]

    window = sg.Window("Matriz", layout, modal=True)

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED or event == "Cancel":
        window.close()
        return -1

    else:
        m.Matrix[event[0], event[1]] = change_value()

    window.close()
    

def window_get_size():
    layout = [[sg.Text('Tamaño de Matriz Cuadrada')],
             [sg.InputText()],
             [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Reducción Gauss Jordan', layout)    

    event, values = window.read()

    if event == "Submit":
        input = values[0]

    
    window.close()
    return int(input)


def event_loop():
    matriz_A = np.array([])
    matriz_B = np.array([])
    size = window_get_size()
    matriz_A = matriz.gen_matrix(matriz_A, size, size)
    matriz_B = matriz.gen_matrix(matriz_B, size, 1)

    while True:
        m = window_modify_matrix(m)
        if m == -1:
            break
    
