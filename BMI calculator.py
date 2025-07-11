from tkinter import *

# Create window
root = Tk()
root.title("BMI Calculator")
root.geometry("350x400")

#colours like -snow,whitesmoke,gainsboro,ghostwhite gives light grey-white shade(looks like system color)
root.configure(bg="whitesmoke")

# ----- Functions -----
def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
            tip = "Eat more frequently. 💪"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            tip = "Stay active and eat balanced. 🥦"
        elif 25 <= bmi < 30:
            category = "Overweight"
            tip = "Cut sugar & walk daily. 🚶"
        else:
            category = "Obese"
            tip = "Start light exercise. 🧘"

        result_label.config(text=f"BMI: {bmi} ({category})")
        tip_label.config(text=f"Tip: {tip}")
    except Exception as e:
        print(e) # Show error reason on screen-
        result_label.config(text="Please enter valid numbers!")
        tip_label.config(text="")

def reset_fields():
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    result_label.config(text="")
    tip_label.config(text="")
    height_entry.focus_set() # So that cursor go on height entry for resetting entries.

# ----- Widgets -----

# Heading
heading = Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="whitesmoke")
heading.grid(row=0, column=0, columnspan=2, pady=10)  # column-span- so that input field occupy 2 columns & heading align in center.

# Height
Label(root, text="Enter Height (cm):", bg="whitesmoke", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W) # todo:sticky=W- grid geometry manager
# todo: sticky align inside cell content.Used with grid. Anchor mostly used with label,canvas,frame etc.

height_entry = Entry(root, width=25)
height_entry.grid(row=1, column=1, pady=5)

# Weight
Label(root, text="Enter Weight (kg):", bg="whitesmoke", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
weight_entry = Entry(root, width=25)
weight_entry.grid(row=2, column=1, pady=5)

# Buttons
calc_btn = Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white", width=20)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

#todo: Some colour name is not defined on tkinter so we use their hexa values for getting them.Like-material green 500 & material red 500.

reset_btn = Button(root, text="Reset", command=reset_fields, bg="#f44336", fg="white", width=20)
reset_btn.grid(row=4, column=0, columnspan=2, pady=5)

# Result
result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="whitesmoke")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Tip
tip_label = Label(root, text="", font=("Arial", 11), bg="whitesmoke", wraplength=300, justify="left")
#todo: wrap-length - It tells us after how many pixels text wrap in next line(instead of all text appear in one line & leads to stack overflow).
# It is used when we have to show a long message through widgets.
tip_label.grid(row=6, column=0, columnspan=2, padx=10)

# Show GUI window
root.mainloop()

