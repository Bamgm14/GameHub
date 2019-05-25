from tkinter import *
import random as r
z=0
def Dif():
    def z1():
        global z
        z=1
        a.destroy()
    def z2():
        global z
        z=2
        a.destroy()
    def z3():
        global z
        z=3
        a.destroy()
    def z4():
        global z
        z=4
        a.destroy()
    def zr():
        global z
        z=r.randrange(1,5)
        a.destroy()
    a=Tk()
    a.geometry('300x250')
    a.title('Snakes And Ladders')
    g=Label(a,text='Choose Difficulty',font=(10)).pack()
    b=Checkbutton(a,text='Level 1',command=z1).pack()
    c=Checkbutton(a,text='Level 2',command=z2).pack()
    d=Checkbutton(a,text='Level 3',command=z3).pack()
    e=Checkbutton(a,text='Level 4',command=z4).pack()
    f=Checkbutton(a,text='Random Level',command=zr).pack()
    a.mainloop()
    return z
