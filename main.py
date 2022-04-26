# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:51:17 2022
@Purpose: Main Thread
@author: Marcus
"""

import City, Player, Ship #Our classes
import random, os #dependencies

Year = 1801
Month = 1 #1 = Jan, 12 = Dec.
gameState = 0
"""
I'm using gameState to track the current state of the game. this value will be used in the main thread below to determine what to print.
0 = city default, selection screen.
1 = market menu
2 = sailing menu


"""

#Create Cities
cityIndex = {
        "San Juan":0,
        "Port Royal":1,
        "Havana":2,
        "Nassau":3
        }
cities = [City.City("San Juan"), City.City("Port Royal"), City.City("Havana"), City.City("Nassau")]

#Track all spawned ships
ships = []
playerShip = Ship.Ship("Der PeliKan", "Sloop", 5) #starter ship
ships.append(playerShip)

#Create Player
player = Player.Player("Talon", cities[random.randint(0,3)].getName(), playerShip.getName())


while True:
    
    os.system('cls' if os.name == 'nt' else 'clear') #clear console
    
    #HUD
    print("*"*32, "Start Turn","*"*31)
    player.debugPlayer()
    print("*"*32, "Ship Info","*"*32)
    playerShip.debugShip()
    print("*"*32, "City Info","*"*32)
    cities[cityIndex[player.getLocation()]].debugCity()
    print("*"*75) #Max BR value
    
    #game state
    if(gameState == 0): #Selection state
        print("*"*28, "Make a selection","*"*29)
        print("Welcome to", player.getLocation())
        rawSelection = input("Type an action: Market, Set Sail, (CTRL-C to quit)\n:") # Need to add validation
        if(rawSelection == "Market"):
            gameState = 1 #goto Market screen
        elif(rawSelection == "Quit"):
            break
        elif(rawSelection == "Set Sail"):
            gameState = 2
    
    elif(gameState == 1): #Market state
        rawInput = input("You enter the market. What would you like to do? ([Buy/Sell] [item] [amount]) or exit\n:")
        inputArray = rawInput.split(" ")
        try:
            if(inputArray[0] == "Buy"):
                itemPrice = cities[cityIndex[player.getLocation()]].getCityItemPrice(inputArray[1]) #Get Item Price
                goldToSpend = itemPrice*int(inputArray[2])
                if(player.getGold() >= goldToSpend):
                    if((playerShip.getMaxCargoCapacity()-playerShip.getCurrentCargoUsed()) >= int(inputArray[2])):
                        player.setGold(goldToSpend*-1)
                        playerShip.changeCargoHold(inputArray[1], int(inputArray[2]))
                        print("Purchased", inputArray[2], inputArray[1])
                        input("Press enter to continue.")
                    else:
                        input("Ship's too fat. Press Enter to continue.")
                else:
                    input("You broke bitch. Press Enter to continue.")
     
            elif(inputArray[0] == "Sell"):
                if(playerShip.checkCargo(inputArray[1], int(inputArray[2])) == True):
                    itemPrice = cities[cityIndex[player.getLocation()]].getCityItemPrice(inputArray[1]) #Get Item Price
                    goldToGain = itemPrice*int(inputArray[2])
                    player.setGold(goldToGain)
                    playerShip.changeCargoHold(inputArray[1], int(inputArray[2])*-1)
                    print("Sold", inputArray[2], inputArray[1])
                    input("Press enter to continue.")
                else:
                    input("You broke bitch. Press Enter to continue.")
            elif(rawInput == "exit"):
                gameState = 0 
                
        except:
            print("Learn to type nerd.")
            input("Press enter to continue.")
            
    elif(gameState == 2):
        rawInput = input("You set sail. Where to?\nOptions: San Juan, Port Royal, Havana, Nassau or Cancel\n:")
        if(rawInput == "Cancel"):
            gameState = 0
        elif(rawInput == "San Juan"):
            player.setLocation("San Juan")
            gameState = 0
        elif(rawInput == "Port Royal"):
            player.setLocation("Port Royal")
            gameState = 0
        elif(rawInput == "Havana"):
            player.setLocation("Havana")
            gameState = 0
        elif(rawInput == "Nassau"):
            player.setLocation("Nassau")
            gameState = 0
    
    

