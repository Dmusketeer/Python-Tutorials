# # TURTLE GRAPHICS

"""
->   It is possible to draw using a turtle in Python. By typing in commands 
    and using loops, you can create intricate patterns. Here is how it works. 

->  A turtle will travel along a path that you define, leaving a pen mark behind it. As you control 
    the turtle, the pattern that is left is revealed. To draw the pentagon shown below you would 
    type in the following code. 

"""

import turtle

turtle.shape("turtle")
for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)
turtle.exitonclick()



