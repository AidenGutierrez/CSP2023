import turtle as trtl


painter = trtl.Turtle()
color = input("Chose a shell color")

painter.pensize(7)

painter.pencolor(color)
painter.fillcolor(color)

#shell
painter.penup()

painter.goto(-40,1)

painter.pendown()
painter.begin_fill()
painter.circle(-80)
painter.end_fill()

painter.penup()
painter.goto(-120,-120)

#head
headColor= input("Chose a head color")
painter.fillcolor(headColor)
painter.pencolor(headColor)
painter.pendown()
painter.begin_fill()
painter.circle(40)
painter.end_fill()

#L eye and right eye
painter.pencolor("black")
painter.penup()
painter.goto(-150,-70)
painter.pendown()
painter.circle(5)
painter.penup()
painter.goto(-90,-70)
painter.pendown()
painter.circle(5)

#smile

painter.penup()
painter.goto(-140,-90)
painter.right(90)
painter.pendown()
painter.circle(20,180)

#shell line

painter.penup()
painter.pencolor("black")
painter.goto(-75,-80)
painter.left(-90)
painter.pendown()
painter.forward(115)

#L leg

painter.penup()
painter.goto(-80,-180)
painter.pencolor(color)
painter.fillcolor(color)

painter.begin_fill()
painter.circle(20)
painter.end_fill()

# R leg
painter.penup()
painter.home()
painter.goto(-10,-180)
painter.pendown()
painter.begin_fill()
painter.circle(20)
painter.end_fill()

#sand
painter.penup()
painter.goto(-300,-180)
painter.pendown()
painter.pencolor("brown")
painter.forward(600)



wn=trtl.Screen()
wn.bgcolor("blue")
wn.mainloop()
