# GUI for Camel-C-Up
# Paul and Wyatt

import tkinter
from tkinter import messagebox

def exit():
    warning = tkinter.messagebox.askyesno("Warning!", "are you sure you want to exit?")
    if warning:
        main_window.destroy()

main_window = tkinter.Tk()
main_window.geometry('1000x500')
main_window.title("Camel Up Board Game")

Board = tkinter.Frame(main_window)
Board.grid()

exit_button = tkinter.Button(Board, text="Exit", bg=("red"), command=exit)
exit_button.grid(row=0, column=0)

Board.mainloop()