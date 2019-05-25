from tkinter import *
import PlayerSnL as PSnL
import Username as U
import Difficulty as D
def snl(Name):
    def pla():
        if str(pm.get())!='':
            try:
                a=int(str(pm.get()))
                sl.withdraw()
                User=U.UN(a,Name)
                assert User!=None
                d=D.Dif()
                assert d!=None
                PSnL.Bam(User,d)
                sl.destroy()
            except:
                print (Name)
                sl.deiconify()
                txt.configure(text='Error Occured')
    global root
    global sl
    global a
    sl=Tk()
    sl.title(Name)
    sl.geometry('350x250')
    Pl=Label(sl,text='Number Of Players',font=(10)).pack()
    txt=Label(sl,text='')
    txt.pack()
    pm=Entry(sl)
    pm.pack()
    pl=Button(sl, text='Enter', command= pla).pack()
    sl.mainloop()
