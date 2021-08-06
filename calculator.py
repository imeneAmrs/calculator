
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar, ttk
from tkinter.constants import BOTH, BOTTOM, RIDGE, RIGHT, TOP, YES
win = tk.Tk()          #create instance
win.geometry("350x450")
win.resizable(0, 0)    #prevent window from been resized
win.title("calculator")

txt = StringVar()
expression = ""
#function to update expression in the text entry box
def click(num):
    global expression
    numbers = [1,2,3,4,5,6,7,8,9]
    if(expression == "0") and (num == 0): #prevent the repitition of zero
        expression = "0"
    elif(expression == "0" and num in numbers): #avoid 0 in the begining of expression
        expression = str(num)
    else:  
        expression = expression + str(num) #concatenate the strings
    txt.set(expression) #update the expression

#
def equal():
    try:
        global expression
        result = str(eval(expression)) #eval function evaluate the expression
        txt.set(result)
        expression = result
    except:
        expression.set("Error")
        expression = ""

#function that clear individual entry
def clr():
    global expression
    length = len(txt.get())
    e1.delete(length-1, 'end')
    expression = e1.get()
    txt.set(e1.get())

def clearAll():
    global expression
    expression = ""
    txt.set("")

#creating frames
frame1 = Frame(win, width=390 ,height=100 ,bg="white")
frame1.pack(side=TOP)
frame2 = Frame(win, width=390 ,height=368 ,bg="white")
frame2.pack(side=BOTTOM)

#creating a label
l1 = Label(frame1, text= "Basic Calculator" ,font=("Arial Bold", 20))
l1.pack(side=TOP, expand=YES)
#creating an entry field
e1 = Entry(frame1, textvariable=txt , width=30 , bd=10, font=("Arial Bold", 12),
     fg="black", bg="white", relief=RIDGE, justify=RIGHT)
e1.pack(side=TOP)
e1.insert(0,"0")

#creating buttons
b1 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(7), text="7", font=("Courier New",16,'bold'))
b1.place(x=5, y=10)

b2 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(4), text="4", font=("Courier New",16,'bold'))
b2.place(x=5, y=81)

b3 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(1), text="1", font=("Courier New",16,'bold'))
b3.place(x=5, y=152)

b4 = Button(frame2, padx=48, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(0), text="0", font=("Courier New",16,'bold'))
b4.place(x=5, y=223)

b5 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(8), text="8", font=("Courier New",16,'bold'))
b5.place(x=72, y=10)

b6 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(5), text="5", font=("Courier New",16,'bold'))
b6.place(x=72, y=81)

b7 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(2), text="2", font=("Courier New",16,'bold'))
b7.place(x=72, y=152)

b8 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click("."), text=".", font=("Courier New",16,'bold'))
b8.place(x=139, y=223)

b9 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(9), text="9", font=("Courier New",16,'bold'))
b9.place(x=139, y=10)

b10 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(6), text="6", font=("Courier New",16,'bold'))
b10.place(x=139, y=81)

b11 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click(3), text="3", font=("Courier New",16,'bold'))
b11.place(x=139, y=152)

b12 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click("+"), text="+", font=("Courier New",16,'bold'))
b12.place(x=205, y=10)

b13 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click("-"), text="-", font=("Courier New",16,'bold'))
b13.place(x=205, y=81)

b14 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click("*"), text="*", font=("Courier New",16,'bold'))
b14.place(x=205, y=152)

b15 = Button(frame2, padx=14, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=lambda:click("/"), text="/", font=("Courier New",16,'bold'))
b15.place(x=205, y=223)

b16 = Button(frame2, padx=14, pady=48, bd=4, fg="white", bg='#2F2D2D',
            command=clr, text="CE", font=("Courier New",16,'bold'))
b16.place(x=270, y=10)

b17 = Button(frame2, padx=153, pady=14, bd=4, fg="white", bg='#2F2D2D',
            command=equal, text="=", font=("Courier New",16,'bold'))
b17.place(x=5, y=294)

b18 = Button(frame2, padx=14, pady=48, bd=4, fg="white", bg='#2F2D2D',
            command=clearAll, text="CA", font=("Courier New",16,'bold'))
b18.place(x=270, y=152)

win.mainloop()
