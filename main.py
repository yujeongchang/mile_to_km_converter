from tkinter import *
window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

def calculate():
    input_miles = float(entry.get())
    cal_km = round(input_miles * 1.609344, 2)   #int
    calculated_km.config(text= f"{cal_km}")
    return cal_km

is_equal_to = Label(text="is equal to", font=("Arial", 15))
is_equal_to.grid(column=0, row=1)
# is_equal_to.config(padx=50, pady=110)

entry = Entry(width=8)
entry.grid(column=1, row=0)

mile = Label(text="Miles", font=("Arial", 15))
mile.grid(column=2 ,row=0)

calculated_km = Label(text="0", font=("Arial", 15))
calculated_km.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 15))
km.grid(column=2 ,row=1)

button_cal = Button(text="Calculate", command=calculate)
button_cal.grid(column=1, row=2)
window.mainloop()