import random as r
import os
from tkinter import *
def Bam(b,d):
    a=open('SnL.py','w+')
    a.write('''import random as r
import Send as s
import time as t
import matplotlib.pyplot as plt
import numpy as np
def Set(n,c=None):
    global Ladders
    global Snakes
    global Players
    a={}
    plt.grid()
    plt.axis([-1,10,-1,10])
    plt.xticks(np.arange(-1, 10, step=1))
    plt.yticks(np.arange(-1, 10, step=1))
    for x in Ladders:
        Alg(x,'g*')
    for x in Snakes:
        Alg(x,'r*')
    for x in n:
        Alg(sum(Players[x]),'bo')
    plt.show()
    for x in n:
        a[x].remove()
def Alg(n,a):
    y=n//10
    x=n%10
    plt.plot(x,y,a)
def BikesAndTrucks(n,q):
    global Ladders
    global Snakes
    a=r.randrange(1,7)
    print ("Player "+str(q)+" Moved "+str(a))
    n.append(a)
    b=r.randrange(1,11)
    if sum(n) in Snakes:
        print ("Oh No... The Snake Got You... Move "+str(b)+" Backward!!")
        n.append(-b)
    b=r.randrange(1,11)
    if sum(n) in Ladders:
        print ("Yay... You Found A Ladder... Move "+str(b)+" Forward!!")
        n.append(b)
    if sum(n)<0:
        n.append((-1)*sum(n))
    print ("Current Position:"+str(sum(n)))
def Standard(Player):
    BikesAndTrucks(Players[Player],Player)
    if sum(Players[Player])>=100:
        print(Player+" Is Winner")
        t.sleep(5)
        break
    t.sleep(1)
def Loop(textbox=None,driver=None):
    global Players
    count=0
    while True:
        count+=1
        for x in list(Players.keys()):
            flag=Standard(textbox,x)
            if flag==1:
                break
        Set(Players,count)
        t.sleep(10)
        if flag==1:
            break\n''')
    Snakes=[]
    Ladders=[]
    while len(Snakes)!=(d*5) or len(Ladders)!=(d*5):
        e=r.randrange(1,100)
        if (e not in Snakes) and (len(Snakes)!=(d*5)):
            Snakes.append(e)
        if (e not in Snakes) or (e not in Ladders) and (len(Ladders)==(d*5)):
            Ladders.append(e)
    a.write('Snakes='+str(Snakes)+'\nLadders='+str(Ladders)+'\n')
    a.write('Players={')
    for x in b:
        a.write('"'+x+'":[],')
    a.write('}\nwhile True:\n')
    a.write('Loop(Players)')
    a.close()
    os.system('python SnL.py || python3 SnL.py')
