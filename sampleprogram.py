import turtle

# Used to loop until the user desires to view the graph. 
answer = 'y'

while (answer == 'y'):

	# Below code is used to create the x and y axis.
	turtle.right(90)

	turtle.pendown()
	turtle.forward(400)
	turtle.penup()
	turtle.left(180)


	turtle.pendown()
	turtle.forward(800)
	turtle.penup()
	turtle.right(180)


	turtle.pendown()
	turtle.forward(400)
	turtle.left(90)
	turtle.forward(400)
	turtle.left(180)
	turtle.penup()

	turtle.pendown()
	turtle.forward(800)
	turtle.left(180)
	turtle.forward(400)

	turtle.penup()

	# Below code is used to write on graph. 
	turtle.goto(300,300)
	turtle.write("X-AXIS: 400 X 400", font=('Times New Roman', 15, 'normal'))
	turtle.goto(300,280)
	turtle.write("Y-AXIS: 400 X 400", font=('Times New Roman', 15, 'normal'))

	turtle.goto(350,0)
	turtle.write("X-AXIS")


	turtle.goto(0,350)
	turtle.write("Y-AXIS")

	turtle.goto(0,0)


	# Below code is used to get input from user. 
	slope = float(input("Enter the slope of the linear line graph: "))
	ycoordinate = float(input("Enter the y-intercept of the linear line graph: "))

	# Below code is used to write the equation for graph.
	turtle.goto(-350,350)
	turtle.write("Graph for y = "+str(slope)+"* x + "+str(ycoordinate), font=('Times New Roman', 20, 'normal'))
	turtle.goto(0,0)
	
	# Making coordinates with y = mx+c
	xcoordinate1 = 0
	ycoordinate1 = ycoordinate

	xcoordinate2 = -(ycoordinate)/slope
	ycoordinate2 = 0

	xcoordinate3 = -100
	ycoordinate3 = (slope*(-100))+(ycoordinate)


	xcoordinate4 = (300 - (ycoordinate))/slope
	ycoordinate4 = 300
	
	ycoordinate5 = -250
	xcoordinate5 = (ycoordinate5 - (ycoordinate))/slope
	

	# Printing x and y coordinates on the graph. 
	turtle.pendown()
	turtle.goto(xcoordinate1, ycoordinate1)
	turtle.write("("+str(xcoordinate1)+","+str(ycoordinate1)+")")
	turtle.goto(xcoordinate2, ycoordinate2)
	turtle.write("("+str(xcoordinate2)+","+str(ycoordinate2)+")")
	turtle.goto(xcoordinate3, ycoordinate3)
	turtle.write("("+str(xcoordinate3)+","+str(ycoordinate3)+")")
	turtle.goto(xcoordinate4, ycoordinate4)
	turtle.write("("+str(xcoordinate4)+","+str(ycoordinate4)+")")
	turtle.goto(xcoordinate5, ycoordinate5)
	turtle.write("("+str(xcoordinate5)+","+str(ycoordinate5)+")")
	turtle.penup()

	answer = input("Do you want to continue y/n:  ")
	
	# Used to clear the graph tp start a new graph. 
	turtle.reset()
