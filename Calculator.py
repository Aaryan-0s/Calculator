from tkinter import  *


#making the canvas
root= Tk()
root.title("                                            Calculator")
root.geometry("436x458")
root.resizable(0,0)
root.config(bg="black")
root.iconbitmap("img2.ico")

#making the place for entering the numbers
e=Entry(root,width=30,borderwidth=5,bg="blue",fg="white",border=0,font="times",justify="right")
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=10)

#adding a function

def button_num(value):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(value))

def clear():
    e.delete(0,END)

def mult():
    mult_value=0
    mult_value=e.get()
    global mult_value1
    global math
    mult_value1=float(mult_value)
    math="mult"
    e.delete(0,END)

def sub():
    sub_value=0
    sub_value=e.get()
    global sub_value1
    global math
    sub_value1=float(sub_value)
    math="sub"
    e.delete(0,END)

def add():
    add_value=0
    add_value=e.get()
    global add_value1
    global math
    add_value1=float(add_value)
    math="add"
    e.delete(0,END)

def div():
    div_value=0
    div_value=e.get()
    global div_value1
    global math
    div_value1=float(div_value)
    math="div"
    e.delete(0,END)



def equal():
    next_value=0
    next_value=float(e.get())
    e.delete(0,END)
    global final_value
    if math=="add":
        final_value=next_value+add_value1
        e.insert(0,final_value)
    elif math=="sub":
        final_value=next_value-sub_value1
        e.insert(0,final_value)
    elif math=="mult":
        final_value=next_value*mult_value1
        e.insert(0,final_value)
    elif math=="div":
        final_value=div_value1/next_value
        e.insert(0,final_value)




#defining the number buttons
button1=Button(root,text="1",fg="#F5F50E",command=lambda:button_num(1),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button2=Button(root,text="2",fg="#F5F50E",command=lambda:button_num(2),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button3=Button(root,text="3",fg="#F5F50E",command=lambda:button_num(3),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button4=Button(root,text="4",fg="#F5F50E",command=lambda:button_num(4),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button5=Button(root,text="5",fg="#F5F50E",command=lambda:button_num(5),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button6=Button(root,text="6",fg="#F5F50E",command=lambda:button_num(6),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button7=Button(root,text="7",fg="#F5F50E",command=lambda:button_num(7),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button8=Button(root,text="8",fg="#F5F50E",command=lambda:button_num(8),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button9=Button(root,text="9",fg="#F5F50E",command=lambda:button_num(9),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
button0=Button(root,text="0",fg="#F5F50E",command=lambda:button_num(0),bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground='#f90749',activeforeground="white")
#defining the operaters
button_sub=Button(root,text="-",fg="#F5F50E",command=sub,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#07d8f9")
button_div=Button(root,text="/",fg="#F5F50E",command=div,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#07d8f9")
button_add=Button(root,text="+",fg="#F5F50E",command=add,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#07d8f9")
button_mult=Button(root,text="x",fg="#F5F50E",command=mult,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#07d8f9")
button_equal=Button(root,text="=",fg="#F5F50E",command=equal,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#aa9191")
button_clear=Button(root,text="CC",fg="#F5F50E",command=clear,bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#b707f9")
button_dot=Button(root,text=".",fg="#F5F50E",bg="black",font=("ALGERISN"),relief=GROOVE,border=1,activebackground="#07d8f9",command=lambda:button_num("."))





#adding the buttons
button1.grid(row=1,column=0,ipadx=40,ipady=20)
button2.grid(row=1,column=1,ipadx=40,ipady=20)
button3.grid(row=1,column=2,ipadx=40,ipady=20)
button4.grid(row=2,column=0,ipadx=40,ipady=20)
button5.grid(row=2,column=1,ipadx=40,ipady=20)
button6.grid(row=2,column=2,ipadx=40,ipady=20)
button7.grid(row=3,column=0,ipadx=40,ipady=20)
button8.grid(row=3,column=1,ipadx=40,ipady=20)
button9.grid(row=3,column=2,ipadx=40,ipady=20)
button0.grid(row=4,column=1,ipadx=40,ipady=20)
button_sub.grid(row=5,column=2,ipadx=42,ipady=20)
button_dot.grid(row=4,column=0,ipadx=42,ipady=20)
button_div.grid(row=4,column=2,ipadx=42,ipady=20)
button_add.grid(row=5,column=0,ipadx=39,ipady=20)
button_mult.grid(row=5,column=1,ipadx=41,ipady=20)
button_equal.grid(row=1,column=3,rowspan=4,ipadx=42,ipady=138)
button_clear.grid(row=5,column=3,ipadx=35,ipady=20)









root.mainloop()