import time
 
# FUNCTIONS
   
# Instructions on how to play




# Introduce the setting




# Options select
def option_select():
    pass
print("You are escaping the plane and can only choose one thing for a better chance at survival")
time.sleep(1.5)
print ("Will you?")
time.sleep(1)
print ("help a man escape the plane who is still alive but stuck under a seat")
time.sleep(0.7)
print ("Or")
time.sleep(0.7)
print ("leave the man to die and take an emergency survial kit strapped to the wall instead")
time.sleep(1)
start = input("What will it be? Quick! ")
if start == "leave the man to die and take an emergency survial kit strapped to the wall instead":
    print ("You have retieved the emergency survival kit, but you didn't have time to save the man who was stuck.")
    print ("Now quickly, you have to leave!")
    time.sleep(1.5)
    print ("...")
    time.sleep(1.5)
    print ("You have now made it to the island, there are a few hours of daylight left.")
else:
    print ("You successfully helped the man escape, but he now has an injured leg, so you have to help him swim to the closest island.")
    time.sleep(1.5)
    print ("...")
    time.sleep(1.5)
    print ("You have now made it to the island, but it took you twice as long because you had to help the man who is injured.")
    time.sleep(1)
    print = ("It's now getting dark, you have to set up camp before it's too cold.")

# MAIN CODE

