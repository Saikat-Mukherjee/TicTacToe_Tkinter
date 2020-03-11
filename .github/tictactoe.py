from tkinter import *
from functools import partial
global player

def action(b):
	global player
	print("Turn : Player "+str(player))
	if b.get() == "X" or b.get() == "O":
		return
	if player == 1:
		b.set("X")
		win_lose()
		player = 2
	else:
		b.set("O")
		win_lose()
		player = 1
	Tie()
	
def win_lose():
	global player
	print("Dhukche")
	for i in range(0,7,3):
		if bt[i].get() == bt[i+1].get()  and bt[i+1].get() == bt[i+2].get() and (bt[i].get() == 'X' or bt[i].get()=='O'):
			print("player" +str(player)+ " Win !! ")
			exit()
			return
	for i in range(3):
		if bt[i].get() == bt[i+3].get()  and bt[i+3].get() == bt[i+6].get() and (bt[i].get() == 'X' or bt[i].get()=='O'):
			print("player" +str(player)+ " Win !! ")
			exit()
			return
	if bt[0].get() == bt[4].get()  and bt[4].get() == bt[8].get() and (bt[0].get() == 'X' or bt[0].get()=='O'):
		print("player" +str(player)+ " Win !! ")
		exit()
		return
	if bt[2].get() == bt[4].get()  and bt[4].get() == bt[6].get() and (bt[2].get() == 'X' or bt[2].get()=='O'):
		print("player" +str(player)+ " Win !! ")
		exit()
		return
def Tie():
	global player
	x = 0
	for i in range(9):
		if bt[i].get() == 'X' or bt[i].get() == 'O':
			x = x + 1
	print(x)
	if x == 9:	
		print("There is a Tie")
		exit()
			
lay = Tk()
lay.geometry("200x200")
lay.title("Tic Tac Go ")
frame1 = Frame(lay,bd = 2,height = 100,width = 100).place(x = 0,y= 0)
#act = partial(action,b1)
bt = []
for i in range(9):
	b = StringVar()
	bt.append(b)
player = 1

b1 = Button(frame1,text = "X",textvariable = bt[0],command = lambda : action(bt[0]),height = 2,width = 2).place(x = 0,y = 0)
b2 = Button(frame1,text = "X",textvariable = bt[1],command = lambda : action(bt[1]),height = 2,width = 2).place(x = 35,y = 0)
b3 = Button(frame1,text = "X",textvariable = bt[2],command = lambda : action(bt[2]),height = 2,width = 2).place(x = 70,y = 0)
b4 = Button(frame1,text = "X",textvariable = bt[3],command = lambda : action(bt[3]),height = 2,width = 2).place(x = 0,y = 35)
b5 = Button(frame1,text = "X",textvariable = bt[4],command = lambda : action(bt[4]),height = 2,width = 2).place(x = 35,y = 35)
b6 = Button(frame1,text = "X",textvariable = bt[5],command = lambda : action(bt[5]),height = 2,width = 2).place(x = 70,y = 35)
b7 = Button(frame1,text = "X",textvariable = bt[6],command = lambda : action(bt[6]),height = 2,width = 2).place(x = 0,y = 70)
b8 = Button(frame1,text = "X",textvariable = bt[7],command = lambda : action(bt[7]),height = 2,width = 2).place(x = 35,y = 70)
b9 = Button(frame1,text = "X",textvariable = bt[8],command = lambda : action(bt[8]),height = 2,width = 2).place(x = 70,y = 70)
#frame2 = Frame(lay,bd = 5,height = 10,width = 10).place(x = 10,y= 10)
lay.mainloop()
