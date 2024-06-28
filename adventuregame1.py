import time
 
# FUNCTIONS
   
# Instructions on how to play
def instructions():
print ("How to play") 
time.sleep(3) 
print ("You will have to make decisions with the multiple options you are given,some options will be good and help you survive on the island, other options will be bad and if you pick too many you can die. Your objective is to make it of the island alive.")
time.sleep(3)


# Introduce the setting
def setting():
    time.sleep(3) # wait 3 seconds
    print("*Alarm sounds*")
    time.sleep(3) # wait 3 seconds
    print("*muffled dialouge comes out the speakers*")
    time.sleep(3) # wait 3 seconds
    print("Brace for impact - says the Pilot")
    time.sleep(3) # wait 3 seconds
    print(". . . ")
    time.sleep(3) # wait 3 seconds
    print("The plane has crashed")
    time.sleep(2) # wait 2 seconds
    print("your ears are ringing")
    time.sleep(1.5) # wait 1.5 seconds
    print("you have to get up and escape before the plane sinks")



# Option select
def option_select():
    
    print("You are escaping the plane and can only choose one thing for a better chance at survival")
    time.sleep(3.5)
    print ("Will you?")
    time.sleep(3.5)
    print ("help a man escape the plane who is still alive but stuck under a seat")
    time.sleep(3)
    print ("Or")
    time.sleep(2.75)
    print ("leave the man to die and take an emergency survial kit strapped to the wall instead")
    time.sleep(3.5)
    start = input("What will it be, help the man(a) or take the kit?(b) Quick! ")
    if start == "b":
        print ("You have retieved the emergency survival kit, but you didn't have time to save the man who was stuck.")
        time.sleep(1)
        print ("Now quickly, you have to leave!")
        time.sleep(3.5)
        print ("...")
        time.sleep(3.5)
        print ("You have now made it to the island, there is still about an hour of daylight left...")
        option_select2()
    elif start == "a":
        print ("You successfully helped the man escape, but he now has an injured leg, so you have to help him swim to the closest island.")
        time.sleep(3.5)
        print ("...")
        time.sleep(3.5)
        print ("You have now made it to the island, but it took you twice as long because you had to help the man who is injured.")
        time.sleep(3.5)
        print = ("It's now getting dark, you have to set up camp before it's too cold.")
        option_select3()
    else:
        print ("Invalid response! The plane is sinking too quickly!")
        time.sleep(2.5)
        print ("You have drowned")
        quit()

# chose to take the kit
def option_select2():
    print ("You don't have too long until it will start to get dark, and when it gets dark it will be very, very cold.")
    time.sleep(2.5)
    print ("Now you have to make a descision before it gets too dark.")
    time.sleep(3.5)
    print ("You have thought of going back to where the plane sunk in search of reasorces that are floating on the surface which will make survival alot easier.")
    print ("However you are worried that it might get too dark and you won't be able to make your way back in time.")
    time.sleep(2)
    print ("The survival part of your brain is telling you to stay and build a small shelter and fire for the night closely approaching.")
    scenario2 = input ("What will do you? Go back to the plane(a) or stay and make a shelter and fire for the night?(b) ")
    if scenario2 == "a":
        print ("You have started swimming back in the direction of the plane")
        time.sleep(3.5)
        print ("...")
        time.sleep(2.5)
        print ("You have managed to grab two suitcases foating on the surface, and start to swim back to the island with them dragging beside you on the surface.")
        print ("The sun is starting to set however, and you aren't even half way back to the island, the water is starting to become freezing, and your muscles are fatiged.")
        time.sleep(2.5)
        print ("You notice you head is dipping below the surface, you are starting to become very tired and cold.")
        time.sleep(2.5)
        print ("...")
        time.sleep(2.5)
        print ("All of a sudden you feel an array of sharp teeth bite your foot, then drag you under the water, you can't fight back, its the end...")
        print ("You have been eaten by a shark")
        time.sleep(3.5)
        quit()
    elif scenario2 == "b":
        print("You start looking around for fallen tress to make a shelter for the night")
        time.sleep(2.5)
        print ("30 minutes later you have a small makeshift shelter, and now you start working on a fire for warmth.")
        time.sleep(3)
        print ("You have managed to make a friction fire with some dead branches and sticks, the fire has been constantly burning for a while now into the night, so you lay down on your side to try and get some rest for tomorrow")
        time.sleep(3)
        print ("...")
        time.sleep(3)
        print ("You wake up to a bright beam of sunlight in your face.")
        time.sleep(2)
        print ("The fire has gone out now and only a small amount of smoke remains rising from the ground.")
        time.sleep(3.5)
        print ("wait...")
        time.sleep(2.5)
        print ("Do you hear that?")
        time.sleep.(2)
        print ("It sounds like a plane in the distance!")
        time.sleep(2.5)
        print ("Hold on a second..")
        time.sleep (2.5)
        print ("It's a small water plane flying right towards the island!")
        time.sleep(2)
        print ("Quick, you have to draw attention so they see you!")
        option_select4()
    else:
        print ("Invalid response, what were you thinking?")
        time.sleep(3.5)
        quit()


# chose to save the man
def option_select3():
    print ("...")

def option_select4():
    scenario3 = input ("You have to do something! (a)run to the beach, throw sand around, jump, and yell, or (b)try and start the fire real quick so the smoke is seen") 
    if scenario3 == "a"
        print ("You run down to the beach, yelling, jumping, and throwing sand around in the air")
        time.sleep(3)
        print ("The plane continues to fly past, devistated you collapse on the sand and wonder what to do next")
        time.sleep(3.5)
        print ("...")
        time.sleep(3.5)
        print ("Wait, you hear the plane comes back, you stand up and see it descenting towards the water on your side of the beach")
        time.sleep(3)
        print ("Here!! You shout. The pilot has come to save you")
        time.sleep(3.5)
        print ("Congratulations!!! You have been Saved, and Won the Game!!!")
        time.sleep(4)
        quit()
    elif scenario3 == "b"
        print ("You manage to light the fire, but it is still only very small, and there is not much smoke, so you try and shout out..")
        time.sleep(3.5)
        print ("You failed to get their attention")
        print ("That was your only hope, now days have gone past and you have had no food or water")
        time.sleep(3)
        print ("On the 6th day you die eating some poisonous berries from a bush")
        quit()
    else:
        print ("Invalid response, come on! What were you thinking now the plane flew past.")
        time.sleep(2.5)
        print ("Unfortunatly while you were daydreaming you were eaten by a wild hog")
        quit()

# MAIN CODE
 option_select()
 