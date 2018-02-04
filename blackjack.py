import random
import os
import sys

# OPP
class Deck(object):
	suits = ['Clubs','Diamonds', 'Hearts', 'Spades']
	cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'Kings']
	values = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

	def __init__(self):
		self.deck = [(card + " of " + suite) for card in self.cards for suite in self.suits]
		self.deck = [(card, value) for (card,value) in zip(self.deck, self.values)]

class Player(object):
	amount = 100
	score = 0
	hand = []

	def __init__(self, name):
		self.name = name
		self.hand = []

	def add_hand(self, card): 
		self.hand.append(card)

# Functions 
def start_game():
	os.system('clear') 
	ins_name  = raw_input('Player Name: ')
	player = Player(name = ins_name)
	os.system('clear') 
	run_game()

def run_game():
	pick_card(player)
	pick_card(player)
	pick_card(dealer)
	pick_card(dealer)
	print dealer.hand
	print_board()
	if is_blakjack(dealer) and is_blakjack(player): 
		print 'Both wins'
		cont()
	elif is_blakjack(player): 
		print 'Player Wins'
		update_value(player, dealer)
		cont()
	elif is_blakjack(dealer): 
		print 'Dealer Wins'
		update_value(dealer, player)
		cont()
	else: 
		loop()

def pick_card(user):
	x = random.randint(0, 51)
	while True: 
		if deck.deck[x][0] not in user.hand:
			user.add_hand((deck.deck[x][0]))
			user.score += deck.deck[x][1]
			break

def print_board():
	print 'Player Hand...........'
	for card in player.hand: print card
	print ("Player Score: " + str(player.score))
	print ("Player Amount: " + str(player.amount))
	print 'Dealer Hand...........'
	print dealer.hand[0]
	print ("Dealer Amount: " + str(dealer.amount))

def is_blakjack(user): 
	if (user.score == 11 and (user.hand[0].find('Ace') == 0 or user.hand[1].find('Ace') == 0)) or user.score == 21:
		user.score = 21
		return True
	else:
		return False

def cont():
	if dealer.amount == 0:
		print "Player wins the game"
		sys.exit()
	elif player.amount == 0:
		print "Dealer wins the game"
		sys.exit()
	else:
		option = raw_input("Do you want to continue? 0 to quit, 1 to play again: ")
		if option == '1':
			play_again()
		else: 
			print 'Finish'
			sys.exit()

def update_value(winner, looser): 
	winner.amount += 20
	looser.amount -= 20 

def loop():
	while True:
		option = raw_input('Choose 0 to Stand or 1 to Hit: ')
		if option == '0': 
			os.system('clear')
			print 'Dealer Result...........'
			print "Dealer's Hand: "
			for card in dealer.hand: print card
			print "Dealer's Score: " + str(dealer.score)
			print 'Player Result...........'
			print "Player's Hand: "
			for card in player.hand: print card
			print "Player's Score: " + str(player.score)
			if winner() == 'Both': 
				print "It's a tie"
				cont()
			else: 
				win = winner().name
				if win == "Dealer": 
					update_value(dealer, player)
					print 'The winner is: ' + win
					cont()
				else: 
					update_value(player, dealer)
					print 'The winner is: ' + win
					cont()		
			break
		else: 
			os.system('clear')
			pick_card(player)
			print_board()
			if game_over():
				print "You Loose!"
				update_value(dealer, player)
				cont()
				break
			elif is_blakjack(player): 
				print 'Player Wins'
				update_value(player, dealer)
				cont()
				break

def game_over(): 
	return player.score > 21

def winner(): 
	if player.score == dealer.score:
		return "Both"
	elif player.score > dealer.score: 
		return player
	else: 
		return dealer

def play_again():
	del player.hand[:]
	del dealer.hand[:]
	dealer.score = 0
	player.score = 0
	os.system('clear') 
	run_game()

# Global Scope
deck = Deck()
player = Player(name = 'Player')
dealer = Player(name = 'Dealer')

# Run Game
start_game()