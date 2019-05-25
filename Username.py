
from tkinter import *
import os
m=0
b=[]
w=None
def UN(User,Title):
    global z
    def callback():
        b=None
        global z
        z.destroy()
    a=User
    def Van():
        global b
        global m
        global w
        if m<User:
            m+=1
            y.configure(text='Player '+str(m))
            w=Entry(z)
            w.grid(row=0,column=1)
            v.configure(text='Enter',command=Can)
        else:
            z.destroy()
    def Can():
        global b
        c=str(w.get())
        if c!='' and (c not in b):
            c.replace(' ','_')
            b.append(c)
            Van()
    z=Tk()
    z.protocol("WM_DELETE_WINDOW", callback)
    z.title(Title)
    y=Label(z,text='Start',font=(10))
    y.grid(row=0,column=0)
    v=Button(z,text='Continue',command=Van)
    v.grid(row=1,column=0)
    z.mainloop()
    return b
Count=UN(1,'Gay')
if Count==None:
    print ('Yes')
print (Count)
