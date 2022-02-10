def add_positive_numbers(x, y):
	assert x > 0 and y > 0, 'Both numbers must be positive!'
	return x +y

# print(add_positive_numbers(1, 2))
# print(add_positive_numbers(-1, 0))

def eat_junk():
	food = input('ENTER A FOOD PLEASE: ')
	assert food in ['pizza', 'ice cream', 'candy', 'fried butter'], 'Food must be junk food!'
	return f'NOM NOM NOM I am eatin {food}'

print(eat_junk())