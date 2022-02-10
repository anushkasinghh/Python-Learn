def be_polite(fn):
	def wrapper():
		print('What a pleasure to meet you!')
		print(fn())
		return 'have a great day!'
	return wrapper
@be_polite
def greet():
	return 'My name is Colt!'
@be_polite
def rage():
	return 'I HATE YOU!'

print(greet())
print(rage())
