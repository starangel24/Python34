start='''
You wake up in a derserted hospital, look outside the window, and see a crowd of people making viscious noises.
You get worried, and have to make a choice between going down the left or right hallway, in order to leave.
Your gut is telling you to take cautious steps.
'''

print (start)

stop= False
print ("Type 'left' to go left or 'right' to go right.")
user_input= input()
while not stop:
    if user_input== "right":
        print ("You decide to go right, and see a wailing baby that's drawing attention to yourself. You want to go further down the hallway, but are conscious of the baby. Type 'take the baby and leave' or 'just leave without the baby'." )
        stop=True
        user_input= input()
        while not stop:
            if user_input== "take the baby and leave":
                print ("Good job, you have a conscience. You see an oncoming intruder with a fascination with the baby, and grabs the baby from you, eating it. You see an opening and run away")
                stop=True
            elif user_input== "just leave without the baby":
                print ("Wow, great job, you just sacrificed a baby. The oncoming intruder sees you with hungry eyes, and decides to eat you.")
    elif user_input== "left":
	print("you decide to go left and run into a bunch of vicious zombie like people. Type 'fight away the zombies' or 'run away?'")
	
	user_input= input()
	while not stop:
	    if user_input== "fight away the zombies":
		print( "the zombie is strongeer so he grabs unto your arm, bites you and you turn into one.")	
                stop=True
	    elif user_input== "run away":
		print( "being very cautious, you run around the hospital making sure not to be seen until you find a safe exit without any vicious looking zombies to leave the hospital. ")
	
