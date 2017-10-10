#!/usr/bin/python

while exit != "":
	length = int(raw_input("Give a length of a rectangle: "))
	width = int(raw_input("Give a width of a rectangle: "))
	
	choice = raw_input("Would you like to calculate [1] area or [2] perimeter? ")
	
	while choice != "1" and choice != "2":
		choice = raw_input("Please choose [1] area or [2] perimeter: ")
		
	if choice == "1":
		answer = length * width
		print "The area of a rectangle that has a length of",length,"and a width of",width,"equals:",answer
	elif choice == "2":
		answer = (2 * length) + (2 * width)
		print "The perimeter of a rectangle that has a length of",length,"and a width of",width,"equals:",answer
	
	exit = raw_input("Press [ENTER] to quit or any key to compute another calculation. ")