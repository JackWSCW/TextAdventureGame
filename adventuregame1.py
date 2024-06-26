import time
 
# FUNCTIONS
   
# Instructions on how to play




# Introduce the setting




# Options select
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
    start = input("What will it be, help the man or take the kit? Quick! ")
    if start == "take the kit":
        print ("You have retieved the emergency survival kit, but you didn't have time to save the man who was stuck.")
        time.sleep(1)
        print ("Now quickly, you have to leave!")
        time.sleep(3.5)
        print ("...")
        time.sleep(3.5)
        print ("You have now made it to the island, there are still a few hours of daylight left...")
        option_select2()
    if start == "help the man":
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

#choose to take kit
def option_select2():
    pass

#choose to save man 
def option_select3():
    
    print("you get wood near by and start making a fire")
    time.sleep(2)
    print("injured man asks you if he should build a shelter for the night")
    screnio3 = input ("yes he should(a),no hes injured(b)")
    if screnio3=="a".upper:
        print("he attemps to build the shelter but falls into a prickly bush and fails to build the shelter.")
        time.sleep(4) 
        print("you pull him out the bush and he terribly injured")
        time.sleep(4)
        print("your really tired so you grabs some big leafs and cover yourself and the injured man and go to sleep")
    elif screnio3=="b".upper:
        print("you finish the fire and after work on making a shelter")
        time.sleep(3)
        print("an hour goes by and your really tried but you finish building a shelter and go to sleep" )
    else:
        print ("Invalid response! you fall and hit your head on a rock!")
        time.sleep(2)
        print ("You have dead")
        quit()


# MAIN CODE