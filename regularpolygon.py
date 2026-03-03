import turtle
import random

#Draw a regular polygon with a given number of sides
#THe pen begins at point (x,y)

def polygon(sides,length,x,y,color):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    for i in range(sides):
        turtle.forward(length)
        turtle.left(360//sides)
    turtle.end_fill()

#Disable rendering to speed up drawing
turtle.hideturtle()
turtle.tracer(0)

for i in range (30):
    polygon(random.randrange(3,11),random.randrange(10,51),random.randrange(-250,251),random.randrange(-250,251),random.choice(("red","green","blue","yellow","cyan","purple")))

turtle.update() #Render image
turtle.exitonclick() #Wait for user mouse's click
    
