#   a116_ladybug.py
from email.policy import default
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

#creats legs
#configure legs
ladybug.right(90)
legs = 6
leg_length = 60
leg_angle = 140 / legs
#draw legs
ladybug.pensize(5)
remaining = 3
while (remaining < legs):
  ladybug.goto(0, -40) 
  ladybug.setheading(leg_angle*remaining+90)
  ladybug.forward(leg_length)
  remaining = remaining + 1
remaining = 3
    

while (remaining < legs):
  ladybug.goto(0, -40) 
  ladybug.setheading(leg_angle*remaining-90)
  ladybug.forward(leg_length)
  remaining = remaining + 1
# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(79)

# config dots
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
for num_dots in range(2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 35
  ypos = xpos -5



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
