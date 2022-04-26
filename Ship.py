# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:55:16 2022
@Purpose: Define Ship Class
@author: Marcus
"""

# Ship stat format: [Name (String), HP (int), MaxCannons (int), Speed (string), Cargo Hold Capacity (int)]
shipStats = [["Sloop", 25, 8, "Fast", 100],["Schooner", 40, 10, "Slow", 200]]
shipIndex = {
            "Sloop" : 0,
            "Schooner" : 1,
            }


class Ship:
    def __init__(self, name, className, cannons):
    
        self.shipName = name
        self.shipClass = className #Sloop, Schooner, etc
        self.hpMax = shipStats[shipIndex[self.shipClass]][1] #HP of the ship
        self.hpCurrent = self.hpMax
        self.cannonsMax = shipStats[shipIndex[self.shipClass]][2] #Max Number of cannons
        self.cannonsCurrent = cannons
        self.speed = shipStats[shipIndex[self.shipClass]][3] #Speed
        self.cargoMax = shipStats[shipIndex[self.shipClass]][4] #Cargo capacity
        self.cargoCurrentself = { #Inventory of items
            "Food" : 0,
            "Textiles" : 0,
            "Firearms" : 0,
            "Drugs": 0
            }
        
    def getClass(self):
        return self.shipClass
    
    def getHPMax(self):
        return self.hpMax
    
    def getHPCurrent(self):
        return self.hpCurrent
    
    def getName(self):
        return self.shipName
    
    def getCannons(self):
        return self.cannonsCurrent
    
    def getCannonsMax(self):
        return self.cannonsMax
    
    def getSpeed(self):
        return self.speed
    
    def checkCargo(self, item, num): #return True/False if ship has checked Cargo
        if(self.cargoCurrentself[item] >= num):
            return True
        else:
            return False
        
    def getCurrentCargoUsed(self):
        cargoInt = 0
        for key, value in self.cargoCurrentself.items():
            cargoInt = cargoInt + value
        return cargoInt
    
    def getMaxCargoCapacity(self):
        return self.cargoMax
    
    def changeCargoHold(self, itemName, valuev): #update cargo hold by valuev
        self.cargoCurrentself[itemName] = self.cargoCurrentself[itemName] + valuev
        
    def debugShip(self):
        print("Ship Name: ", self.getName())
        print("Ship Class: ", self.getClass())
        print("Ship HP: ", self.getHPCurrent(), "/", self.getHPMax())
        print("Ship Cannons: ", self.getCannons(), "/", self.getCannonsMax())
        print("Ship Capacity: ", self.getCurrentCargoUsed(), "/", self.getMaxCargoCapacity())
        print("Ship Cargo: ")
        for item in self.cargoCurrentself:
            print("\t", item, ' : ', self.cargoCurrentself[item])
    
    
    
    