# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#-----game configuration----
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
#score configuration
score = 0
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)
#timersetup
font_setup = ("Arial", 20, "normal")
timer = 5
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
    manage_leaderboard()
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


counter.goto(-250,250)
#makes the score
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
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
#onclick settings
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
