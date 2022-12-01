#Group Name Generator
import random
import os

def randomizer(words):
    word1 = random.choice(words)
    word2 = random.choice(words)
    if(word2 == word1):
        word2 = random.choice(words)
        
    print("Your new team name is: "+ word1 + " " + word2)

def quiz(words):
    org = input("What's the acronym of your school/organization?\n")
    if (org[-1] in vowels):
        org = org + "cian"
    else:
        org = org + "ian"
    words.append(org)
    words.append(input("What's your favorite color?\n"))
    words.append(input("What's one word to describe yourself?\n"))
    words.append(input("Give me one adjective?\n"))
    words.append(input("Give me another adjective?\n"))
    words.append(input("What's your go-to beverage?\n"))
    words.append(input("What's your comfort food?\n"))
    words.append(input("What's your spirit animal?\n"))
    words.append(input("What's your biggest fears?\n"))
    words.append(input("Give me a fantasy creature?\n"))

words = []
choice = "Y"
vowels = ['a','i','u','e','o','A','I','U','E','O']
i = 0

print("Welcome to the Tech Group Generator")
quiz(words)

while (i == 0):
    if (choice == 'Y' or choice == 'y'):
        randomizer(words)
    else: 
        break
    
    choice = input("\nDo you want a new name? [Y/N]\n")
    os.system('CLS')
    
    
