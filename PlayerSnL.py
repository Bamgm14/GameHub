import random as r
import os
from tkinter import *
def Bam(b,d):
    a=open('SnL.py','w+')
    a.write('''import random as r
import time as t
def a(n,q):
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
    print ("Current Position:"+str(sum(n)))\n''')
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
    for x in b:
        a.write('\ta(Players["'+x+'"],"'+x+'")\n')
        a.write('\tif sum(Players["'+x+'"])>=100:\n')
        a.write('\t\tprint("'+x+' Is Winner")\n')
        a.write('\t\tt.sleep(5)\n')
        a.write('\t\tbreak\n')
        a.write('\tt.sleep(1)\n')
    a.close()
    os.system('python SnL.py || python3 SnL.py')
