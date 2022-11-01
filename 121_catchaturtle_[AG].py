# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
score = 0
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)
#timersetup
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

counter.goto(-250,250)
#makes the scire
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(250,250)

font_setup = ("Arial", 20, "normal")

spot = trtl.Turtle()
spot.penup()
spot_color = "pink"
spot_size = 2
spot_shape = "circle" 
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)
#-----game functions--------
def spot_clicked(x, y):
  if timer_up != True:
    update_score()
    change_position()
  else:
    spot.hideturtle()
    

def change_position():
  new_xpos= rand.randint(-200,200)
  new_ypos = rand.randint(-200,200)
  spot.goto(new_xpos, new_ypos)
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
