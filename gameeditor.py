# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:41:46 2024

@author: ikowa
"""
story = { "Name":["This describes the game", "First choice description", "NodeA"], "start": ["You are on a boat. It's on fire", "Stay on the boat", "stay", "Jump in the water", "water"], 
 "stay": ["Did I mention the boat was ON FIRE?", "Start over", "start", "Quit", "quit"], 
 "water": ["You are in the water. You see a lifeboat and some floating debris", "Swim to the lifeboat", "lifeboat", "Cling to the debris", "debris"], 
 }
 
import json
            
        
def getMenuChoice():
    print("""
          0) exit
       1) load default game
       2) load a game file
       3) save the current game
       4) edit or add a node
       5) play the current game
    """)
    menu = input("Select a number")
    return menu
def getDefaultGame():
    
    defaultGame = {"start": ["default start node", "start over", "start","Quit","quit"],}
    defnode = ("start")
    print(f'{defaultGame[defnode][0]}')
    print(f"""Choose your next move
    1. {defaultGame[defnode][1]}
    2. {defaultGame[defnode][3]} """)
    return defnode

def playGame():
    print(f'{story[menu][0]}')
    decision = input(f"""Choose your next move
    1. {story[menu][1]}
    2. {story[menu][3]} """)
    if decision == "1":
        node = story[[1]]
    elif decision == "2":
        node = story[node][4]
    print("I play the game")
def main():
   keepGoing = True
   #Just do if staments for code
   menu = getMenuChoice()
   while keepGoing:
       if menu == "0":
          keepGoing = False
       elif menu == "1":
          menu = getDefaultGame()
       elif menu =="2":
           print("Load game file")
       elif menu =="3":
           print("save game file")
       elif menu =="4":
           print("edit or add")
       elif menu =="5":
           print("default game")
           menu = playGame(story, node)
       else:
           print("That's not right! try again")
           menu = getMenuChoice()
main()