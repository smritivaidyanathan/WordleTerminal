import sys
import random
import colorama
from colorama import Fore, Back, Style

#0 = right letter right position
#1 = right letter wrong posision
#2 = wrong letter wrong positions

def wordle():
    print("Let's play a game of Wordle!")
    listOfWords = ["ABUSE", "ADULT", "AGENT", "ANGER", "APPLE", "AWARD", "BASIS", "BEACH", "BIRTH", "BLOCK", "BLOOD", "BOARD", "BRAIN", "BREAD", "BREAK", "BROWN", "BUYER", "CAUSE", "CHAIN", "CHAIR", "CHEST", "CHIEF", "CHILD", "CHINA", "CLAIM", "CLASS", "CLOCK", "COACH", "COAST", "COURT", "COVER", "CREAM", "CRIME", "CROSS", "CROWD", "CROWN", "CYCLE", "DANCE", "DEATH", "DEPTH", "DOUBT", "DRAFT", "DRAMA", "DREAM", "DRESS", "DRINK", "DRIVE", "EARTH", "ENEMY", "ENTRY", "ERROR", "EVENT", "FAITH", "FAULT", "FIELD", "FIGHT", "FINAL", "FLOOR", "FOCUS", "FORCE", "FRAME", "FRANK", "FRONT", "FRUIT", "GLASS", "GRANT", "GRASS", "GREEN", "GROUP", "GUIDE", "HEART", "HENRY", "HORSE", "HOTEL", "HOUSE", "IMAGE", "INDEX", "INPUT", "ISSUE", "JAPAN", "JONES", "JUDGE", "KNIFE", "LAURA", "LAYER", "LEVEL", "LEWIS", "LIGHT", "LIMIT", "LUNCH", "MAJOR", "MARCH", "MATCH", "METAL", "MODEL", "MONEY", "MONTH", "MOTOR", "MOUTH", "MUSIC", "NIGHT", "NOISE", "NORTH", "NOVEL", "NURSE", "OFFER", "ORDER", "OTHER", "OWNER", "PANEL", "PAPER", "PARTY", "PEACE", "PETER", "PHASE", "PHONE", "PIECE", "PILOT", "PITCH", "PLACE", "PLANE", "PLANT", "PLATE", "POINT", "POUND", "POWER", "PRESS", "PRICE", "PRIDE", "PRIZE", "PROOF", "QUEEN", "RADIO", "RANGE", "RATIO", "REPLY", "RIGHT", "RIVER", "ROUND", "ROUTE", "RUGBY", "SCALE", "SCENE", "SCOPE", "SCORE", "SENSE", "SHAPE", "SHARE", "SHEEP", "SHEET", "SHIFT", "SHIRT", "SHOCK", "SIGHT", "SIMON", "SKILL", "SLEEP", "SMILE", "SMITH", "SMOKE", "SOUND", "SOUTH", "SPACE", "SPEED", "SPITE", "SPORT", "SQUAD", "STAFF", "STAGE", "START", "STATE", "STEAM", "STEEL", "STOCK", "STONE", "STORE", "STUDY", "STUFF", "STYLE", "SUGAR", "TABLE", "TASTE", "TERRY", "THEME", "THING", "TITLE", "TOTAL", "TOUCH", "TOWER", "TRACK", "TRADE", "TRAIN", "TREND", "TRIAL", "TRUST", "TRUTH", "UNCLE", "UNION", "UNITY", "VALUE", "VIDEO", "VISIT", "VOICE", "WASTE", "WATCH", "WATER", "WHILE", "WHITE", "WHOLE", "WOMAN", "WORLD", "YOUTH"]
    word = random.choice(listOfWords)
    availableletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    grayletters = []
    yellowletters = []
    greenletters = []

    index = 0
    for i in range (0, 6):
        print("---------------------------------------------")
        print("Trial " + str(i+1))
        print("Here are the letters you can use: ")
        print(availableletters)
        if (len(greenletters) > 0):
            print("Here are the green letters: ")
            print(colorama.Fore.GREEN + str(greenletters) + Style.RESET_ALL)
        if (len(yellowletters) > 0):
            print("Here are the yellow letters: ")
            print(colorama.Fore.YELLOW + str(yellowletters) + Style.RESET_ALL)
        if (len(grayletters) > 0):
            print("Here are the grayed out letters: ")
            print(colorama.Style.DIM + str(grayletters) + Style.RESET_ALL)
        guess = str(input("Type in your 5 letter guess: ")).strip().upper()
        if (len(guess)!= 5):
            print("Invalid Length.")
            while(len(guess) != 5):
                guess = str(input("Please try again. Type in a 5 letter guess: ")).strip().upper()
        print("Your guess was " + guess)
        if (guess == word):
            print("Congrats! You got the wordle.")
            print(str(i+1) + "/6")
            break
        else:
            results = ""
            for j in range (len(guess)):
                index = word.find(guess[j])
                if (index == j):
                    if(guess[j] not in greenletters):
                        greenletters.append(guess[j])
                    if(guess[j] in yellowletters):
                        yellowletters.remove(guess[j])
                    results += (guess[j] + " = Green\n")
                    print(colorama.Fore.GREEN + guess[j] + Style.RESET_ALL)
                elif (index != -1):
                    if(guess[j] not in yellowletters):
                        yellowletters.append(guess[j])
                    results += (guess[j] + " = Yellow\n")
                    print(colorama.Fore.YELLOW + guess[j] + Style.RESET_ALL)
                else:
                    if(guess[j] not in grayletters):
                        grayletters.append(guess[j])
                    if (guess[j] in availableletters):
                        availableletters.remove(guess[j])
                    print(colorama.Style.DIM + guess[j] + Style.RESET_ALL)
                    results += (guess[j] + " = Gray\n")
            print(Style.RESET_ALL)
            print("You have " + str(6-i-1) + " tries left.")
        if i == 5:
            print("The word was " + word)
    

wordle()
    
        
            



    