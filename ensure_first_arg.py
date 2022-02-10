from functools import wraps

def ensure_first_arg(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] == val:
				return fn(*args, **kwargs)
			return f'Invalid! First argument must be {val}'
		return wrapper
	return inner

@ensure_first_arg('burrito')
def fav_foods(*foods):
	return foods

print(fav_foods('burrito', 'Ice cream'))
print(fav_foods('Ice cream', 'burrito'))

@ensure_first_arg(10)
def add_to_ten(num1, num2):
	return num1 + num2

print(add_to_ten(10, 12))
print(add_to_ten(1, 2))