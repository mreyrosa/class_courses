import turtle
window=turtle.Screen()
turtle=turtle.Turtle()
def straight(x, y):
	turtle.reset()
	turtle.forward(100)
	turtle.right(144)	
	turtle.forward(100)
	turtle.right(144)	
	turtle.forward(100)
	turtle.right(144)	
	turtle.forward(100)
	turtle.right(144)	
	turtle.forward(100)
	turtle.right(144)
turtle.onclick(straight)

run=True
def start():	
#	char=list(main)
#	valid=["c", "C", "e", "E", "l", "L", "i", "I", "f", "F", "h", "H"]
#	if valid[1] or valid[2] or valid[3] or valid[4] or valid[5] or valid[6] or valid[7] or valid[8] or valid[9] or valid[10] or valid[11] or valid[12]:
#	main=str(input("Please choose any of the follwing six letters to see them printed out in ASCII art (C, E, L, I, F, H). Or type 'quit' to leave the loop: "))
	string1=str(len(main))
	list1=list(main)
	i=0

#	main=str(input("Please choose any of the follwing six letters to see them printed out in ASCII art (C, E, L, I, F, H). Or type 'quit' to leave the loop: "))
	turtle.reset()
	for i in range(int(string1)):
		if list1[i]=="c" or list1[i]=="C":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10,0)
			turtle.pendown()
			turtle.forward(100)
			turtle.back(100)
			turtle.right(90)
			turtle.forward(100)
			turtle.left(90)
			turtle.forward(100)
		elif list1[i]=="e" or list1[i]=="E":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10,0)
			turtle.pendown()
			turtle.forward(100)
			turtle.back(100)
			turtle.right(90)
			turtle.forward(50)
			turtle.left(90)
			turtle.forward(100)
			turtle.back(100)
			turtle.right(90)
			turtle.forward(50)
			turtle.left(90)
			turtle.forward(100)
		elif list1[i]=="l" or list1[i]=="L":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10,0)
			turtle.pendown()
			turtle.right(90)
			turtle.forward(100)
			turtle.left(90)
			turtle.forward(50)
		elif list1[i]=="i" or list1[i]=="I":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10, 0)
			turtle.pendown()
			turtle.forward(100)
			turtle.back(50)
			turtle.right(90)
			turtle.forward(100)
			turtle.left(90)
			turtle.back(50)
			turtle.forward(100)
		elif list1[i]=="f" or list1[i]=="F":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10, 0)
			turtle.pendown()
			turtle.forward(100)
			turtle.back(100)
			turtle.right(90)
			turtle.forward(30)
			turtle.left(90)
			turtle.forward(100)
			turtle.back(100)
			turtle.right(90)
			turtle.forward(70)
			turtle.left(90)
			turtle.penup()
			turtle.setposition(turtle.xcor()+100,0)
		elif list1[i]=="h" or list1[i]=="H":
			turtle.penup()
			turtle.setposition(turtle.xcor()+10, 0)
			turtle.pendown()
			turtle.right(90)
			turtle.forward(100)
			turtle.back(50)
			turtle.left(90)
			turtle.forward(50)
			turtle.left(90)
			turtle.forward(50)
			turtle.back(100)
			turtle.right(90)
	i=i+1
while run:	
	main=str(input("Please choose any of the follwing six letters to see them printed out in ASCII art (C, E, L, I, F, H). Or type 'quit' to leave the loop: "))
	if main=="quit":
		break
	start()