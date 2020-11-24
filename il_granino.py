#############################################
#   THis program takes the totals from the  #
#   il Granino Invoice and calculates the   #
#   total amount GST is to be paid on and   #
#   The total amount GST is not paid on     #
#                                           #
#   Written by S. Parker copywrite 2020     #
#############################################

from tkinter import *
from tkmacosx import Button

root = Tk()
# root.geometry("450x350")
root.title("Il Granino Invoice Converter for MYOB.")
root.iconbitmap("bread.icns")
root.configure(bg="#4ca6a6")

exgst = StringVar()                 # This sections creates the global variables
gst = StringVar()
result = StringVar()
resultgst = StringVar()


def calculate():
    a = float(exgst.get())          # Creates float variable 'a' with EX-GST value from user
    b = float(gst.get())            # Creates float variable 'b' with GST value from user
    c = b * 10                      # Creates variable 'c' and assigns it the GST paid
    e = ("%0.2f" % c)               # Creates the variable 'e' and formats 'c' to two decimal places
    d = a - c                       # creates the variable 'd' and assigns it the the GST value
    result.set(e)                   # assigns value of 'e' to variable result - The amount GST is paid on
    resultgst.set(d)                # assigns value of 'd' to variable resultgst - The amount GST is not paid on


def reset():                        # Clears all the input boxes by setting their value to null ""
    exgst.set("")
    gst.set("")
    result.set("")
    resultgst.set("")


def leave():
    root.destroy()                  # Ends the program by destroying the root frame


# User Entry EX-GST
txtexgst = Entry(root, width=10, textvariable=exgst, font=("Helvetica", 18), bd=0)
txtexgst.grid(row=1, column=1, padx=10, pady=10,)

# User Entry GST
txtgst = Entry(root, width=10, textvariable=gst, font=("Helvetica", 18), bd=0)
txtgst.grid(row=2, column=1, padx=10, pady=10)

# Output calculate GST
txtresult = Entry(root, width=10, textvariable=resultgst, font=("Helvetica", 18), bd=0)
txtresult.grid(row=5, column=1, padx=10, pady=10)

# Output calculate EX-GST
txtexgst = Entry(root, width=10, textvariable=result, font=("Helvetica", 18), bd=0)
txtexgst.grid(row=6, column=1, padx=10, pady=10)

lbltitle = Label(root, text="Il Granino Invoice to MYOB Conversion Program", bg="#4ca6a6", fg="#FFFFFF", font=("Helvetica", 24))
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)

# Label for EX-GST Amount
lblexgst = Label(root, text="Enter EX GST Amount on the Invoice", bg="#4ca6a6", fg="#FFFFFF")
lblexgst.grid(row=1, column=0, padx=10, pady=10)

# Label for GST Amount
lblgst = Label(root, text="Enter the GST Amount on the Invoice", bg="#4ca6a6", fg="#FFFFFF")
lblgst.grid(row=2, column=0, padx=10, pady=10)

# Label for EX_GST Amount Output
lblresult = Label(root, text="The EX-GST Amount is", bg="#4ca6a6", fg="#FFFFFF")
lblresult.grid(row=5, column=0, padx=10, pady=10)

# Label for GST Amount Output
lblgst = Label(root, text="The GST Amount is", bg="#4ca6a6", fg="#FFFFFF")
lblgst.grid(row=6, column=0, padx=10, pady=10)

# Button To Calculate
btnTotal = Button(root, text="Total", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=123, command=calculate)
btnTotal.grid(row=3, column=1, padx=10, pady=10)

# Button To reset
btnReset = Button(root, text="Reset", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=123, command=reset)
btnReset.grid(row=7, column=0, padx=10, pady=10)

# Button To Exit
btnExit = Button(root, text="Exit", borderless=1, relief='sunken', bordercolor='#000000', pady=10, padx=30, bg='#4c79a6', fg='#FFFFFF', width=123, command=leave)
btnExit.grid(row=7, column=1, padx=10, pady=10)

# Label copywrite
lblcopywrite = Label(root, text="\xa9 Copyright S.N.Parker 2020", bg="#4ca6a6", fg="#FFFFFF", font=("Helvetica", 10))
lblcopywrite.grid(row=8, column=0, padx=5, pady=20, sticky="W")

root.mainloop()
