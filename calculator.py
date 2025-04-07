import FreeSimpleGUI as sg

sg.theme("Dark")
input_task = sg.InputText("", key="input")

button_7 = sg.Button("7", key="7")
button_8 = sg.Button("8", key="8")
button_9 = sg.Button("9", key="9")
button_dev = sg.Button("/", key="devision")

button_4 = sg.Button("4", key="4")
button_5 = sg.Button("5", key="5")
button_6 = sg.Button("6", key="6")
button_mult = sg.Button("*", key="mult")

button_1 = sg.Button("1", key="1")
button_2 = sg.Button("2", key="2")
button_3 = sg.Button("3", key="3")
button_minus = sg.Button("-", key="minus")

button_0 = sg.Button("0", key="0")
button_point = sg.Button(".", key=".")
button_eq = sg.Button("=", key="equal")
button_plus = sg.Button("+", key="plus")

button_clear = sg.Button("C", key="clear")

output = sg.Text(key="output")


window = sg.Window("Calculator", layout=[
                    [input_task],
                    [button_7, button_8, button_9, button_dev],
                    [button_4, button_5, button_6, button_mult],
                    [button_1, button_2, button_3, button_minus],
                    [button_0, button_point, button_eq, button_plus],
                    [button_clear, output]])

current_input = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # If a number or operator is pressed, add it to the current input
    if event in "1234567890":
        current_input += event
        window["input"].update(current_input)
    elif event == "plus":
        current_input += "+"
        window["input"].update(current_input)
    elif event == "minus":
        current_input += "-"
        window["input"].update(current_input)
    elif event == "mult":
        current_input += "*"
        window["input"].update(current_input)
    elif event == "devision":
        current_input += "/"
        window["input"].update(current_input)
    elif event == ".":
        current_input += "."
        window["input"].update(current_input)


    # If "=" is pressed, evaluate the expression
    if event == "equal":
        result = eval(current_input)
        window["output"].update(result)

    if event == "clear":
        window["input"].update("")
        window["output"].update("")


window.close()

# print(eval(input('Enter the input: ')))