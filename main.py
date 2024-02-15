import random

import PySimpleGUI as sg

hist = []  # This is the user's input history. On pressing "=", it will smash it together and do the math.
hist_string = ""  # String to display on screen
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")"]
operators = ["+", "-", "*", "/"]
allowed_characters = numbers + operators
allowed_characters.append("=")
allowed_characters.append("Backspace")
allowed_characters.append("DEL")
equation = 0

# Initialise window and layout
layout = [
    [sg.Text(hist_string, key="input", size=(30, 2), font=('Helvetica', 15)),
     sg.Text(f"= {equation}", size=(30, 1), font=("Helvetica", 30), key="-EQUATION-")],
    [sg.Button("+", size=(8, 3), font=('Helvetica', 15)), sg.Button("-", size=(8, 3), font=('Helvetica', 15)),
     sg.Button("*", size=(8, 3), font=('Helvetica', 15)), sg.Button("/", size=(8, 3), font=('Helvetica', 15)),
     # sg.Text("NOTES\nIf your equation is not appearing, you may have added a lonesome ')' with nobody to love, "
     #         "so in their sorrow, they decided to ruin your fun, how rude :(. Make sure this doesn't happen by making "
     #         "sure your parenthesis are always in pairs.", size=(50, 10))
             ],
    [sg.Button("7", size=(8, 3), font=('Helvetica', 15)), sg.Button("8", size=(8, 3), font=('Helvetica', 15)),
     sg.Button("9", size=(8, 3), font=('Helvetica', 15)), sg.Button("(", size=(8, 3), font=('Helvetica', 15))],
    [sg.Button("4", size=(8, 3), font=('Helvetica', 15)), sg.Button("5", size=(8, 3), font=('Helvetica', 15)),
     sg.Button("6", size=(8, 3), font=('Helvetica', 15)), sg.Button(")", size=(8, 3), font=('Helvetica', 15))],
    [sg.Button("1", size=(8, 3), font=('Helvetica', 15)), sg.Button("2", size=(8, 3), font=('Helvetica', 15)),
     sg.Button("3", size=(8, 3), font=('Helvetica', 15)), sg.Button("DEL", size=(8, 3), font=('Helvetica', 15))],
    [sg.Button("0", size=(8, 3), font=('Helvetica', 15)),
     sg.Button("Backspace", size=(20, 3), font=('Helvetica', 15))]
]

sg.SetOptions(element_padding=(10, 10))

sg.theme(random.choice(sg.theme_list()))
window = sg.Window("Calculator", layout, size=(800, 600), finalize=True, enable_close_attempted_event=True)


def last_input_not_operator():
    try:
        if len(hist) != 0:
            if hist[-1] not in operators:
                return True
    except IndexError:
        return False


def finish_equation():
    global equation, hist_string, window
    hist_string = " ".join(hist_string)
    equation = ""
    try:
        for item in hist:
            equation = equation + str(item)
        print("equation", eval(equation))
        equation = eval(equation)
        window["-EQUATION-"].update(equation)
    except ValueError:
        window["-EQUATION-"].update("ERROR")
    except SyntaxError:
        # This is here to stop the program crashing and burning when the user has only entered 1 +
        # This is because we re-evaluate the equation every loop, including during half done equations
        pass
    except ZeroDivisionError:
        # There's probably some reason this isn't true, but I always thought something divided by 0 should equal 0.
        # Think of it like this: you have zero cookies, divided between however many people, there are no cookies to
        # give, so everyone gets 0 cookies each.
        # But to remain mathematically correct, I suppose we'll just tell the user off for being a silly goober.
        window["-EQUATION-"].update("Don't")


def main():
    global hist, hist_string, numbers, operators, allowed_characters, equation

    while True:
        main_event, main_values_input = window.read()

        if main_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or main_event == "Cancel":
            break

        print(main_event)
        if main_event in allowed_characters:
            try:
                if main_event == "Backspace":
                    if len(hist) != 0:
                        del hist[-1]
                elif main_event == "DEL":
                    # ERADICATE ZEM
                    hist = []
                    hist_string = ""
                    window["input"].update(hist_string)
                    window["-EQUATION-"].update(f"= {0}")  # It's kind of pointless to specify it being an int, but meh.
                    finish_equation()
                elif main_event in ("-", "(", ")") or main_event in operators and last_input_not_operator():
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

                finish_equation()
            except ValueError:
                pass


if __name__ == '__main__':
    main()
