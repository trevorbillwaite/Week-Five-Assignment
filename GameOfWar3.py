__author__ = 'trevorbillwaite'

# Week Five Assignment
# Introduction to Computer Science
# GameOfWar3
# Collaboration with Nicole Ignasiak


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
		if gameCounter > 999:
			print("Game is a draw")
			break
		print (gameCounter)
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	# Define the actions of PlayerA and PlayerB playing a card
	ACardOne = PlayerA.pop()
	BCardOne = PlayerB.pop()
	
	ARank = getRank(ACardOne)
	BRank = getRank(BCardOne)
	
	if ARank > BRank:
		PlayerA.insert(0, ACardOne)
		PlayerA.insert(0, BCardOne)
	elif BRank > ARank:
		PlayerB.insert(0, ACardOne)
		PlayerB.insert(0, BCardOne)
	else:
		PlayerA.append(ACardOne)
		PlayerB.append(BCardOne)
		print("WAR")
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
	# Save off 3 cards from each player.
	# Match the 4th card.
	# Winner gets ALL the cards.
	# If this play is a tie, all cards are discarded (lost).
	if len(PlayerA) > 4 and len(PlayerB) > 4:
		ACardOne = PlayerA.pop()
		ACardTwo = PlayerA.pop()
		ACardThree = PlayerA.pop()
		ACardFour = PlayerA.pop()
		ACardFive = PlayerA.pop()
		BCardOne = PlayerB.pop()
		BCardTwo = PlayerB.pop()
		BCardThree = PlayerB.pop()
		BCardFour = PlayerB.pop()
		BCardFive = PlayerB.pop()
		
		AllCards = [ACardOne, ACardTwo, ACardThree, ACardFour, ACardFive, BCardOne, BCardTwo, BCardThree, BCardFour, BCardFive]
		
		ARankFive = getRank(ACardFive)
		BRankFive = getRank(BCardFive)
		
		if ARankFive > BRankFive:
			# This means that if PlayerA wins, all of the cards in the battle are given to PlayerA.
			PlayerA = AllCards + PlayerA
			print("PlayerA wins WAR")
		elif BRankFive > ARankFive:
			# This means that if PlayerB wins, all of the cards in the battle are given to PlayerB.
			PlayerB = AllCards + PlayerB
			print("PlayerB wins WAR")
		else:
			# If the cards flipped over in the WAR battle are the same, then all cards are lost (LOSE).
			PlayerA, PlayerB = LOSE(PlayerA, PlayerB)
			print("Second tie in same round, all cards in round are lost")
			
	return PlayerA, PlayerB

# This function discards all 10 cards
def LOSE(PlayerA, PlayerB):
	return PlayerA, PlayerB
	
	
	
def getRank(anyCard):
	return anyCard % 13

if __name__ == '__main__':
	main()

