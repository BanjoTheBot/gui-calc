import PySimpleGUI as sg


def main():
    layout = [
        [sg.Button("7"), sg.Button("8"), sg.Button("9")],
        [sg.Button("4"), sg.Button("5"), sg.Button("6")],
        [sg.Button("1")], sg.Button("2"), sg.Button("3")],
    window = sg.Window("Calculator", layout, size=(800, 600), enable_close_attempted_event=True)

    while True:
        main_event, main_values_input = window.read()

        if main_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or main_event == "Cancel":
            break


if __name__ == '__main__':
    main()
