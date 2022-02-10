class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th birthday, {self.first}"

user1 = User("Anushka", "Singh", 19)
user2 = User("Saurabh", "Midha", 69)
print(user2.full_name())

print(user1.initials())

print(user2.likes("Music"))

print(user2.is_senior())

print(user1.age)
print(user1.birthday())
print(user1.age)