#\n
import time
points = 0
health = 100

print("Hello, welcome to the rainforest. Have fun exploring but beware of what lurks in the shadows.")
name = input("What is your name, fellow adventurer?")
def intro(name):
    return "Nice to meet you, " + name
print(intro(name))
print("Now it's time to choose your tools and companians for you journey.")
pet = input("Do you want any pets? Your options are a dog, cat, rabbit, or horse. If yes, type the name of the animal you want out of the options. If not, answer No.")
pet = pet.lower()
pet = pet.replace(" ", "")
while pet not in ["dog","cat","rabbit","horse"]:
    pet = input("Sorry, I didn't understand that. Make sure you type the name of the animal (dog, horse, cat, or rabbit) without any spelling errors. If you didn't want a pet, please type 'no'")

if pet == "dog":
        petname = input("What is the name of your dog?")
elif pet == "cat":
        petname = input("What is the name of your cat?")
elif pet == "rabbit":
        petname = input("What is the name of your rabbit?")
elif pet == "horse":
        petname = input("What is the name of your horse?")
elif pet == "no":
        print("Okay, brave choice. You will be going solo this adventure.")

tools = input("Do you want any tools? You options are a bow and arrow for fighting and hunting (you can only use it six times until you find more arrows and it has the farthest range), a machette to cut through trees or in fights (it can be used infinite times, but only for close distance), or a slingshot using rocks anywhere you go (so it can be used infinite times, but it will do less damage). If you want a tool, write the name of the tool. If not, answer 'no'.")
tools = pet.lower()
tools = pet.replace(" ", "")
while tools != "bow and quiver" or "machette" or "slingshot":
    if tools == "bow and quiver":
       print("congrats, you got your bow and arroew")
    elif tools == "machette":
        print("congrats you have a machette")
    elif tools == "slingshot":
        print("congrats, you have a slingshot")
    elif tools == "no":
        print("Okay, brave choice. You will be going without any tools on this adventure. Good luck surviving.")
    else:
        print("Sorry, I didn't understand that. Make sure you type the name of the tool (bow and arrow, machette, or slingshot) without any spelling errors. If you didn't want a tool, please type 'no'")

time.sleep(2)


obstacle_1 = input("Oh no, you've reached a bear in the path. Do you want to try to fight it or hide? (for hide - type hide and for fight - type fight")
if obstacle_1 == "hide":
    print("congrats, you survived by hiding.")
    points = points+1
elif obstacle_1 == "fight":
    print("oh, no the bear was too strong. you lost 5 health!")
    health = health-5
else:
    print("sorry, you reacted wrong. you lost 10 health")
    health = health+5
