# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:54:39 2022
@Purpose: Player Object
@author: Marcus
"""

class Player:
    def __init__(self, name, loc, assignedShipName):
        self.playerName = name
        self.gold = 500
        self.currentLocation = loc
        self.shipName = assignedShipName
    
    def setGold(self, goldv):
        self.gold = self.gold + goldv
    
    def getGold(self):
        return self.gold
    
    def getName(self):
        return self.playerName
    
    def getShipName(self):
        return self.shipName
    
    def getLocation(self):
        return self.currentLocation
    
    def setLocation(self, loc):
        self.currentLocation = loc
    
    def debugPlayer(self):
        print("Location: ", self.getLocation())
        #print("Ship Name: ", self.getShipName())
        print("Gold: ", self.getGold())
        
        
    
    