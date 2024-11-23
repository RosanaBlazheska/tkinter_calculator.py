import tkinter


def presmetaj():
    label.config(text=eval(entry.get()))


screen = tkinter.Tk()

entry = tkinter.Entry()

entry.grid(row=0, column=0)

button = tkinter.Button(text="presmetaj", command=presmetaj)

button.grid(row=3, column=0)

label = tkinter.Label(text="0")

label.grid(row=4, column=0)

screen.mainloop()