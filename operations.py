import gui

def ascii_to_text(user_input_ascii):
    list_of_inputs = []
    converted = []
    list_of_inputs.append(user_input_ascii.split())

    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(chr(int(char)))

    for i in range(len(converted)):
        gui.tk_textbox1.insert("end", (str(converted[i])))
def text_to_ascii(user_input_text):
    list_of_inputs = []
    converted = []
    list_of_inputs.append(user_input_text)

    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(ord(char))

    converted.remove(converted[-1])
    for i in range(len(converted)):
        gui.tk_textbox3.insert("end", (str(converted[i]) + " "))

def button_event():
    user_input_ascii = gui.tk_textbox.get("0.0", "end")
    clear = gui.tk_textbox1.delete("0.0", "end")
    ascii_to_text(user_input_ascii)

def button_event1():
    user_input_text =gui.tk_textbox2.get("0.0", "end")
    clear = gui.tk_textbox3.delete("0.0", "end")
    text_to_ascii(user_input_text)