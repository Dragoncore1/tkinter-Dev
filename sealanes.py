from tkinter import *
from tkmacosx import Button

root = Tk()
root.geometry("520x500")
root.title("Sealanes to MYOB Cconversion Program")
root.iconbitmap("chef.icns")
root.configure(bg="#4ca6a6")

# Create Variable
seaexgst = StringVar()
seagst = StringVar()
crunchexgst = StringVar()
crunchegst = StringVar()
cogsfood = StringVar()
resultadd = StringVar()
resultfood = StringVar()


# Define Functions
def calculate():
    a = float(seaexgst.get())
    b = float(seagst.get())
    d = float(crunchexgst.get())
    e = float(crunchegst.get())
    g = float(cogsfood.get())

    h = float(b - e)  # Difference between both GST amounts
    i = float(h * 10)  # Difference in GST Value
    k = ("%0.2f" % i)
    j = float(d + i)  # Crunchtime Ex-GST Amount + Difference in GST Amounts
    m = float(g - (j - a))
    n = ("%0.2f" % m)

    resultadd.set(k)
    resultfood.set(n)


def reset():
    seaexgst.set("")
    seagst.set("")
    crunchexgst.set("")
    crunchegst.set("")
    cogsfood.set("")
    resultadd.set("")
    resultfood.set("")


def finish():
    root.destroy()


# Create Inputs
txtsealanes_ex = Entry(root, width=10, textvariable=seaexgst, font=("Helvetica", 18), bd=0)
txtsealanes_ex.grid(row=1, column=1, sticky="W")

txtsealanes_gst = Entry(root, width=10, textvariable=seagst, font=("Helvetica", 18), bd=0)
txtsealanes_gst.grid(row=2, column=1, sticky="W")

txtcrunch_ex = Entry(root, width=10, textvariable=crunchexgst, font=("Helvetica", 18), bd=0)
txtcrunch_ex.grid(row=3, column=1, sticky="W")

txtcrunch_gst = Entry(root, width=10, textvariable=crunchegst, font=("Helvetica", 18), bd=0)
txtcrunch_gst.grid(row=4, column=1, sticky="W")

txtcogs_food = Entry(root, width=10, textvariable=cogsfood, font=("Helvetica", 18), bd=0)
txtcogs_food.grid(row=5, column=1, sticky="W")


# Create Labels
lbltitle = Label(root, text="Sealanes Invoice to MYOB Conversion Program", bg="#4ca6a6", fg="#FFFFFF", font=("Helvetica", 24))
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)

lblsealanes_ex = Label(root, text="Input the EX-GST Amount from the Sealanes Invoice: ", bg="#4ca6a6", fg="#FFFFFF")
lblsealanes_ex.grid(row=1, column=0, pady=10, sticky="W")

lblsealanes_gst = Label(root, text="Input the GST Amount from the Sealanes Invoice: ", bg="#4ca6a6", fg="#FFFFFF")
lblsealanes_gst.grid(row=2, column=0, pady=10, sticky="W")

lblcrunch_ex = Label(root, text="Input the EX-GST Amount from Crunchtime: ", bg="#4ca6a6", fg="#FFFFFF")
lblcrunch_ex.grid(row=3, column=0, pady=10, sticky="W")

lblcrunch_gst = Label(root, text="Input the GST Amount from Crunchtime: ", bg="#4ca6a6", fg="#FFFFFF")
lblcrunch_gst.grid(row=4, column=0, pady=10, sticky="W")

lblcogs_food = Label(root, text="Input the COGS Food Amount from Crunchtime: ", bg="#4ca6a6", fg="#FFFFFF")
lblcogs_food.grid(row=5, column=0, pady=10, sticky="W")

# Create Buttons
btnCalc = Button(root, text="Calculate", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=123, command=calculate)
btnCalc.grid(row=6, column=1, sticky="W")
# Button To reset
btnReset = Button(root, text="Reset", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=130, command=reset)
btnReset.grid(row=9, column=0, sticky="W")
# Button To Exit
btnfinish = Button(root, text="Exit", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=130, command=finish)
btnfinish.grid(row=9, column=1, sticky="W")

# Label for GST Amount Output
lbloutadd = Label(root, text="Add a food line with a total of", bd=0, bg='#4ca6a6', fg='#FFFFFF')
lbloutadd.grid(row=7, column=0, padx=10, pady=10, sticky="W")
# Label for GST Amount Output
lbloutnewfood = Label(root, text="Change the existing COGS Food to", bd=0, bg='#4ca6a6', fg='#FFFFFF')
lbloutnewfood.grid(row=8, column=0, padx=10, pady=10, sticky="W")

# Output boxes
txtadd = Entry(root, width=11, textvariable=resultadd, font=("Helvetica", 18), bd=0)
txtadd.grid(row=7, column=1, sticky="W")

txtnew = Entry(root, width=11, textvariable=resultfood, font=("Helvetica", 18), bd=0)
txtnew.grid(row=8, column=1, sticky="W")

# Label copywrite
lblcopywrite = Label(root, text="\xa9 Copyright S.N.Parker 2020", bg="#4ca6a6", fg="#FFFFFF", font=("Helvetica", 10))
lblcopywrite.grid(row=10, column=1, padx=5, pady=25, sticky="W")

root.mainloop()
