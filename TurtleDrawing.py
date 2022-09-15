import turtle as trtl


painter = trtl.Turtle()
color = input("Chose a shell color")

painter.pensize(7)

painter.pencolor(color)
painter.fillcolor(color)

painter.penup()

painter.goto(-40,1)

painter.pendown()
painter.begin_fill()
painter.circle(-80)
painter.end_fill()

painter.penup()
painter.goto(-120,-120)

color= input("Chose a head color")
painter.fillcolor(color)
painter.pencolor(color)
painter.pendown()
painter.begin_fill()
painter.circle(40)
painter.end_fill()

painter.penup()
painter.pencolor("black")
painter.goto(-80,-80)
painter.pendown()
painter.forward(120)
wn=trtl.screen()
wn.mainloop()
