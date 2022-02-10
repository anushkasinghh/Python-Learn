class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		# return "{} of {}".format(self.value, self.suit)
		return f"{self.value} of {self.suit}"

# test_card = Card('A', 'Hearts')
# print(type(test_card))