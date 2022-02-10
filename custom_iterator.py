#  rewriting the range function:

class Counter:

	def __init__(self, low, high, step):
		self.low = low
		self.high = high
		self.step = step

	def __iter__(self):
		return self

	def __next__(self):
		if self.low < self.high:
			i = self.low
			self.low += self.step
			return i
		raise StopIteration

for x in Counter(1, 10, 4): #step can only be positive
	print(x)