#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:57:12 2021

@author: rozdixon
"""

#diner menu

menu = { 
    'breakfast' :
    {'sweet breakfasts' : {'pancakes' : 10.49, 'waffles' : 10.49, 'french toast' : 9.49, 'crepe' : 9.89},
    'savory breakfasts' : {'tofu scramble' : 8.49, 'eggs and fried potatoes' : 7.59, 
            'vegitarian crepe' : [9.89, 'sauteed mushrooms, spinach, and cheddar'], 'hashbrowns' : 6.79,
            'breakfast burrito' : [9.89, 'eggs, potatoes, salsa, avacado, jack cheese']},
    'omelettes' : {'feta cheese' : 8.59, 'western' : [8.59, 'ham, peppers, jack cheese'], 
            'mushroom and mozzarella' : 8.59, 'mushroom and black olive' : 8.59, 
            'spinach, tomato & feta' : 8.59}},
    'lunch' :
    {'soups' : {'chicken noodle' : 6.59, 'lentil' : 5.49, 'tomato' : 6.49, 'clam chowder' : 7.89,
            'french onion' : 7.59, 'broccoli cheddar' : 6.89},
    'sandwiches' : {'BLT' : 7.59, 'french dip' : 8.59, 
            'turkey bacon avacado' : [7.49, 'with jack cheese, tomato, and lettuce'], 'tuna melt' : 6.89, 
            'reuben' : 7.49, 'grilled cheese' : [4.59, 'choice of cheese']}},
    'beverages' :
    {'shirley temple' : 2.89, 'soft drink' : [2.49, 'coke, pepsi, sprite'], 
    'hot coffee' : [1.49, 'choice of cream and sugar'], 'orange juice' : 2.49, 'lemonade' : 2.49,
    'strawberry lemonade' : 2.89, 'sweet tea' : 1.79, 'vanilla shake' : 3.49, 'chocolate shake' : 3.49,
    'strawberry shake' : 3.49}
        }
#format
#choice of cheese for grilled cheese (pepper jack, cheddar, jack, brie (+1.00), gruyere)
#ask about cream and sugar in coffee
#get-set for price and calories (car thing)
#calories could be a private variable
#with side + dollar
#add elses
#option to sit down or use jukebox
#small, med, large drink
INPUT_MENU = ('/Users/rozdixon/Downloads/UCSC/CSE_20/menu.txt')

def print_menu():
    #print(menu[])
    menu_file = open('menu.txt','w')
    menu_file.writelines("Breakfast: with choice of sausage links or bacon, and biscuits or toast\n")
    menu_file.writelines("\tSweet Breakfasts:\n\t\t{}\n".format(menu['breakfast']['sweet breakfasts']))
    menu_file.writelines("\t\toffered with choice of whipped cream, blueberries, strawberries, or maple syrup\n")
    menu_file.writelines("\tSavory Breakfasts:\n\t\t{}\n".format(menu['breakfast']['savory breakfasts']))
    menu_file.writelines("\tOmelettes:\n\t\t{}\n".format(menu['breakfast']['omelettes']))
    menu_file.writelines("Lunch: comes with a choice of fries, curly fries, or sweet potato fries\n")
    menu_file.writelines("\tSoups:\n\t\t{}\n".format(menu['lunch']['soups']))
    menu_file.writelines("\tSandwiches:\n\t\t{}\n".format(menu['lunch']['sandwiches']))
    menu_file.writelines("Beverages:\n")
    menu_file.writelines("\t{}\n".format(menu['beverages']))
    menu_file.close()
    
def opn_menu(menu_file):
    opn = open(menu_file, 'r')
    print(str(opn.read()))

class Order:
    def __init__(self, main_order, side_order=None):
        self.main_order = main_order
        self.side_order = side_order
        self.price = 0
        self.cal = 0
    def get_order(self):
        pass
    def get_side(self):
        #side_order = input("Would you like a side? ")
        pass
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price += price
    def get_cal(self):
        return self.cal
    def set_cal(self, cal):
        self.cal += cal
    def __str__(self): # the str() method uses another one of these __ functions
        return "({0}, {1})".format(self.main_order, self.side_order)

class Breakfast(Order):
    def __init__(self, main_order, side_order=None):
        super().__init__(main_order, side_order)
    def savory_breaky(self):
        print("what's poppin little lady")
    def omelette_breaky(self):
        print("how u doin")

class Lunch(Order):
    def __init__(self, main_order, side_order):
        super().__init__(main_order, side_order)
    def set_side(self):
        side_q = input ("sides are an extra three dollars. is that alright? ").upper()
        if side_q == "YES":
            self.price += 2
            self.cal += 200
        elif side_q == "NO":
            print("alrighty! no side then")

class Sweet_Breaky(Breakfast):
    def __init__(self, main_order, toppings, side_order=None):
        super().__init__(main_order, side_order)
        self.toppings = toppings
    def set_toppings(self):
        #if toppings == "maple syrup" etc.
        toppings_q = input ("toppings are an extra dollar is that alright? ").upper()
        if toppings_q == "YES":
            self.price += 1
            self.cal += 100
        elif toppings_q == "NO":
            print("alrighty! no toppings then")
    def __str__(self): # the str() method uses another one of these __ functions
        return "({0}, {1})".format(self.main_order, self.toppings)

class Savory_Breaky(Breakfast):
    def __init__(self, main_order, side_order):
        super().__init__(main_order, side_order)
    def set_side(self):
        side_q = input ("sides are an extra two dollars. is that alright? ").upper()
        if side_q == "YES":
            self.price += 2
            self.cal += 200
        elif side_q == "NO":
            print("alrighty! no side then")

class Omelette_Breaky(Savory_Breaky):
    def __init__(self, main_order, side_order):
        super().__init__(main_order, side_order)
    def hot_sauce(self):
        hot_sauce_q = input("Would you like hot sauce on your omelette? ").upper()
        if hot_sauce_q == "YES":
            self.cal += 50
        elif hot_sauce_q == "NO":
            print("alrighty! no hot sauce then then")

class Drink(Order):
    def __init__(self, main_order, side_order=None):
        super().__init__(main_order, side_order)
        self.__straw_bool = False
    def straw(self):
        straw_q = input("Would you like a straw? ").upper()
        if straw_q == "YES":
            self.__straw_bool = True
        elif straw_q == "NO":
            print("It's people like you that are killing the environment.")

class Shake(Drink):
    def __init__(self, main_order, size, side_order=None):
        super().__init__(main_order, side_order)
        self.__size = size
    def shake_size(self, size):
        if size == 'medium':
            self.cal += 50
            self.price += 1
        elif size == 'large':
            self.cal += 100
            self.price += 1.50
            
class Full_Order:
    def __init__(self):
        self.orders = []
    def set_order(self):
        ordered = False
        #put in a while loop
        while not ordered:
            self.orders.append(take_main())
            complete_order = input("Will that be all? (yes or no) ").upper()
            if complete_order == 'YES':
                ordered = True
            elif complete_order == 'NO':
                ordered = False
        drink_q = input("Would you like anything to drink with that? (yes or no) ").upper()
        if drink_q == 'YES':
            drink_ordered = False
            while not drink_ordered:
                self.orders.append(take_drink())
                complete_drink_order = input("Will that be all? (yes or no) ").upper()
                if complete_drink_order == 'YES':
                    drink_ordered = True
                elif complete_drink_order == 'NO':
                    drink_ordered = False
        elif drink_q == 'NO':
            pass
        self.get_order()
    def get_order(self):
        for order in self.orders:
            print(f"ORDER {self.orders.index(order)}:\n\tMAIN - {order.main_order}")

def jukebox(coins):
    print("Add to queue:\n\
    A) My Chemical Romance - I'm Not Okay (I Promise)\n\
    B) Childish Gambino - IV. Sweatpants\n\
    C) Mac Miller - Dang! (feat.Anderson .Paak)\n\
    D) Malaguena - Celedonio Romero\n\
    F) Kendrick Lamaar - i\n\
    G) Car Seat Headrest - Drunk Drivers/Killer Whales\n\
    H) Neutral Milk Hotel - In the Aeroplane Over the Sea\n\
    I) Earl Sweatshirt - Sasquatch (feat. Tyler, The Creator)\n\
    J) J.I.D - D/vision (feat. EARTHGANG)\n\
    K) Juice WRLD - All Girls Are the Same")
    songs = []
    for i in range(int(coins)):
        songs += input("Add song to queue: ")
    #for range len coins, song choice: +=
        
def take_main():
    main_order = input("what would you like? ")
    main_order = main_order.lower()
    #anything to eat? yes = food order, then anything to drink with that?
    #no = alright what about something to drink? yes = what can i get you, no = ummmm ok 
    
    #sweet breaky
    if main_order == 'pancakes' or main_order == 'waffles' or main_order == 'french toast' or main_order == 'crepe':
        toppings = input("and what would you like on top? ")
        sweet_order = Sweet_Breaky(main_order, toppings)
        sweet_order.set_toppings()
        sweet_order.set_price(menu['breakfast']['sweet breakfasts'][main_order])
        #print(sweet_order.get_price())
        return sweet_order
        
    #savory breaky
    elif main_order == 'tofu scramble' or main_order == 'eggs and fried potatoes' or main_order == 'hashbrowns':
        side_order = input("and what would you like on the side? ")
        savory_order = Savory_Breaky(main_order, side_order)
        savory_order.set_side()
        savory_order.set_price(menu['breakfast']['savory breakfasts'][main_order])
        #print(savory_order.get_price())
        return savory_order
    elif main_order == 'vegitarian crepe' or main_order == 'breakfast burrito':
        side_order = input("and what would you like on the side? ")
        savory_order = Savory_Breaky(main_order, side_order)
        savory_order.set_side()
        savory_order.set_price(menu['breakfast']['savory breakfasts'][main_order][0])
        #print(savory_order.get_price())
        return savory_order
    
    #omelette
    elif main_order == 'omelette':
        pass
    elif 'omelette' in main_order:
        side_order = input("and what would you like on the side? ")
        h_omelette = main_order.replace('omelette', '')
        h_omelette = h_omelette.replace('and', '')
        h_omelette = h_omelette.replace(',', '')
        h_omelette = h_omelette.replace('&', '')
        h_omelette = h_omelette.replace(' ', '')
        if h_omelette == 'fetacheese' or h_omelette == 'mushroommozzarella' or h_omelette == 'mushroomblackolive' or h_omelette == 'spinachtomatofeta':
            if h_omelette == 'fetacheese':
                main_order = 'feta cheese'
            elif h_omelette == 'mushroommozzarella':
                main_order = 'mushroom and mozzarella'
            elif h_omelette == 'mushroomblackolive':
                main_order = 'mushroom and black olive'
            elif h_omelette == 'spinachtomatofeta':
                main_order = 'spinach, tomato & feta'
            omelette_order = Omelette_Breaky(main_order, side_order)
            omelette_order.set_side()
            omelette_order.hot_sauce()
            omelette_order.set_price(menu['breakfast']['omelettes'][main_order])
            #print(omelette_order.get_price())
            return omelette_order
        elif h_omelette == 'western':
            main_order = 'western'
            omelette_order = Omelette_Breaky(main_order, side_order)
            omelette_order.set_side()
            omelette_order.hot_sauce()
            omelette_order.set_price(menu['breakfast']['omelettes'][main_order][0])
            #print(omelette_order.get_price())
            return omelette_order
    elif main_order == 'feta cheese':
        side_order = input("and what would you like on the side? ")
        omelette_order = Omelette_Breaky(main_order, side_order)
        omelette_order.set_side()
        omelette_order.hot_sauce()
        omelette_order.set_price(menu['breakfast']['omelettes'][main_order])
        #print(omelette_order.get_price())
        return omelette_order
    elif main_order == 'western':
        side_order = input("and what would you like on the side? ")
        omelette_order = Omelette_Breaky(main_order, side_order)
        omelette_order.set_side()
        omelette_order.hot_sauce()
        omelette_order.set_price(menu['breakfast']['omelettes'][main_order][0])
        #print(omelette_order.get_price())
        return omelette_order
    elif 'mushroom' in main_order and 'mozzarella' in main_order:
        side_order = input("and what would you like on the side? ")
        main_order = 'mushroom and mozzarella'
        omelette_order = Omelette_Breaky(main_order, side_order)
        omelette_order.set_side()
        omelette_order.hot_sauce()
        omelette_order.set_price(menu['breakfast']['omelettes'][main_order])
        #print(omelette_order.get_price())
        return omelette_order
    elif 'mushroom' in main_order and 'black olive'in main_order:
        side_order = input("and what would you like on the side? ")
        main_order = 'mushroom and black olive'
        omelette_order = Omelette_Breaky(main_order, side_order)
        omelette_order.set_side()
        omelette_order.hot_sauce()
        omelette_order.set_price(menu['breakfast']['omelettes'][main_order])
        #print(omelette_order.get_price())
        return omelette_order
    elif 'spinach' in main_order and 'tomato' in main_order and 'feta' in main_order:
        side_order = input("and what would you like on the side? ")
        main_order = 'spinach, tomato & feta'
        omelette_order = Omelette_Breaky(main_order, side_order)
        omelette_order.set_side()
        omelette_order.hot_sauce()
        omelette_order.set_price(menu['breakfast']['omelettes'][main_order])
        #print(omelette_order.get_price())
        return omelette_order
    
        #soup
    elif main_order == 'soup':
        pass
    elif 'soup' in main_order:
        main_order = main_order.replace('soup', '')
        main_order = main_order.replace(' ', '')
        if main_order == 'chickennoodle' or main_order == 'clamchowder' or main_order == 'frenchonion' or main_order == 'broccolicheddar':
            if main_order == 'chickennoodle':
                main_order = 'chicken noodle'
            elif main_order == 'clamchowder':
                main_order = 'clam chowder'
            elif main_order == 'frenchonion': 
                main_order = 'french onion'
            elif main_order == 'broccolicheddar':
                main_order = 'broccoli cheddar'
        if main_order == 'chicken noodle' or main_order == 'lentil' or main_order == 'tomato' or main_order == 'clam chowder' or main_order == 'french onion' or main_order == 'broccoli cheddar':
            side_order = input("and what would you like on the side? ")
            soup_order = Lunch(main_order, side_order)
            soup_order.set_side()
            soup_order.set_price(menu['lunch']['soups'][main_order])
            #print(soup_order.get_price())
            return soup_order
    elif main_order == 'chicken noodle' or main_order == 'lentil' or main_order == 'tomato' or main_order == 'clam chowder' or main_order == 'french onion' or main_order == 'broccoli cheddar':
        side_order = input("and what would you like on the side? ")
        soup_order = Lunch(main_order, side_order)
        soup_order.set_side()
        soup_order.set_price(menu['lunch']['soups'][main_order])
        #print(soup_order.get_price())
        return soup_order
    
        #sandwich
    elif main_order == 'sandwich':
        pass
    elif 'sandwich' in main_order:
        main_order = main_order.replace('sandwich', '')
        main_order = main_order.replace(' ', '')
        if main_order == 'frenchdip' or main_order == 'tunamelt' or main_order == 'turkeybaconavacado' or main_order == 'grilledcheese':
            if main_order == 'frenchdip':
                main_order = 'french dip'
            elif main_order == 'tunamelt':
                main_order = 'tuna melt'
            elif main_order == 'turkeybaconavacado': 
                main_order = 'turkey bacon avacado'
            elif main_order == 'grilledcheese':
                main_order = 'grilled cheese'
        if main_order == 'french dip' or main_order == 'tuna melt' or main_order == 'reuben':
            side_order = input("and what would you like on the side? ")
            sandwich_order = Lunch(main_order, side_order)
            sandwich_order.set_side()
            sandwich_order.set_price(menu['lunch']['sandwiches'][main_order])
            #print(soup_order.get_price())
            return sandwich_order
        elif main_order == 'blt':
            side_order = input("and what would you like on the side? ")
            sandwich_order = Lunch(main_order, side_order)
            sandwich_order.set_side()
            sandwich_order.set_price(menu['lunch']['sandwiches'][main_order.upper()])
            #print(soup_order.get_price())
            return sandwich_order
        elif main_order == 'turkey bacon avacado' or main_order == 'grilled cheese':
            side_order = input("and what would you like on the side? ")
            sandwich_order = Lunch(main_order, side_order)
            sandwich_order.set_side()
            sandwich_order.set_price(menu['lunch']['sandwiches'][main_order][0])
            #print(soup_order.get_price())
            return sandwich_order
    elif main_order == 'french dip' or main_order == 'tuna melt' or main_order == 'reuben':
        side_order = input("and what would you like on the side? ")
        sandwich_order = Lunch(main_order, side_order)
        sandwich_order.set_side()
        sandwich_order.set_price(menu['lunch']['sandwiches'][main_order])
        #print(soup_order.get_price())
        return sandwich_order
    elif main_order == 'blt':
        side_order = input("and what would you like on the side? ")
        sandwich_order = Lunch(main_order, side_order)
        sandwich_order.set_side()
        sandwich_order.set_price(menu['lunch']['sandwiches'][main_order.upper()])
        #print(soup_order.get_price())
        return sandwich_order
    elif main_order == 'turkey bacon avacado' or main_order == 'grilled cheese':
        side_order = input("and what would you like on the side? ")
        sandwich_order = Lunch(main_order, side_order)
        sandwich_order.set_side()
        sandwich_order.set_price(menu['lunch']['sandwiches'][main_order][0])
        #print(soup_order.get_price())
        return sandwich_order

def take_drink():    
    drink_order = input("What would you like to drink? ").lower()
    if drink_order == 'shirley temple' or drink_order == 'orange juice' or drink_order == 'lemonade' or drink_order == 'strawberry lemonade' or drink_order == 'sweet tea':
        norm_drink = Drink(drink_order)
        norm_drink.straw()
        norm_drink.set_price(menu['beverages'][drink_order])
        #print(norm_drink.get_price())
        return norm_drink
    elif drink_order == 'soft drink' or drink_order == 'hot coffee':
        norm_drink = Drink(drink_order)
        norm_drink.straw()
        norm_drink.set_price(menu['beverages'][drink_order][0])
        #print(norm_drink.get_price())
        return norm_drink
    elif 'shake' in drink_order:
        size = input("What size would you like? (small, medium, large) ")
        shake_drink = Shake(drink_order, size)
        shake_drink.shake_size(size)
        shake_drink.set_price(menu['beverages'][drink_order])
        #print(shake_drink.get_price())
        return shake_drink

def main():
    g = Order('sausage', 'egg')
    print(g)
    print_menu()
    opn_menu(INPUT_MENU)
    #introducing the jukebox
    sit_or_jukebox = input("Go to your table or the jukebox?\n\
    A) jukebox\n\
    B) table\n\
        >>> ").upper()
    if sit_or_jukebox == 'A':
        coins = input("How many quarters do you insert? " )
        jukebox(coins)
    #the class is mean to be interactive, as it is to simulate being in a diner
    ordernum1 = Full_Order()
    print(ordernum1.set_order())
    
if __name__ == "__main__":
    main()