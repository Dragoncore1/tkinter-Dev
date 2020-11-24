from tkinter import *

root = Tk()
root.title("Conversion Program")
root.iconbitmap("wizard.jpg")
root.configure(background="#D6EAF8")

# Define Frame 1

lengthframe1 = LabelFrame(root, text="Converting Length", padx=5, pady=5, font=("Futura Bold", "15"), bg="#FCF3CF")
lengthframe1.grid(row=0, column=0, padx=10, pady=10)

# Define Frame 2
weightframe2 = LabelFrame(root, text="Converting Weight", padx=5, pady=5, font=("Futura Bold", "15"), bg="#ABEBC6")
weightframe2.grid(row=2, column=0, padx=10, pady=10)

# Define Result Labels
lengthresultlbl = Label(lengthframe1)
weightresultlbl = Label(weightframe2)

# Define Lenth Function


def length():
    global lengthresultlbl
    lengthresultlbl.destroy()
    lengthchoice = lengthclicked.get()
    if lengthchoice == "inches to cm":
        lengthnum1 = float(lengthnum.get())
        lengthresult = round(lengthnum1 * 2.54, 2)
    elif lengthchoice == "feet to cm":
        lengthnum1 = float(lengthnum.get())
        lengthresult = round(lengthnum1 * 30.48, 2)
    elif lengthchoice == "miles to km":
        lengthnum1 = float(lengthnum.get())
        lengthresult = round(lengthnum1 * 1.60934, 2)
    else:
        lengthresult = "Error"

    lengthresultlbl = Label(lengthframe1, text=lengthresult)
    lengthresultlbl.grid(row=4, column=1, sticky="W")

# Define Weight Function


def weight():
    global weightresultlbl
    weightresultlbl.destroy()
    weightchoice = weightclicked.get()
    if weightchoice == "ounces to grams":
        weightnum1 = float(weightnum.get())
        weightresult = round(weightnum1 * 28.35, 2)
    elif weightchoice == "pounds to grams":
        weightnum1 = float(weightnum.get())
        weightresult = round(weightnum1 * 454.592, 2)
    elif weightchoice == "pounds to kilograms":
        weightnum1 = float(weightnum.get())
        weightresult = round(weightnum1 / 2.205, 2)
    elif weightchoice == "stones to kilograms":
        weightnum1 = float(weightnum.get())
        weightresult = round(weightnum1 * 6.35, 2)
    else:
        weightresult = "Error"

    weightresultlbl = Label(weightframe2, text=weightresult)
    weightresultlbl.grid(row=4, column=1, sticky="W")


# Length Menu Items
lengthoption = [
    "inches to cm",
    "feet to cm",
    "miles to km",
]
lengthclicked = StringVar()
lengthclicked.set(lengthoption[0])

lengthdrop = OptionMenu(lengthframe1, lengthclicked, *lengthoption)
lengthdrop.grid(row=0, columnspan=2)
lengthdrop.config(font=("Arial Black", "15"), bg="yellow")


# Length User Input box
lengthnum = Entry(lengthframe1)
lengthnum.grid(row=1, column=1)

lengthuslbl = Label(lengthframe1, text="Enter number to convert")
lengthuslbl.grid(row=1, column=0, padx=10, pady=10)

lengthconvbtn = Button(lengthframe1, text="Convert Length", command=length)
lengthconvbtn.grid(row=3, column=1)

lengthanswer = Label(lengthframe1, text="The result is....")
lengthanswer.grid(row=4, column=0)


# Weight Menu Items
weightoption = [
    "ounces to grams",
    "pounds to grams",
    "pounds to kilograms",
    "stones to kilograms"
]
weightclicked = StringVar()
weightclicked.set(weightoption[0])

weightdrop = OptionMenu(weightframe2, weightclicked, *weightoption)
weightdrop.grid(row=0, columnspan=2)
weightdrop.config(font=("Arial Black", "15"), bg="green")


# Weight User Input box
weightnum = Entry(weightframe2)
weightnum.grid(row=1, column=1)

weightuslbl = Label(weightframe2, text="Enter number to convert")
weightuslbl.grid(row=1, column=0, padx=10, pady=10)

weightconvbtn = Button(weightframe2, text="Convert Weight", command=weight)
weightconvbtn.grid(row=3, column=1)

weightanswer = Label(weightframe2, text="The result is....")
weightanswer.grid(row=4, column=0)


root.mainloop()
