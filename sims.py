# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:09:24 2022
@Purpose: Running simulations
@Author: Marcus
"""

""" Items
"Produce" : 0,
"Wood" : 0,
"Spices" : 0,
"Oil" : 0,
"Metal" : 0,
"Textiles" : 0,
"Home Goods" : 0,
"Firearms" : 0,
"Alcohol" : 0,
"Drugs": 0

"""
""" Notes
Time/Cycle
    4 Seasons
    3 Months per Season
    4 weeks per Month = 48 weeks

Base mats
    Produce
    Spices
    Wood
    Oil
    Metal
    
Produced Goods
    Textiles = Produce
    Home Goods = Wood + Metal
    Alcohol = Produce + Spice
    Firearms = Wood + Oil + Metal
    Drugs = Oil + Spices
    
Food Conversion Rates
    1 produce = 1 food
    1 livestock = 5 food

1 pop = 
    consume 2 food/week
    consume 1 Home Goods/week
    consume 1 spice/week
    consume .25 textile/week
    consume .1 firearm/week
    consume .5 alcohol/week
    
Week Phases
    Produce raw mats
    Consume Food.
        Kill/create pops (based on food deficit) (Adjust demand?)
    Produce goods.
    Adjust demand.
    DISPLAY
    
Pops are assigned equally across all resources.
    

"""

import random, math

livestockFoodRate = 5
weekNumber = 1


class City:
  def __init__(self, name, pop):
    self.name = name
    self.pop = pop
    self.targetPopGrowthRate = random.randint(1,10)*.01
    self.food = random.randint(int(math.ceil(self.pop/10)),self.pop)
    
    
    self.yieldRate = { #Yield rates for raw materials
            "Produce" : round(random.uniform(.1,2),2),
            "Wood" : round(random.uniform(.1,2),2),
            "Spices" : round(random.uniform(.1,2),2),
            "Oil" : round(random.uniform(.1,2),2),
            "Metal" : round(random.uniform(.1,2),2)
            }
    
    self.marketInventory = { #Inventory of items
            "Produce" : self.pop-int(self.pop*.1),
            "Wood" : 0,
            "Spices" : 0,
            "Oil" : 0,
            "Metal" : 0,
            "Textiles" : 0,
            "Home Goods" : 0,
            "Firearms" : 0,
            "Alcohol" : 0,
            "Drugs": 0
            }
    
    self.marketUnitPrice = { #Price of goods on the market
            "Produce" : 0,
            "Wood" : 0,
            "Spices" : 0,
            "Oil" : 0,
            "Metal" : 0,
            "Textiles" : 0,
            "Home Goods" : 0,
            "Firearms" : 0,
            "Alcohol" : 0,
            "Drugs": 0
            }
    
    self.resourceDemand = { #Demand of resources. (1 low, 10 high)
            "Produce" : 5,
            "Wood" : 5,
            "Spices" : 5,
            "Oil" : 5,
            "Metal" : 5,
            "Textiles" : 5,
            "Home Goods" : 5,
            "Firearms" : 5,
            "Alcohol" : 5,
            "Drugs": 5
            }
    
    self.resourceChange = { #Keeping record of how much was earned/week.
            "Produce" : 0,
            "Wood" : 0,
            "Spices" : 0,
            "Oil" : 0,
            "Metal" : 0,
            "Textiles" : 0,
            "Home Goods" : 0,
            "Firearms" : 0,
            "Alcohol" : 0,
            "Drugs": 0
            }

  def resolveWeek(self):
      #Phase 1: Raw Production
      self.resourceChange["Produce"] = int(self.pop*self.yieldRate["Produce"])
      self.resourceChange["Wood"] = int((self.pop/10)*self.yieldRate["Wood"])
      self.resourceChange["Spices"] = int((self.pop/10)*self.yieldRate["Spices"])
      self.resourceChange["Oil"] = int((self.pop/10)*self.yieldRate["Oil"])
      self.resourceChange["Metal"] = int((self.pop/10)*self.yieldRate["Metal"])
      
      self.marketInventory["Produce"] = self.marketInventory["Produce"] + int(self.pop*self.yieldRate["Produce"])
      self.marketInventory["Wood"] = self.marketInventory["Wood"] + int((self.pop/10)*self.yieldRate["Wood"])
      self.marketInventory["Spices"] = self.marketInventory["Spices"] + int((self.pop/10)*self.yieldRate["Spices"])
      self.marketInventory["Oil"] = self.marketInventory["Oil"] + int((self.pop/10)*self.yieldRate["Oil"])
      self.marketInventory["Metal"] = self.marketInventory["Metal"] + int((self.pop/10)*self.yieldRate["Metal"])
      
      #Phase 2: Food. Consume food if we have enough, otherwise kill pop.
      if(self.pop > self.food): #If we have more population than food, convert produce.
          requiredFood = self.pop - self.food #find how much more we need.
          if(self.marketInventory["Produce"] >= requiredFood): #if we have enough produce, convert it into food.
              self.food = self.food + requiredFood 
              self.marketInventory["Produce"] = self.marketInventory["Produce"] - requiredFood
      if(self.food >= self.pop): #Consume food if we have enough
          self.food = self.food - self.pop
      else: #if we can't feed everyone, kill between 30-60% of pop. Leave food stores.
          killPop = random.randint(30,60)*.01
          self.pop = int(self.pop - (self.pop*killPop))
          
      #Phase 3: Produce Goods
      
      #Phase 4: Adjust Demand
      #Phase 5: Adjust Prices
          

  def debugCity(self):
      print("\n----Week Number: ", weekNumber, "-----")
      print("Name: ", self.name)
      print("City Pop: ", self.pop)
      print("Pop Target Growth Rate: ", self.targetPopGrowthRate)
      print("Food Stores: ", self.food)
      print("-----Inventory-----")
      for key, value in self.marketInventory.items():
        print(key, " : ", value, " +", self.resourceChange[key])
      print("-----Yield Rates-----")
      for key, value in self.yieldRate.items():
        print(key, " : ", value)
      print("---------")
      
###########################################################
###########################################################
###########################################################
c1 = City("Santo Domingo", random.randint(500,5000))
for i in range(0,10):
    c1.debugCity()
    c1.resolveWeek()
    weekNumber = weekNumber + 1
    