import PySimpleGUI as sg

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

layout = [
    [sg.Text("BMI Calculator")],
    [sg.Text("Weight (kg):"), sg.InputText("", key="weight", size=(10, 1))],
    [sg.Text("Height (m):"), sg.InputText("", key="height", size=(10, 1))],
    [sg.Text("", key="bmi_result", size=(20, 1))],
    [sg.Text("", key="category_result", size=(20, 1))],
    [sg.Button("Calculate"), sg.Button("Quit")]
]

window = sg.Window("BMI Calculator", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Quit"):
        break
    elif event == "Calculate":
        try:
            weight = float(values["weight"])
            height = float(values["height"])

            if weight <= 0 or height <= 0:
                window["bmi_result"].update("Invalid input. Please enter a positive number for weight and height.")
                window["category_result"].update("")
            else:
                bmi = calculate_bmi(weight, height)
                category = classify_bmi(bmi)

                window["bmi_result"].update("Your BMI is: " + str(round(bmi, 2)))
                window["category_result"].update("You are classified as: " + category)
        except ValueError:
            window["bmi_result"].update("Invalid input. Please enter a number for weight and height.")
            window["category_result"].update("")

window.close()