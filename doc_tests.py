import unittest
from card import Card
from deck import Deck

class CardTests(unittest.TestCase):
	# def setUp(self):
	# 	self.test_card = Card('A', 'Hearts')

	def test_init(self):
		'''cards should have a suit and a value'''
		test_card = Card('A', 'Hearts')
		self.assertTrue(test_card.suit)
		self.assertTrue(test_card.value)

	def test_repr(self):
		'''repr should return a string of the form "VALUE of SUIT"'''
		test_card = Card('A', 'Hearts')
		self.assertEqual(str(test_card), "A of Hearts")

class DeckTests(unittest.TestCase):

	# def setUp(self):
	# 	self.test_deck = Deck()

	def test_init(self):
		test_deck = Deck()
		self.assertTrue(isinstance(test_deck.cards, list), True)
		self.assertEqual(len(test_deck.cards), 52)

	def test_repr(self):
		test_deck = Deck()
		self.assertEqual(str(test_deck), "Deck of 52 cards")

	def test_count(self):
		test_deck = Deck()
		self.assertEqual(test_deck.count(), 52)
		test_deck.cards.pop()
		self.assertEqual(test_deck.count(), 51)

	def test_deal_sufficient_cards(self):
		test_deck = Deck()
		self.assertTrue(isinstance(test_deck._deal(10), list))
		self.assertEqual(len(test_deck._deal(10)), 10)
		self.assertEqual(test_deck.count(), 32)

	def test_deal_insufficient_cards(self):
		test_deck = Deck()
		self.assertEqual(len(test_deck._deal(100)), 52)
		self.assertEqual(test_deck.count(), 0)

	def test_deal_no_cards(self):
		test_deck = Deck()
		test_deck._deal(100)
		with self.assertRaises(ValueError):
			test_deck._deal(3)


	def test_shuffle_full_deck(self):
		test_deck = Deck()
		cards = test_deck.cards[:]
		test_deck.shuffle()
		self.assertEqual(test_deck.count(), 52)
		self.assertNotEqual(test_deck.cards, cards)

	def shuffle_not_a_full_deck(self):
		test_deck._deal(30)
		with self.assertRaises(ValueError):
			test_deck.shuffle()

	def test_deal_card(self):
		test_deck = Deck()
		card = test_deck.cards[-1]
		dealt_card = test_deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(test_deck.count(), 51)

	def test_deal_hand(self):
		test_deck = Deck()
		ls_cards = test_deck.cards[-10:]
		dealt_cards = test_deck.deal_hand(10)
		self.assertEqual(ls_cards, dealt_cards)
		self.assertEqual(test_deck.count(), 42)
		self.assertTrue(isinstance(dealt_cards, list))

if __name__ == '__main__':
	unittest.main()
