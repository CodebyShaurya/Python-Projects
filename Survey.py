def yes():
    mylabel = Label(root,text='Did you like our service').grid(row=2,column=3)
    mylabel = Label(root,text='').grid(row=3,column=0)
    mylabel = Label(root,text='').grid(row=3,column=6)
    myutton = Button(root , text = 'YES',command= yes2).grid(row= 3,column=1)
    mutton = Button(root , text = 'NO',command=no2).grid(row= 3,column=5)
    
def no():
    mylabel = Label(root,text='Okay').grid(row=2,column=3)
def yes2():
    Label(root,text='Thank you').grid(row=4,column=3)
def no2():
    Label(root,text='PLease tell us how can we improve').grid(row=4,column=3)
    global e
    e=Entry(root)
    e.grid(row=5,column=3)
    myuon = Button(root , text = 'Submit',command= sub).grid(row= 6,column=3)
def sub():
    global f 
    f=e.get()
    
                                      




from tkinter import *
root=Tk()




mylabel = Label(root,text='Would you like to give a survey ?').grid(row=0,column=3)

mylabel = Label(root,text='').grid(row=1,column=0)
mylabel = Label(root,text='').grid(row=1,column=6)
mybbutton = Button(root , text = 'YES',command=yes).grid(row= 1,column=1)
mybutton = Button(root , text = 'NO',command=no).grid(row= 1,column=5)
