import turtle as trtl

wallNumber = 7
wallLength = 40
wallDistance = 17
wallColor = "black"
wallPainter = trtl.Turtle()
wallPainter.color(wallColor)
wallPainter.pensize(5)
wallPainter.hideturtle()
wallPainter.speed(0)
doorGap = 10
    
for walls in range(wallNumber):
    for moves in range(3):
        #begining of loop turns painter
        wallPainter.left(90)
        #gets painter to move a little before creating a door
        wallPainter.forward(10)
        wallPainter.penup()
        wallPainter.forward(doorGap)
        wallPainter.pendown()
        #creates the perpindicular lines
        wallPainter.forward(10)
        wallPainter.right(90)
        wallPainter.forward(wallDistance)
        #moves the pen back to the line
        wallPainter.penup()
        wallPainter.backward(wallDistance)
        wallPainter.left(90)
        #finishes the rest of the wall
        wallPainter.pendown()
        wallPainter.forward(wallLength - (doorGap * 3))
        #increases wall Length
        wallLength += 10

        


wn = trtl.Screen()
wn.mainloop()