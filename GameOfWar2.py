__author__ = 'trevorbillwaite'

# Week Five Assignment
# Introduction to Computer Science
# GameOfWar2


#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	# Define the actions of PlayerA and PlayerB playing a card
	ACard = PlayerA.pop()
	BCard = PlayerB.pop()
	
	ARank = getRank(ACard)
	BRank = getRank(BCard)
	
	if ARank > BRank:
		PlayerA.insert(0, ACard)
	elif BRank > ARank:
		PlayerB.insert(0, BCard)
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
		
	
	'''
	This is the method that plays one round of War
	The method takes PlayerA and PlayerB as input parameters
	and returns PlayerA and PlayerB after modification
	for the round
	
	Remember, high card wins. I have included a convenience
	function getRank(anyCard) that will return the rank.
	
	See the README.md for the variations of
	the game to program.
	'''
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# Any card that loses a battle is dead, or eliminated from the game.
	# The card that wins returns to the original owner. This will result in a average of about 45 rounds per run.

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()