import time
 
# FUNCTIONS
   
# Instructions on how to play




# Introduce the setting




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
        print ("The sun is starting to set however, and you arn't even half way back to the island, the water is starting to become freezing, and your muscles are fatiged.")
        time.sleep(2.5)
        print ("You notice you head is dipping below the surface, you are starting to become very tired and cold.")
        time.sleep(2.5)
        print ("...")
        time.sleep(2.5)
        print ("All of a sudden you feel an array of sharp teeth bite your foot, then drag you under the water, you can't fight back, its the end...")
        print ("You have been eaten by a shark")
        quit()
    elif scenario2 == "b":
        print("You start looking around for fallen tress to make a shelter for the night")
        time.sleep(2.5)
        print ("30 minutes later you have a small makeshift shelter, and now you start working on a fire.")
    else:
        print ("Invalid response, what were you thinking?")
        quit()


# chose to save the man
def option_select3():
    pass
# MAIN CODE

