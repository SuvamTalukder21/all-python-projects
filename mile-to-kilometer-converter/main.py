from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=35, pady=20)


def convert_miles_to_kilometers():
    miles = float(user.get())
    kilometre = round(miles * 1.609, 3)
    # label3.config(text=f"{kilometre}")
    label3.config(text=str(kilometre))
    label3.grid(row=1, column=1)


user = Entry()
user.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert_miles_to_kilometers)
calculate.grid(row=2, column=1)

window.mainloop()
