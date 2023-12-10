import PySimpleGUI as sg      

#Ventana secundaria
def open_window(size):
    print(size)

    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

#EVENT LOOP
def main():
    layout = [[sg.Text('Tamaño de Matriz Cuadrada')],
             [sg.InputText()],
             [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Reducción Gauss Jordan', layout)    

    while True:
        event, values = window.read()
        print(event,values)
        if event == "Cancel" or event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == "Submit":
            open_window(int(values[0]))
    
    window.close()

if __name__ == "__main__":
    main()
    
