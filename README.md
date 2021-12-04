# diner_menu

READ ME
https://github.com/rozy-dixon/diner_menu	diner_menu.py is a simple program to run what is basically a diner simulation
	First you'll want to look at the Order class, which takes in an order every time an order is inputted.
	These are organized in a dictionary called menu, printed into a file called menu.txt, and opened at the beginning of main right before the jukebox option is introduced.
	The menu is organized into breakfast, lunch, and beverage, which is then organized into sweet breakfast, savory breakfast, omelette, soup, and sandwich.
	The order class is organized similarly with subclasses for sweet breakfast, savory breakfast, and drink, then omelette which builds off savory breakfast and shake which builds off drink
	The full order class is meant to process these orders and return them after they are inputted
	The demo program is simply to introduce the functions, and organization thereof, that the user will need.
	As this is a simulation for the user, it is entirely interactive, and the variables are not set.
