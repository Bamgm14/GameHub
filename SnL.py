import random as r
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
    print ("Current Position:"+str(sum(n)))
Snakes=[33, 29, 26, 24, 98, 18, 67, 89, 8, 11, 94, 25, 76, 42, 68]
Ladders=[64, 78, 87, 21, 56, 51, 4, 9, 90, 91, 30, 13, 21, 80, 90]
Players={"Hello":[],"23o":[],}
while True:
	a(Players["Hello"],"Hello")
	if sum(Players["Hello"])>=100:
		print("Hello Is Winner")
		t.sleep(5)
		break
	t.sleep(1)
	a(Players["23o"],"23o")
	if sum(Players["23o"])>=100:
		print("23o Is Winner")
		t.sleep(5)
		break
	t.sleep(1)
