#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "orchid"]

for s in turtle_shapes:
    
    t = trtl.Turtle(shape=s)
    t.pensize(5)
    
    color = turtle_colors.pop()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    
    my_turtles.append(t)
    t.end_fill()



#  cordinates

startx = 0
starty = 0
direction = 90 
#looping


for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.setheading(direction)
    t.begin_fill()
    t.right(50)     
    t.forward(60)

    
    #sets next corinate	
    direction = t.heading()
    startx = t.xcor()
    starty = t.ycor()
    

wn = trtl.Screen()
wn.mainloop()
