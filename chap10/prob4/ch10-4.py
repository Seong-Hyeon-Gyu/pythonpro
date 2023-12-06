class Card:
	""" A playing card. """
	RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
	SUITS = ["c","d","h","s"]
	def __init__(self, rank, suit):
		self.rank=rank
		self.suit=suit
	def __str__(self):
		reply=self.rank+self.suit
		return reply
class Hand:
	""" A hand of playing chars. """
	def __init__(self):
		self.cards=[]
	def __str__(self):
		if self.cards:
			reply=""
			for card in self.cards:
				reply+=str(card)+" "
		else:
			reply="<empty>"
		return reply
	def clear(self):
		self.cards=[]
	def add(self, card):
		self.cards.append(card)
	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)
class Deck(Hand):
	""" A deck of playing cards. """
	def populate(self):
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))
	def shuffle(self):
	 	import random
	 	random.shuffle(self.cards)
	def deal(self, hands, per_hand=1):
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card=self.cards[0]
					self.give(top_card, hand)
				else:
					print("Out of cards!")
class Unprintable_Card(Card):
	def __str__(self):
		return "<unprintable>"
class Positionable_Card(Card):
	def __init__(self, rank, suit, face_up = True):
		super().__init__(rank, suit)
		self.is_face_up = face_up
	def __str__(self):
		if self.is_face_up:
			reply = super().__str__()
		else:
			reply = "XX"
		return reply
	
	def flip(self):
		self.is_face_up = not self.is_face_up
class Player(Card):
	def __init__(self, name):
		self.name = name
class Dealer(Card):
if __name__ == "__main__":
	print "\t\t\tWelcome to Blackjack!"
	pn = int(input("How many players? (2-5): "))
	players = [player1, player2, player3, player4, player5]
	del players[pn:5]
	for count in range(pn):
		name = input("Enter player name: ")
		for user in range(players):
			players[user] = name
	deck = Deck()
	deck.populate()
	deck.shuffle()
	

