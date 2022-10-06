#Challenge 1:  Write a program that asks the user to input their age 
#in years and tells them: 
#a)How many days they have been alive. 
#b)How many decades they have been alive. 
#c)How many weeks they have been alive. 
#d)How many minutes they have been alive.

age = int(input("How old are you?"))
days = age * 365
decades = age / 10
weeks = days / 7
minutes = (days * 24)*60
print("you are,",age, "years old. You are,", days,"days old.", "{:.1f}".format(decades), "Decades old.", 
round(weeks), "Weeks old, and",
 minutes,"Minutes old.")
