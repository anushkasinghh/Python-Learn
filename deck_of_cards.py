from random import sample

class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"


class Deck:

	deck = [Card(y,x) for x in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K") for y in ("Hearts", "Diamonds", "Clubs", "Spades")]
	count = len(deck)

	def __init__(self):
		pass

	def __repr__(self):
		return f"Deck of {Deck.count} cards"

	def ct(self):
		return f"No. of cards remaining in deck are {Deck.count}"

	def _deal(self, n):
		# l = []
		if n < Deck.count:
			# while n > 0:
				# n -= 1
				# l.append(Deck.deck.pop(choice(range(len(Deck.deck)))))
			Deck.count -= 1
			return Deck.deck[len(Deck.deck)-n:]
		elif n > Deck.count and Deck.count != 0:
			# while Deck.count > 0:
			# 	l.append(Deck.deck.pop(choice(range(len(Deck.deck)))))
			Deck.count -= 1
			return Deck.deck.clear()
		elif Deck.count == 0:
			raise ValueError("All cards have been dealt")

	def shuffle(self):
		ls = Deck.deck
		return sample(ls, len(ls))

	def deal_card(self):
		return Deck._deal(self, 1)[0]

	def deal_hand(self, n):
		return Deck._deal(self, n)


my_deck = Deck()
print(my_deck)
print(my_deck.ct())
print(my_deck.deal_card())
# print(my_deck.ct())
print(my_deck.deal_hand(3))
print(my_deck.ct())
# print(my_deck._deal(24))
# print(my_deck.ct())
# print(Deck.deal_hand(34))
# print(my_deck.shuffle())
print(my_deck)

