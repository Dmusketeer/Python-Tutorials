# Draw three squares 
# in a row with a gap 
# between each. Fill 
# them using three 
# different colours. 

import turtle
turtle.shape("turtle")
turtle.color("black","red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()

turtle.forward(200)

turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()

turtle.forward(200)

turtle.color("black","blue")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()

turtle.exitonclick()
