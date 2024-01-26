# Here I will great a GUI in order to make the collection and management of data
# simpler and more user friendly.

from tkinter import *

window = Tk()
window.minsize(width=250, height =500)

window.title("Calorie Calculator and Meal planner")


label = Label(text="In order to calculate your BMI\n we will need to take some personal info.", font=('ariel', 12, 'bold'))
label.grid(row=0, column =1)
name_label = Label(text="Whats your name?")
name_label.grid(row=1, column=0)
name_entry = Entry()
name_entry.grid(row=1, column=3)
weight_label = Label(text="Enter your Weight")
weight_label.grid(row=4, column=1)

# def to_km():
#     output_label.config(text=str(float(entry.get()) * 1.609344))
#
# def to_miles():
#     output_label.config(text=str(float(entry.get()) / 1.609344))

button = Button(text='Calculate')
button.grid(row=14, column=1)

output_label =Label(text='')
output_label.grid(row=2, column=1)

def radio_used():
    if weight_radio_state.get() == 1:
        print("KG")
        weight_entry = Entry()
        weight_entry.grid(row=5, column=5)
        weight_label2 = Label(text='KG')
        weight_label2.grid(row=5, column=6)
        # label1.config(text="KMs")
        # label2.config(text="Miles")
        # button.config(command=to_miles)
    if weight_radio_state.get() == 2:
        print("Stone,Pound")
        weight_entry2 = Entry()
        weight_entry2.grid(row=4, column=5)
        weight_label2 = Label(text='Stone')
        weight_label2.grid(row=4, column=6)
        weight_entry = Entry()
        weight_entry.grid(row=5, column=5)
        weight_label2 = Label(text='Pounds')
        weight_label2.grid(row=5, column=6)
        # label1.config(text="Miles")
        # label2.config(text="KMs")
        # button.config(command=to_km)
    if weight_radio_state.get() == 3:
        print('Pounds')
        weight_entry = Entry()
        weight_entry.grid(row=5, column=5)
        weight_label2 = Label(text='Pounds')
        weight_label2.grid(row=5, column=6)
        # label1.config(text="Miles")
        # label2.config(text="KMs")
        # button.config(command=to_km)


weight_radio_state = IntVar()
weight_select_kg = Radiobutton(text="Weight in Kgs", value=1, variable=weight_radio_state, command=radio_used)
weight_select_stone_pounds = Radiobutton(text="Weight in Stone, Pounds", value=2, variable=weight_radio_state, command=radio_used)
weight_select_pounds = Radiobutton(text="Weight in pounds", value=3, variable=weight_radio_state, command=radio_used)

weight_select_kg.grid(row=3, column=0)
weight_select_stone_pounds.grid(row=4, column=0)
weight_select_pounds.grid(row=5, column=0)

height_radio_state = IntVar()

height_select_cm = Radiobutton(text="height in CMs", value=1, variable=height_radio_state, command=radio_used)
height_select_feet_inch = Radiobutton(text="Height in Feet, Inches", value=2, variable=height_radio_state, command=radio_used)
height_select_inch = Radiobutton(text="height in Inches", value=3, variable=height_radio_state, command=radio_used)

height_select_cm.grid(row=8, column=0)
height_select_feet_inch.grid(row=9, column=0)
height_select_inch.grid(row=10, column=0)

window.mainloop()