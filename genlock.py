import random
import string
import json
import os

alphabet = list(string.ascii_lowercase)
digits = list(string.punctuation)

mode = input("Would you like to generate a password or read entries.json? (Stored passwords) [G/R]: ")
if mode == "R":
    if not os.path.exists("entries.json"):
        data = {
        }

        with open("entries.json", "w") as f:
            json.dump(data, f, indent=4)
    
            
    with open("entries.json", "r") as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))

def AddNumbers():
    i = 1
    while i <= 15:
        rand = random.randrange(len(alphabet))
        rand2 = random.randint(0, 9)
        alphabet[rand] = str(rand2)
        i += 1
    AddSpecial()


def AddSpecial():
    i = 0
    while i < 16:
        rand = random.randrange(len(alphabet))
        rand2 = random.randrange(len(digits))
        alphabet[rand] = digits[rand2]
        i += 1


def GenerateLabel():
    if "final_password" in globals() and not mode == "R":
        labelInput = input("Input the name for the label: ")
        with open("entries.json", "r") as f:
            data = json.load(f)
            data[labelInput] = final_password

        with open("entries.json", "w") as f:
            json.dump(data, f, indent=4)    

def GenerateBookEntry():
    if not os.path.exists("entries.json"):
        data = {
        }

        with open("entries.json", "w") as f:
            json.dump(data, f, indent=4)

    if os.path.exists("entries.json") and "final_password" in globals():
        GenerateLabel()


AddNumbers()
final_password = ''.join(alphabet)
GenerateBookEntry()


if not mode == "R":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("== Done ==")
    print("[❕] Warning! Some generated passwords could cause issues in shells/scripts if not escaped!")
    print("[🔐] Final password:", final_password)
