#!/usr/bin/python

import time
import random
from datetime import datetime
from sys import exit


def start():
	print "There is a door to your left, a door to your right, and a path behind you. Which one do you choose?"
	choice = raw_input("> ")
	
	if choice == "left" or choice == "left door":
		mario()
	elif choice == "right" or choice == "right door":
		minecraft()
	elif choice == "path" or choice == "behind":
		print "The path that you came from has magically sealed itself off. Press any key to go back."
		raw_input("> ")
		start()
	else:
		end("You died of indecision.")
		
		
def mario():
	print "You pass through the door and suddenly you see flying turtles, venus flytraps spitting fireballs, and a strange plumber with a mustache that beckons you over. Do you talk to the plumber, run, or explore?"
	choice = raw_input("> ")
	
	while choice != "talk" and choice != "run" and choice != "explore":
		print "Sorry, that's not an option. Choose to talk, run, or explore."
		choice = raw_input("> ")
		
	if choice == "talk":
		print "The plumber, whose name is apparently Mario, tells you that Princess Peach was taken and that he cannot save her. You are his last hope or she will be gone forever. Will you help him?"
		answer = raw_input("> ")
		
		if answer == "yes" or answer == "y":
			boss()
		elif answer == "no" or answer == "n":
			end("Mario turns away. As he does the goombas and koopas swarm. As a newcomer to this world, they easily overcome you.")
		else:
			end("A fireball hit you while you were deciding because you weren't paying attention.")
		
	elif choice == "run":
		end("As you run, you reach an area that has lots of penguins and ice. You think you can rest for a while when suddenly a kart comes racing towards you with a blue shell flying behind it. You are collateral damage.")
	elif choice == "explore":
		boss()
	else:
		print "You stand in one place too long and a goomba hits you, sending you into darkness to cool theme music."

		
def boss():
	print "You walk for what seems like miles, a strange spiky castle drawing closer and closer. When you get to the doors, you take a deep breath and enter, coming face to face with a GIANT spiky monster and seeing a princess trapped behind him."
	print "Do you throw a fireball or do you demand that it lets the princess go?"
	choice = raw_input("> ")
	
	if choice == "throw a fireball" or choice == "fireball":
		print "You caught the monster off guard! Stunned, he attempts to throw a fireball of his own which you easily dodge. You end up defeating him and rescuing the princess! Princess Peach is so grateful that she leads you to a strange mushroom house that has three chests inside. Do you choose the one on the left, on the right, or in the middle?"
		chest = raw_input("> ")
		
		while chest != "left" and chest != "right" and chest != "middle":
			print "Sorry, that's not an option and you deserve a reward. Choose left, right, or middle."
			chest = raw_input("> ")
			
		treasure = ["a fireball powerup", "an iceball powerup", "three mushrooms"]
		
		end("You chose the %s chest and received %s as your prize!" % (chest, random.choice(treasure)))

	elif choice == "demand" or choice == "let princess go" or choice == "demand that it lets the princess go":
		print "The monster just stares at you..."
		
		seconds = []
		for i in range(0, 4):
			seconds.append(i)
			seconds.pop(-1)
		
		for sec in seconds:
			print "%d..." % sec
			time.sleep(1)
			
		end("Too late, you realize he has thrown a fireball. You try to dodge out of the way, but to no avail.")
		
	else:
		end("The spiky turtle couldn't understand your silence and threw a fireball at you in frustration. You first shrink in size, then fall into darkness.")
	
	
def minecraft():
	print "You step through the door and immediately everything turns into blocks. The trees, the hills, even the pig wandering around looks blocky."
	print "You get used to your new environment, chopping down a few trees first with your bare hands, then with a wooden axe you made. As it gets dark, you hear a noise behind you. What do you do?"
	turn = False
	
	while True:
		choice = raw_input("> ")
	
		while choice != "turn around" and choice != "turn" and choice != "run" and choice != "keep going" and choice != "stop":
			print "Sorry, you can't choose that. Choose to turn, run, or stop."
			choice = raw_input("> ")
			
		if choice == "turn around" or choice == "turn":
			print "As you turn, you hear a hissing noise. Scared, you blindly swing your axe one, two, three, four times and the creature falls. Upon examination, you see gunpowder. Must have been a creeper."
			turn = True
			
		elif choice == "run" and turn == False or choice == "keep going" and turn == False:
			end("You start to run, but you lurch forward as you feel an arrow pierce your back. You try and turn to fight the creature, but when you do you are only able to watch as the skeleton shoots you again, killing you.")
				
		elif choice == "run" or choice == "keep going" and turn == True:
			print "You take another glance around, confirming nothing else is lurking in the shadows, and continue on your way, keeping a watchful eye on every movement."
			dungeon()
				
		elif choice == "stop":
			option = random.randint(1,2)
			if option == 1:
				end("You stop, thinking maybe you were just hearing things... you find out you were wrong very quickly.")
				
			elif option == 2:
				print "You stop, thinking maybe you were just hearing things... it turns out it was just a sheep eating some grass behind you. You press on through the night."
				dungeon()
			
			
def dungeon():
	print "As the sun rises, you realize there is more to life than just wandering aimlessly. You find a village, make friends, and settle down, often going on adventures to gather iron, gold, and even diamond."
	print "On one of these adventures, you stumble across a dungeon that you decide to explore in hopes of finding gold, diamonds, or even the end portal. As you walk down the corridor, the path diverges into three. Do you go left, right, or in the middle?"
	choice = raw_input("> ")

	while choice != "left" and choice != "right" and choice != "middle" and choice != "in the middle":
		print "Sorry, that's not a valid choice. Please choose left, right, or middle."
		choice = raw_input("> ")

	if choice == "left":
		end("You continue down the left corridor. As you walk, you hear a click and suddenly the floor disappears from beneath you and you fall into a pit of lava.")
		
	elif choice == "right":
		end("You continue down the right corridor. You take a few more twists and turns and can see an ornately decorated room up ahead. Anticipating the end portal, you carelessly forgot to keep your guard up and a cave spider jumps out and attacks you, weakening you to where a zombie behind the cave spider only has to hit you once before you die.")
		
	elif choice == "middle" or choice == "in the middle":
		print "You continue down the middle corridor. You take a few more twists and turns, keeping your guard up and looting chests along the way. You eventually fight your way into a room with three chests."
		print "Do you choose the chest on the left, on the right, or the middle?"
		chest = raw_input("> ")
		
		while chest != "left" and chest != "right" and chest != "middle":
			print "Sorry, that's not an option and you deserve a reward. Choose left, right, or middle."
			chest = raw_input("> ")
			
		treasure = ["16 diamonds", "an enchanted diamond chestplate", "an unbreaking enchanted diamond sword"]
		
		end("You chose the %s chest and received %s as your prize!" % (chest, random.choice(treasure)))
	
	
def end(why):
	print why, "\nGame over"
	target = open("endings.txt", "a")
	target.write(why + " " + str(datetime.now().ctime()) + "\n")
	target.close()
	exit(0)
	
	
start()