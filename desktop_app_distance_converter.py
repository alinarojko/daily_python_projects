import FreeSimpleGUI as sg
from functions import convert_km_miles
from functions import convert_miles_km


label1 = sg.Text("Distance Converter")
label2 = sg.Text("Enter Distance: ")
drop_down = sg.Combo(["KM to Miles", "Miles to KM"], key="choice", default_value="KM to Miles")

distance = sg.InputText(tooltip="Enter a distance", key="distance")

convert_button = sg.Button("Convert", key="convert")
clear_button = sg.Button("Clear", key="clear")

output_label = sg.Text("",key="output")

sg.theme("Black")
window = sg.Window('Distance Converter...', layout=[[label1],
                                                 [drop_down],
                                                 [label2, distance],
                                                 [convert_button, clear_button],
                                                 [output_label]])
while True:
    event, values = window.read()
    distance_input = float(values["distance"])
    convertion_choice = values["choice"]
    if event == "convert":
        if convertion_choice == "KM to Miles":
            window["output"].update(value=f"{distance_input} km is {convert_km_miles(distance_input)} miles")
        else :
            window["output"].update(value=f"{distance_input} miles is {convert_miles_km(distance_input)} km")
    if  event == "clear":
        window["distance"].update("")
        window["output"].update("")
    if event ==  "Exit":
        break
    if event == sg.WIN_CLOSED:
        break

window.read()
window.close()
