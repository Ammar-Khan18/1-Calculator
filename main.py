from tkinter import *
# Function to Display the NUmbers and Symbols
def addToEqu(num):
    global equText
    equText += str(num)
    equLabel.set(equText)
# Function to evaluate the expression
def equateEqu():
    global equText
    try:
        total = str(eval(equText))
        equLabel.set(total)
        equText = total
    except ZeroDivisionError:
        equLabel.set("Arithmatic Error")
        equText = ""
    except SyntaxError:
        equLabel.set("Syntax Error")
        equText = ""
# Function to clear the Display
def clearEqu():
    global equText
    equLabel.set("")
    equText = ""
# Initialising Window
root= Tk()
root.title("Calculator")
root.configure(background="light grey")
root.geometry("500x550")
# Variable Declaration
equText = ""
equLabel = StringVar()
h = 3
w = 9
# Display
label = Label(root,textvariable=equLabel,font=("Arial",24),background="light grey",width=24,height=2)
label.pack()
# Frame
frame = Frame(root)
frame.configure(background="light grey")
frame.pack()
# All GUI Buttons
button7 = Button(frame,text=7,height=h,width=w,font=(40),command=lambda: addToEqu(7)).grid(column=0,row=0)
button8 = Button(frame,text=8,height=h,width=w,font=(40),command=lambda: addToEqu(8)).grid(column=1,row=0)
button9 = Button(frame,text=9,height=h,width=w,font=(40),command=lambda: addToEqu(9)).grid(column=2,row=0)
button4 = Button(frame,text=4,height=h,width=w,font=(40),command=lambda: addToEqu(4)).grid(column=0,row=1)
button5 = Button(frame,text=5,height=h,width=w,font=(40),command=lambda: addToEqu(5)).grid(column=1,row=1)
button6 = Button(frame,text=6,height=h,width=w,font=(40),command=lambda: addToEqu(6)).grid(column=2,row=1)
button1 = Button(frame,text=1,height=h,width=w,font=(40),command=lambda: addToEqu(1)).grid(column=0,row=2)
button2 = Button(frame,text=2,height=h,width=w,font=(40),command=lambda: addToEqu(2)).grid(column=1,row=2)
button3 = Button(frame,text=3,height=h,width=w,font=(40),command=lambda: addToEqu(3)).grid(column=2,row=2)
button0 = Button(frame,text=0,height=h,width=w,font=(40),command=lambda: addToEqu(0)).grid(column=1,row=3)
buttonLeftPara = Button(frame,text="(",height=h,width=w,font=40,command=lambda: addToEqu("(")).grid(column=0,row=3)
buttonRightPara = Button(frame,text=")",height=h,width=w,font=40,command=lambda: addToEqu(")")).grid(column=2,row=3)
plus = Button(frame,text="+",height=h,width=w,font=40,command=lambda: addToEqu("+")).grid(column=3,row=0)
minus = Button(frame,text="-",height=h,width=w,font=40,command=lambda: addToEqu("-")).grid(column=3,row=1)
multi = Button(frame,text="*",height=h,width=w,font=40,command=lambda: addToEqu("*")).grid(column=3,row=2)
divide = Button(frame,text="/",height=h,width=w,font=40,command=lambda: addToEqu("/")).grid(column=3,row=3)
dot = Button(frame,text=".",height=h,width=w,font=40,command=lambda: addToEqu(".")).grid(column=2,row=4)
equal = Button(frame,text="=",height=h,width=w,font=40,background="light blue",command=equateEqu).grid(column=3,row=4)
clear = Button(frame,text="Clear",height=h,width=w+10,font=40,background="orange",command=clearEqu).grid(column=0,row=4,columnspan=2)
# Main loop running the app
root.mainloop()