"""
File: blackjack.py
Example 8.5
Author: George

Establishes a player class, dealer class, and game mechanics for a BlackJack card game.
"""

from cards import Deck, Card

class Player(object):
	"""This class represents a player in a blackjack game."""
	
	def __init__(self, cards):
		self._cards = cards
		for card in self._cards:
			card.turn()

	def __str__(self):
		"""Returns string rep of cards and points."""
		result = ", ".join(map(str, self._cards))
		result += "\n  " + str(self.getPoints()) + " points"
		return result
		
	def hit(self, card):
		self._cards.append(card)
		
	def getPoints(self):
		"""Returns the number of points in the hand"""
		count = 0
		for card in self._cards:
			if card.rank > 9:
				count += 10
			elif card.rank == 1:
				count += 11
			else:
				count += card.rank
		#Deduct 10 if Ace is available and need as 1
		for card in self._cards:
			if count <= 21:
				break
			elif card.rank == 1:
				count -= 10
		return count
		
	def hasBlackjack(self):
		"""Dealt 21 or not"""
		return len(self._cards) == 2 and self.getPoints() == 21
		
	def getCards(self):
		return self._cards

class Dealer(Player):
	"""Like a player, but with some restrictions"""
	
	def __init__(self, cards):
		"""Initial state: show one card only"""
		Player.__init__(self, cards)
		self._showOneCard = True
		self._cards[0].turn()
		
	def __str__(self):
		"""Return just one card if not hit yet."""
		if self._showOneCard:
			return str(self._cards[0])
		else:
			return Player.__str__(self)
			
	def hit(self, deck):
		"""Add cards while points < 17, then allow all to be shown."""
		while self.getPoints() < 17:
			card = deck.deal()
			card.turn()
			self._cards.append(card)
			
	def turnFirstCard(self):
		"""Turns over the first card to show it"""
		self._showOneCard = False
		self._cards[0].turn()

class Blackjack(object):
	
	def __init__(self):
		self._deck = Deck()
		self._deck.shuffle()
		
		#Pass the player and the dealer two cards each
		self._player = Player([self._deck.deal(), self._deck.deal()])
		self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

	def getPlayerCards(self):
		"""Returns a list of the player's cards."""
		return self._player.getCards()
		
	def getDealerCards(self):
		"""Returns a list of the dealer's cards."""
		return self._dealer.getCards()
		
	def hitPlayer(self):
		"""Deals a card to the player. Returns a tuple of the card and the player's points."""
		card = self._deck.deal()
		card.turn()
		self._player.hit(card)
		return (card, self._player.getPoints())
		
	def hitDealer(self):
		"""Deals cards to the dealer until an outcome occurs. Returns a string representing the outcome."""
		self._dealer.turnFirstCard()
		playerPoints = self._player.getPoints()
		if playerPoints > 21:
			return "You bust and lose!"
		else:
			self._dealer.hit(self._deck)
			dealerPoints = self._dealer.getPoints()
			if dealerPoints > 21:
				return "Dealer busts, you win!"
			elif dealerPoints > playerPoints:
				return "Dealer wins :("
			elif dealerPoints < playerPoints and playerPoints <= 21:
				return "Congrats! You win!"
			elif dealerPoints == playerPoints:
				if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
					return "Blackjack! You Win!"
				elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
					return "Dealer Blackjack! You lose!"
				else:
					return "There is a tie"
