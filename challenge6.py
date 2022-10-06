'''Create a program that asks for 
the number of inial zombies, number of zombies they infect a 
day, and the number of days since Mr. Chatard was infected. This 
program should then print out the number of zombies on that 
given day.'''


print ('''Hello user. 
I hear there has been a Zombie appocolypse. 
Please give me some numbers so I can tell you how many zombies are out there.''')

initial = int(input ("Number of zombies on day one."))
daily = int(input ("How many people do they infect in a day."))
days = int(input ("How long has it been since Mr. Chatard was infected."))



zombies = initial*daily*days

print ("There are currently,", zombies, "outside right now.")

if zombies > 100:
    print("So you probably will not have a chance of surviving this appocolypse...")




