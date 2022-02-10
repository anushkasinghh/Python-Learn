# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("Don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be int or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")
# print(divide(1,2))
# print(divide(1,"a"))


def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("SOMETHING WENT WRONG")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")
print(divide(1,0))
print(divide(1,"a"))
