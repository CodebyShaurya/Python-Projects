def yes():
    i=0
    Label(screen,text='I Knew it ').grid(row=7,column=1)
    screen.quit()
def no():
        btn.grid_remove()
        x=randrange(20,200)
        y=randrange(30,340)
        btn1=Button(screen,text='NO',command=no)
        btn.place(x=x ,y=y)
        
        
        
from tkinter import *
from random import randrange

    
     





screen=Tk()
screen.geometry('720x350')
screen.title('Dumb Check')
label=Label(screen,text='Are you Dumb ? ').grid(row=1,column=3)
label=Label(screen,text=' ').grid(row=3,column=0)
label=Label(screen,text=' ').grid(row=7,column=10)
Butto=Button(screen,text='YES',command=yes).grid(row=3 ,column=1)
btn=Button(screen,text='NO',command=no)
btn.grid(row=3 ,column=5)
screen.mainloop()
