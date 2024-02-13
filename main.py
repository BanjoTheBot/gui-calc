import random

import PySimpleGUI as sg

hist = []  # This is the user's input history. On pressing "=", it will smash it together and do the math.
hist_string = ""  # String to display on screen
numbers = ["7", "8", "9", "(", "4", "5", "6", "1", "2", "3", "0"]
operators = ["+", "-", "*", "/"]
allowed_characters = numbers + operators
allowed_characters.append("=")


def last_input_not_operator():
    try:
        print(len(hist))
        if len(hist) != 0:
            print("haha")
            if hist[-1] not in operators:
                return True
    except IndexError:
        return False


def main():
    global hist, hist_string, numbers, operators, allowed_characters
    layout = [
        [sg.Text(hist_string, key="input")],
        [sg.Button("+"), sg.Button("-"), sg.Button("*"), sg.Button("/")],
        [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("(")],
        [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button(")")],
        [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("=")],
        [sg.Button("0"), sg.Button("Backspace")],
    ]

    sg.theme(random.choice(sg.theme_list()))
    window = sg.Window("Calculator", layout, size=(800, 600), enable_close_attempted_event=True)

    while True:
        main_event, main_values_input = window.read()

        if main_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or main_event == "Cancel":
            break

        print(main_event)
        if main_event in allowed_characters:
            print("cock")
            print(hist)
            print("cock", hist_string)
            try:
                print(hist)
                if main_event == "Backspace":
                    if len(hist) != 0:
                        print(hist)
                        print("how", hist_string)
                        hist.remove([-1])
                elif main_event in operators and last_input_not_operator():
                    print("hehe" + main_event)
                    hist.append(main_event)
                else:
                    print(int(main_event))
                    hist.append(int(main_event))
                    window.refresh()
                print(hist)

                # for item in hist:
                # print("item", item)
                # hist_string = ""
                print(len(hist))
                hist_string = hist_string + (" " if hist[-1] != "(" or ")" else "") + str(hist[-1])
                print(hist_string)
                # if hist_string[0] == " ":
                #     hist_string = hist_string[:-1]
                window["input"].update(hist_string)
            except ValueError as e:
                sg.PopupError(e)


if __name__ == '__main__':
    main()
