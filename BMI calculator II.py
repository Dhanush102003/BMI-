import tkinter

app = tkinter.Tk()
app.title("BMI Calculator ")
app.minsize(width=400, height=140)
app.config(bg='black')


def calculate_bmi():
    instruct_welcome = str(instruct_label.get())
    name_input = str(name_entry.get())
    weight_input = int(weight_entry.get())
    height_input = int(height_entry.get())
    bmi = weight_input / (height_input * height_input/10000)
    classification = ["Under Weight", "Normal", "Over Weight", "Obesity (Class I)", "Obesity (Class II)",
                      "Extreme Obesity"]

    for i in range(len(classification)):
        if bmi < 18.5:
            i = 0
        elif bmi < 24.9:
            i = 1
        elif bmi < 29.9:
            i = 2
        elif bmi < 34.9:
            i = 3
        elif bmi < 39.9:
            i = 4
        elif bmi > 40:
            i = 5
    sonuc_label.config(text=(f"{name_input} Your Bmi is " + '{:.2f}'.format(bmi)  + "and You are " + classification[i]))


instruct_label = tkinter.Label(text='Welcome to BMI calculator',font=35,bg='red')
instruct_label.pack()
name_label = tkinter.Label(text="Enter Your Name",font=30, bg='light green',)
name_label.pack(pady=6)
name_entry = tkinter.Entry(width=15,bg='light pink',font=15)
name_entry.pack(pady=5)

weight_label = tkinter.Label(text="Enter Your Weight (kg)",font=30,pady=6, bg='light green')
weight_label.pack()
weight_entry = tkinter.Entry(width=15,font=15,bg='light pink')
weight_entry.pack(pady=5)
height_label = tkinter.Label(text="Enter Your Height (cm)",font=30,pady=6, bg='light green')
height_label.pack()
height_entry = tkinter.Entry(width=20,font=15,bg='light pink')
height_entry.pack(pady=5)
calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi,font=30, bg='light green')
calculate_button.pack()
sonuc_label = tkinter.Label(bg='light pink')
sonuc_label.pack(pady=5)

app.mainloop()