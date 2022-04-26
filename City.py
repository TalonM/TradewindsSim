# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:09:24 2022
@Purpose: City Class
@Author: Marcus
"""

import random


class City:
    def __init__(self, name):
        self.name = name
        self.marketPrices = { #Prices of items
                "Food" : random.randint(5,50),
                "Textiles" : random.randint(100,750),
                "Firearms" : random.randint(500,1500),
                "Drugs": random.randint(1000,6969)
                }
    
    def getName(self):
        return self.name
    
    def getCityItemPrice(self, item):
        return self.marketPrices[item]
    
    def printPrices(self):
        print("City Market Prices: ")
        for item in self.marketPrices:
            print("\t", item, ':', self.marketPrices[item])
    
    def debugCity(self):
        print("City Name:", self.getName())
        self.printPrices()
      
###########################################################
###########################################################
###########################################################

    