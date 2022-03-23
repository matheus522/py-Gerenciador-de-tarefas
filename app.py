import PySimpleGUI as sg

# Criar tarefa


def new_init_window():
    tema_padrao = 'DarkBlue17'

    sg.theme(tema_padrao)
    linha = [
        [sg.Combo(['-None-', 'ToDo', 'Doing', 'Done'], key='stage',
                  default_value='-None-'), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tasks', layout=linha, key='container')],
        [sg.Button('New Task'), sg.Button('Reset')],
        [sg.Button('change theme')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)


# Criar janela
janela = new_init_window()

# Criar regras da janela
while True:
    tema_padrao = 'DarkBlue17'
    tema_atual = 'DarkBlue17'

    event, values = janela.read()
    # Encerra o programa
    if event == sg.WIN_CLOSED:
        break
    # Cria nova tarefa
    elif event == 'New Task':
        janela.extend_layout(janela['container'], [
            [sg.Combo(['ToDo', 'Doing', 'Done'], key='stage'), sg.Input('')]])
    # Reseta configs
    elif event == 'Reset':
        janela.Close()
        janela = new_init_window()
    # altera tema
    elif event == 'change theme':
        if tema_padrao == tema_atual:
            sg.theme('Default')
            print('2')
        else:
            sg.theme(tema_padrao)
