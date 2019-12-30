from tkinter import *
import tkinter.font

main = tkinter.Tk()
main.title("Calculator")
Input=""

main.configure(bg="whitesmoke")

variable = StringVar()

new_font = tkinter.font.Font(size=36)

def btnpress(number):
    global Input
    Input = Input + str(number)
    variable.set(Input)
    
def clear():
    global Input
    Input=""
    variable.set("")
   
def equal():
    try:
        global Input
        total = str(eval(Input))
        variable.set(total)
        Input = total
    except:
        variable.set("error")
        Input = ""

entry = Entry(main,textvariable=variable,justify=RIGHT,width=10,font=new_font,bg="lightgrey")
entry.grid(columnspan=4)

btn1 = Button(main,text="1",command=lambda:btnpress(1), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn1.grid(row=4,column=0)

btn2 = Button(main,text="2",command=lambda:btnpress(2), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn2.grid(row=4,column=1)

btn3 = Button(main,text="3",command=lambda:btnpress(3), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn3.grid(row=4,column=2)

btn4 = Button(main,text="4",command=lambda:btnpress(4), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn4.grid(row=3,column=0)

btn5 = Button(main,text="5",command=lambda:btnpress(5), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn5.grid(row=3,column=1)

btn6 = Button(main,text="6",command=lambda:btnpress(6), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn6.grid(row=3,column=2)

btn7 = Button(main,text="7",command=lambda:btnpress(7), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn7.grid(row=2,column=0)

btn8 = Button(main,text="8",command=lambda:btnpress(8), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn8.grid(row=2,column=1)

btn9 = Button(main,text="9",command=lambda:btnpress(9), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn9.grid(row=2,column=2)

btnadd = Button(main,text="+",command=lambda:btnpress("+"), height=1, width=2,bd=4,bg="deepskyblue",font=new_font)
btnadd.grid(row=2,column=3)

btnsub = Button(main,text="-",command=lambda:btnpress("-"), height=1, width=2,bd=4,bg="deepskyblue",font=new_font)
btnsub.grid(row=3,column=3)

btnmul = Button(main,text="*",command=lambda:btnpress("*"), height=1, width=2,bd=4,bg="deepskyblue",font=new_font)
btnmul.grid(row=4,column=3)

btndiv = Button(main,text="/",command=lambda:btnpress("/"), height=1, width=2,bd=4,bg="deepskyblue",font=new_font)
btndiv.grid(row=5,column=3)

btnclear = Button(main,text="C",command=lambda:clear(), height=1, width=2,bd=4,bg="royalblue",font=new_font)
btnclear.grid(row=5,column=0)

btn0 = Button(main,text="0",command=lambda:btnpress(0), height=1, width=2,bd=4,bg="skyblue",font=new_font)
btn0.grid(row=5,column=1)

btnequal = Button(main,text="=",command=lambda:equal(), height=1, width=2,bd=4,bg="royalblue",font=new_font)
btnequal.grid(row=5,column=2)

main.mainloop()