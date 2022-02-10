from random import shuffle

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		# return "{} of {}".format(self.value, self.suit)
		return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
    	suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    	values = ['A','2','3','4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    	self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        print(self.cards)
        return "Deck of " + str(self.count()) + " cards"

    def __iter__(self):
    	return iter(self.cards)
    
    def count(self):
        return len(self.cards)

    def _deal(self, n):

    	count = self.count()
    	actual = min([count, n])
    	if count == 0:
    		raise ValueError("All cards have been dealt")
    	cards = self.cards[-actual:]
    	self.cards = self.cards[:-actual]
    	return cards


        # if n < self.count():
        #     cards = self.cards[n:]
        #     self.cards = self.cards[:(self.count() - n)]
        #     return cards

        # elif n > self.count() and self.count() != 0:
        #     self.cards = self.cards.clear()
        #     return self.cards

        # elif self.count() == 0:
        #     raise ValueError("All cards have been dealt")

    def shuffle(self):
        if self.count() < 52:
        	raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, n):
        return self._deal(n)

my_deck = Deck()
print(my_deck.count())
print(len(my_deck.cards))