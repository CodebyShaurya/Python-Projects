def butt_select(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current+str(num))

def add():
    global y,fun
    fun='+'
    y=e.get()
    e.delete(0,END)

def sub():
    global y,fun
    fun='-'
    y=e.get()
    e.delete(0,END)

def mul():
    global y,fun
    fun='*'
    y=e.get()
    e.delete(0,END)

def div():
    global y,fun
    fun='/'
    y=e.get()
    e.delete(0,END)

def equal():
    dic={'+':int(e.get())+int(y),'-':int(y)-int(e.get()) , '*':int(e.get())*int(y), '/':int(y)/int(e.get())}
    e.delete(0,END)
    e.insert(0,dic[fun])

def clear():
    e.delete(0,END)
    y=0
    

    

from tkinter import *
root=Tk()


e =Entry(root,width=35,borderwidth=15)
#BUTTON DEFINING
button1 = Button(root , text = '1',padx=40,pady=20,command=lambda: butt_select(1))
button2 = Button(root , text = '2',padx=40,pady=20,command=lambda: butt_select(2))
button3 = Button(root , text = '3',padx=40,pady=20,command=lambda: butt_select(3))
button4 = Button(root , text = '4',padx=40,pady=20,command=lambda: butt_select(4))
button5 = Button(root , text = '5',padx=40,pady=20,command=lambda: butt_select(5))
button6 = Button(root , text = '6',padx=40,pady=20,command=lambda: butt_select(6))
button7 = Button(root , text = '7',padx=40,pady=20,command=lambda: butt_select(7))
button8 = Button(root , text = '8',padx=40,pady=20,command=lambda: butt_select(8))
button9 = Button(root , text = '9',padx=40,pady=20,command=lambda: butt_select(9))
button0 = Button(root , text = '0',padx=40,pady=20,command=lambda: butt_select(0))
buttonadd = Button(root,text='+',padx=40,pady=20,command=add)
buttonsub = Button(root,text='-',padx=40,pady=20,command=sub)
buttonmul = Button(root,text='x',padx=40,pady=20,command=mul)
buttondiv = Button(root,text='/',padx=40,pady=20,command=div)
buttonequ = Button(root,text='=',padx=40,pady=20,command=equal)
buttoncle = Button(root,text='CLEAR',padx=120,pady=20,command=clear)




#BUTTON SETTING
e.grid(row=0,column=0,columnspan=3)
button1.grid(row= 2,column=0)
button2.grid(row= 2,column=1)
button3.grid(row= 2,column=2)
button4.grid(row= 3,column=0)
button5.grid(row= 3,column=1)
button6.grid(row= 3,column=2)
button7.grid(row= 4,column=0)
button8.grid(row= 4,column=1)
button9.grid(row= 4,column=2)
button0.grid(row= 5,column=0)
buttonadd.grid(row=5, column=1)
buttonsub.grid(row=5 ,column=2)
buttonmul.grid(row=6 ,column=0)
buttondiv.grid(row=6, column=1)
buttonequ.grid(row=6, column=2)
buttoncle.grid(row=7, column=0 , columnspan=4)










