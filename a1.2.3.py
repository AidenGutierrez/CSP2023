#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
applelist = []
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
xcor = -300
ycor = 90
for i in range (5):
  apple = trtl.Turtle()
  apple.penup()
  apple.goto (xcor + 100, ycor)
  xcor = xcor + 100
  applelist.append(apple)
drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()
drawer.goto(-30,100)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  for active_apple in applelist:
    active_apple.shape(apple_image)
  wn.update()
def fall():
  apple = applelist.pop()
  xcor = apple.xcor()
  ycor = apple.ycor()
  ycor -= 200
  apple.goto(xcor,ycor)
  apple.hideturtle()
  drawer.clear()
  draw()
x = []
def draw():
  global letters
  letters = [ 'a','s','d','f','g','h','j','k','l']
  global screenletter
  screenletter = rand.choice(letters)
  x.append(screenletter)
  drawer.write(screenletter, font=("Arial", 74, "bold")) 

#-----function calls-----
index = 0
draw_apple(apple)
draw()
wn.onkeypress(fall, screenletter)
wn.listen()
wn.update()
wn.mainloop()
