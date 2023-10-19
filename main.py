from tkinter import *

window = Tk()
window.title("Mole to KM converter")
window.config(pady=20, padx=20)

miles_entry = Entry(width=5)

miles_entry.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=2)

km_entry = Label(text=0)

km_entry.grid(column=1, row=2)

km = Label(text="Km")
km.grid(column=2, row=2)


def convert():
    miles_distance = float(miles_entry.get())
    km_distance = round(miles_distance * 1.6, 2)
    km_entry.config(text=f"{km_distance}")


calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=3)


window.mainloop()
