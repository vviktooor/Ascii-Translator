from art import *
from tkinter import *
import tkinter
import customtkinter

def main():
    tprint("ASCII TO TEXT  OR  TEXT TO ASCII", font='small')
    print("PLEASE WRITE: \n 1 --> ASCII TO TEXT \n 2 --> TEXT TO ASCII \n")
    user_choice = int(input("YOUR CHOICE: \n"))

    if user_choice == 1:
        ascii_to_text()
    elif user_choice == 2:
        text_to_ascii()
    else:
        print("THIS OPTION NOT EXIST!")

def ascii_to_text(user_input_ascii):
    list_of_inputs = []
    converted = []
    list_of_inputs.append(user_input_ascii.split())

    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(chr(int(char)))

    for i in range(len(converted)):
        tk_textbox1.insert("end", (str(converted[i])))
def text_to_ascii(user_input_text):
    list_of_inputs = []
    converted = []
    list_of_inputs.append(user_input_text)

    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(ord(char))

    converted.remove(converted[-1])
    for i in range(len(converted)):
        tk_textbox3.insert("end", (str(converted[i]) + " "))


def button_event():
    user_input_ascii = tk_textbox.get("0.0", "end")
    clear = tk_textbox1.delete("0.0", "end")
    ascii_to_text(user_input_ascii)

def button_event1():
    user_input_text = tk_textbox2.get("0.0", "end")
    clear = tk_textbox3.delete("0.0", "end")
    text_to_ascii(user_input_text)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.title("Translator app by vviktooor")

tabView = customtkinter.CTkTabview(master=app,
                                   corner_radius=10
                                   )
tabView.pack(padx= 20, pady = 20, anchor=tkinter.CENTER)

tabView.add("ASCII TO TEXT")
tabView.add("TEXT TO ASCII")

""" ASCII TO TEXT ELEMENTS """
tk_textbox = tkinter.Text(master=tabView.tab("ASCII TO TEXT"), highlightthickness=0, font=("Arial", 11))
tk_textbox.grid(row=0, column=0, sticky="ns")

ctk_texbox_scrollbar = customtkinter.CTkScrollbar(master=tabView.tab("ASCII TO TEXT"), command=tk_textbox.yview)
ctk_texbox_scrollbar.grid(row=0, column=1, sticky="ns")

tk_textbox.configure(yscrollcommand=ctk_texbox_scrollbar.set)

button = customtkinter.CTkButton(master=tabView.tab("ASCII TO TEXT"), corner_radius=10, text="CONVERT", command=button_event, font=("Arial", 11))
button.grid(row=1, column=0, sticky="ns", pady=10)

tk_textbox1 = tkinter.Text(master=tabView.tab("ASCII TO TEXT"), highlightthickness=0, font=("Arial", 11))
tk_textbox1.grid(row=2, column=0, sticky="ns")

ctk_texbox_scrollbar1 = customtkinter.CTkScrollbar(master=tabView.tab("ASCII TO TEXT"), command=tk_textbox1.yview)
ctk_texbox_scrollbar1.grid(row=2, column=1, sticky="ns")

tk_textbox1.configure(yscrollcommand=ctk_texbox_scrollbar1.set)
""" TEXT TO ASCII ELEMENTS"""
tk_textbox2 = tkinter.Text(master=tabView.tab("TEXT TO ASCII"), highlightthickness=0, font=("Arial", 11))
tk_textbox2.grid(row=0, column=0, sticky="ns")

ctk_texbox_scrollbar2 = customtkinter.CTkScrollbar(master=tabView.tab("TEXT TO ASCII"), command=tk_textbox2.yview)
ctk_texbox_scrollbar2.grid(row=0, column=1, sticky="ns")

tk_textbox2.configure(yscrollcommand=ctk_texbox_scrollbar2.set)

button1 = customtkinter.CTkButton(master=tabView.tab("TEXT TO ASCII"), corner_radius=10, text="CONVERT", command=button_event1, font=("Arial", 11))
button1.grid(row=1, column=0, sticky="ns", pady=10)

tk_textbox3 = tkinter.Text(master=tabView.tab("TEXT TO ASCII"), highlightthickness=0, font=("Arial", 11))
tk_textbox3.grid(row=2, column=0, sticky="ns")

ctk_texbox_scrollbar3 = customtkinter.CTkScrollbar(master=tabView.tab("TEXT TO ASCII"), command=tk_textbox3.yview)
ctk_texbox_scrollbar3.grid(row=2, column=1, sticky="ns")

tk_textbox3.configure(yscrollcommand=ctk_texbox_scrollbar3.set)

app.mainloop()

if __name__ == '__main__':
    main()