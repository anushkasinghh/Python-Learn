class User:

	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

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

# print(user2.full_name())

# print(user1.initials())

# print(user2.likes("Music"))

# print(user2.is_senior())

# print(user1.age)
# print(user1.birthday())
# print(user1.age)

print(User.active_users)
user1 = User("Anushka", "Singh", 19)
user2 = User("Saurabh", "Midha", 69)
print(User.active_users)
print(user2.logout())
print(User.active_users)