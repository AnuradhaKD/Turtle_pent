import turtle
turtle.bgcolor("black")
colors=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
turtle.speed(0.5)
for i in range(288):
	turtle.pencolor(colors[i%7])
	turtle.pensize(i/88+1)
	turtle.forward(i)
	turtle.left(59)
turtle.done()

#	~AkD~
