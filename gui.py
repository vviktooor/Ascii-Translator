from tkinter import *
import tkinter
import customtkinter
import operations

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.title("Translator app by vviktooor")

tabView = customtkinter.CTkTabview(master=app,
                                   corner_radius=10
                                   )
tabView.pack(padx=20, pady=20, anchor=tkinter.CENTER, fill=BOTH, expand=True)

tabView.add("ASCII TO TEXT")
tabView.add("TEXT TO ASCII")

""" ASCII TO TEXT ELEMENTS """
tk_textbox = tkinter.Text(master=tabView.tab("ASCII TO TEXT"), highlightthickness=0, font=("Arial", 11))
tk_textbox.grid(row=0, column=0, sticky="nsew")

ctk_texbox_scrollbar = customtkinter.CTkScrollbar(master=tabView.tab("ASCII TO TEXT"), command=tk_textbox.yview)
ctk_texbox_scrollbar.grid(row=0, column=1, sticky="ns")

tk_textbox.configure(yscrollcommand=ctk_texbox_scrollbar.set)

button = customtkinter.CTkButton(master=tabView.tab("ASCII TO TEXT"), corner_radius=10, text="CONVERT", command=operations.button_event, font=("Arial", 11))
button.grid(row=1, column=0, sticky="nsew", pady=10)

tk_textbox1 = tkinter.Text(master=tabView.tab("ASCII TO TEXT"), highlightthickness=0, font=("Arial", 11))
tk_textbox1.grid(row=2, column=0, sticky="nsew")

ctk_texbox_scrollbar1 = customtkinter.CTkScrollbar(master=tabView.tab("ASCII TO TEXT"), command=tk_textbox1.yview)
ctk_texbox_scrollbar1.grid(row=2, column=1, sticky="ns")

tk_textbox1.configure(yscrollcommand=ctk_texbox_scrollbar1.set)

""" TEXT TO ASCII ELEMENTS"""
tk_textbox2 = tkinter.Text(master=tabView.tab("TEXT TO ASCII"), highlightthickness=0, font=("Arial", 11))
tk_textbox2.grid(row=0, column=0, sticky="nsew")

ctk_texbox_scrollbar2 = customtkinter.CTkScrollbar(master=tabView.tab("TEXT TO ASCII"), command=tk_textbox2.yview)
ctk_texbox_scrollbar2.grid(row=0, column=1, sticky="ns")

tk_textbox2.configure(yscrollcommand=ctk_texbox_scrollbar2.set)

button1 = customtkinter.CTkButton(master=tabView.tab("TEXT TO ASCII"), corner_radius=10, text="CONVERT", command=operations.button_event1, font=("Arial", 11))
button1.grid(row=1, column=0, sticky="nsew", pady=10)

tk_textbox3 = tkinter.Text(master=tabView.tab("TEXT TO ASCII"), highlightthickness=0, font=("Arial", 11))
tk_textbox3.grid(row=2, column=0, sticky="nsew")

ctk_texbox_scrollbar3 = customtkinter.CTkScrollbar(master=tabView.tab("TEXT TO ASCII"), command=tk_textbox3.yview)
ctk_texbox_scrollbar3.grid(row=2, column=1, sticky="ns")

tk_textbox3.configure(yscrollcommand=ctk_texbox_scrollbar3.set)

# Making columns resizable with different weights
tabView.tab("ASCII TO TEXT").grid_columnconfigure(0, weight=1)
tabView.tab("ASCII TO TEXT").grid_columnconfigure(1, weight=0)

tabView.tab("TEXT TO ASCII").grid_columnconfigure(0, weight=1)
tabView.tab("TEXT TO ASCII").grid_columnconfigure(1, weight=0)

# Making rows resizable
for i in range(3):
    tabView.tab("ASCII TO TEXT").grid_rowconfigure(i, weight=1)

for i in range(3):
    tabView.tab("TEXT TO ASCII").grid_rowconfigure(i, weight=1)

app.mainloop()
