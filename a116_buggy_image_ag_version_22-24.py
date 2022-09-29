#   a116_buggy_image.py
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
leg_angle = 200 / legs
#draw legs
spider.pensize(5)
legs_remaining = 0
while (legs_remaining < legs):
  spider.goto(0,0)
  spider.setheading(leg_angle*legs_remaining)
  spider.forward(leg_length)
  legs_remaining = legs_remaining + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
