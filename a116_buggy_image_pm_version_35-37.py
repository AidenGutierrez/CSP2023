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
leg_length = 100
leg_angle = 140 / legs
#draw legs
spider.pensize(5)
remaining = 4
while (remaining < legs):
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(leg_angle*remaining)
  spider.circle(-leg_length,50)
  spider.penup()
  remaining = remaining + 1
remaining = 4
    

while (remaining < legs):
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(leg_angle*remaining-180)
  spider.circle(leg_length,50)
  spider.penup()
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
