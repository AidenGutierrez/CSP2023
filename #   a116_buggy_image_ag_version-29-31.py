#   a116_buggy_image.py
from tkinter import END
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
#creates spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#configure legs
legs = 8
leg_length = 120
leg_angle = 140 / legs
#draw legs
spider.pensize(5)
remaining = 4
while (remaining < legs):
  spider.goto(0,20)
  spider.setheading(leg_angle*remaining)
  spider.forward(leg_length)
  remaining = remaining + 1
remaining = 4
    

while (remaining < legs):
  spider.goto(0,20)
  spider.setheading(leg_angle*remaining-180)
  spider.forward(leg_length)
  remaining = remaining + 1

spider.penup()
spider.goto(0,40)
spider.fillcolor("white")

for i in range (2):
  spider.begin_fill()
  spider.pendown
  spider.color("white")
  spider.circle(5)
  spider.end_fill()
  spider.penup()
  spider. goto(0,0)





spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
