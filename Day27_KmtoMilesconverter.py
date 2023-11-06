from tkinter import *

#Create my GUI window
window=Tk()
window.title("Km to Miles converter")
window.minsize(width=300,height=300)

#Create space
space=Label(text=" ",font=(24))
space.grid(column=1,row=1)
#Create a label for Km
km_label=Label()
km_label.config(text="Km",font=("Calibri",24,"bold"))
km_label.grid(column=3,row=2)
#Create an entry for the km
km_entry=Entry()
km_entry.config(width=10,font=("Calibri",24))
km_entry.grid(column=2,row=2)


#Create a label for Miles
mile_label=Label()
mile_label.config(text="Miles",font=("Calibri",24,"bold"))
mile_label.grid(column=3,row=4)
#Create an entry for the number of Miles
milenr_label=Label()
milenr_label.config(font=("Calibri",24))
milenr_label.grid(column=2,row=4)

#Create a buttom for conversion
def action():
    num_miles=round(float(km_entry.get())/1.6,3)
    milenr_label.config(text=str(num_miles))

#calls action() when pressed
conv_button = Button(text="Convert", font=("Calibri",24), command=action)
conv_button.grid(column=2,row=5)

#Create a label for "is equal to"
mile_label=Label()
mile_label.config(text="is equal to",font=("Calibri",24,"bold"))
mile_label.grid(column=1,row=3)


window.mainloop()

