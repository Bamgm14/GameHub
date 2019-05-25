import os
from tkinter import *
import SetUpSnL as SUSL
SnLad='Trucks And Bikes'
def rot():
    global root,SnLad
    root=Tk()
    root.title('Game Chooser')
    root.geometry('250x200')
    Title=Message(root,text='Games',font=("Times", 15, "bold")).pack()
    SnL=Checkbutton(root,text=SnLad,command=snl).pack()
    O_E=Checkbutton(root,text='Odd Or Even').pack()
    Bull=Checkbutton(root,text='Bull').pack()
    root.mainloop()
def snl():
    global root,SnLad,SnaL
    root.destroy()
    SnaL=Tk()
    SnaL.title(SnLad)
    Head=Message(SnaL,text=SnLad,font=("Times", 15, "bold")).pack()
    Explain1=Message(SnaL,text='').pack()
    N=Button(SnaL,text='No',command=rotS).pack()
    Y=Button(SnaL,text='Yes',command=snl1).pack()
def snl1():
    global SnaL
    SnaL.destroy()
    SUSL.snl(SnLad)
def rotS():
    global SnaL
    SnaL.destroy()
    rot()
try:
    rot()
except:
    print ('Error')
    
