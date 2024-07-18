from tkinter import *
window = Tk()
window.minsize(width=300, height=200)
window.maxsize(width=300, height=200)
window.title("Miles to Km converter")

label = Label(text="Miles\n\nKm", font='Arial')
label.place(x=195, y=20)

miles_entry = Entry()
miles_entry.place(x=70, y=24)
miles_entry.insert(END, string="0")

km_entry = Entry()
km_entry.place(x=70, y=60)


def convert():
    value = float(miles_entry.get())
    value *= 1.60934
    return str(round(value, 2))


def entry():
    km_entry.delete(0, END)
    km_entry.insert(END, string=convert())


button = Button(text="convert", command=entry)
button.place(x=120, y=100)

window.mainloop()
