# _name
#__name
#__name__

class Person:
	def __init__(self):
		self._secret = "hi!"
		self.name = "Tony"
		self.__msg = "Ilike turtles"

p = Person()

print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
