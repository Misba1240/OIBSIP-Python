import PySimpleGUI as sg
import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

layout = [
    [sg.Text("Password Generator")],
    [sg.Text("Length:"), sg.InputText("", key="length", size=(5, 1))],
    [sg.Checkbox("Include lowercase letters", True, key="use_lowercase"),
     sg.Checkbox("Include uppercase letters", True, key="use_uppercase"),
     sg.Checkbox("Include digits", True, key="use_digits"),
     sg.Checkbox("Include symbols", True, key="use_symbols")],
    [sg.Button("Generate"), sg.Text("", key="password", size=(20, 1))],
]

window = sg.Window("Password Generator", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Cancel"):
        break
    elif event == "Generate":
        try:
            length = int(values["length"])
            use_lowercase = values["use_lowercase"]
            use_uppercase = values["use_uppercase"]
            use_digits = values["use_digits"]
            use_symbols = values["use_symbols"]

            password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
            window["password"].update(password)
        except ValueError as e:
            window["password"].update("Error: " + str(e))

window.close()