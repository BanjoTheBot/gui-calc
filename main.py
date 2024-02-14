import random

import PySimpleGUI as sg

hist = []  # This is the user's input history. On pressing "=", it will smash it together and do the math.
hist_string = ""  # String to display on screen
numbers = ["7", "8", "9", "(", "4", "5", "6", "1", "2", "3", "0"]
operators = ["+", "-", "*", "/"]
allowed_characters = numbers + operators
allowed_characters.append("=")
allowed_characters.append("Backspace")


def last_input_not_operator():
    try:
        if len(hist) != 0:
            if hist[-1] not in operators:
                return True
    except IndexError:
        return False


def main():
    global hist, hist_string, numbers, operators, allowed_characters
    layout = [
        [sg.Text(hist_string, key="input", size=(30, 2), font=('Helvetica', 15))],
        [sg.Button("+", size=(8, 3), font=('Helvetica', 15)), sg.Button("-", size=(8, 3), font=('Helvetica', 15)),
         sg.Button("*", size=(8, 3), font=('Helvetica', 15)), sg.Button("/", size=(8, 3), font=('Helvetica', 15))],
        [sg.Button("7", size=(8, 3), font=('Helvetica', 15)), sg.Button("8", size=(8, 3), font=('Helvetica', 15)),
         sg.Button("9", size=(8, 3), font=('Helvetica', 15)), sg.Button("(", size=(8, 3), font=('Helvetica', 15))],
        [sg.Button("4", size=(8, 3), font=('Helvetica', 15)), sg.Button("5", size=(8, 3), font=('Helvetica', 15)),
         sg.Button("6", size=(8, 3), font=('Helvetica', 15)), sg.Button(")", size=(8, 3), font=('Helvetica', 15))],
        [sg.Button("1", size=(8, 3), font=('Helvetica', 15)), sg.Button("2", size=(8, 3), font=('Helvetica', 15)),
         sg.Button("3", size=(8, 3), font=('Helvetica', 15)), sg.Button("=", size=(8, 3), font=('Helvetica', 15))],
        [sg.Button("0", size=(8, 3), font=('Helvetica', 15)),
         sg.Button("Backspace", size=(20, 3), font=('Helvetica', 15))]

    ]

    sg.SetOptions(element_padding=(10, 10))

    sg.theme(random.choice(sg.theme_list()))
    window = sg.Window("Calculator", layout, size=(800, 600), finalize=True, enable_close_attempted_event=True)

    while True:
        main_event, main_values_input = window.read()

        if main_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or main_event == "Cancel":
            break

        print(main_event)
        if main_event in allowed_characters:
            try:
                print(hist)
                if main_event == "=":
                    hist_string = " ".join(hist_string)
                    equation = ""
                    for item in hist:
                        equation = equation + str(item)
                    print("equation", eval(equation))

                    # try:
                # except ValueError:
                #     sg.popup_error("boywhatdahellboy")

                # print(main_event)
                if main_event == "Backspace":
                    print("cock")
                    if len(hist) != 0:
                        del hist[-1]
                elif main_event in operators and last_input_not_operator():
                    hist.append(main_event)
                else:
                    print(int(main_event))
                    hist.append(int(main_event))
                    window.refresh()
                print(hist)

                hist_string = ""
                for item in hist:
                    print("this is hist", hist)
                    hist_string = hist_string + (" " if hist[-1] != "(" or ")" else "") + str(item)
                window["input"].update(hist_string)
            except ValueError:
                # sg.PopupError(e)
                pass

if __name__ == '__main__':
    main()
