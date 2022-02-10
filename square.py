# def square(x):
# 	return x**2

# print(square(4))
# print(square(8))

# a = input('val of a = ')
# b= input('val of b = ')
# # def add(a, b):
# # 	return int(a) + int(b)
# # print(add(a, b))

# def multiply(a=2, b=2):
# 	"""multiplies two numbers"""
# 	return int(a)*int(b)
# print(multiply())
# print(multiply.__doc__)

# def yell(x):
# 	return (x.upper())
# print(yell('anushka'))

# def exponent(num, power=2):
#  	return num**power

# print(exponent(power=3, num=4)) #8
# print(exponent(3))
# print(exponent(7))


# def add(a, b):
# 	return a+b
# def subtract(a, b):
# 	return a - b
# def math(a, b, fn=add):
# 	return fn(a, b)
# print(math(2, 2, subtract))
# print(math(2,3))

# instructor1 = 'Mary'
# def say_hello():
# 	instructor2 = 'Colt'
# 	return f'Hello {instructor2}'
# say_hello()

# print(instructor1)


# t = 0

# def inc():
# 	global t
# 	t += 1
# 	return t

# print(inc())

# def return_day(x):
# 	a = {2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday', 1: 'Sunday'}
# 	if x > 0 and x <= 7:
# 		return a[x]
# 	return None
# print(return_day(1))


# def single_letter_count(x, y):
# 	if y in x:
# 		return x.count(y)
# 	return 0

# print(single_letter_count('hello world', 'z'))

# def multiple_letter_count(string):
#     return {x.lower():string.lower().count(x.lower()) for x in string}
# print(multiple_letter_count('Amazing'))

# def list_manipulation(list, command, location, value=None):
#     if command == 'add':
#         if location == 'beginning':
#             list = list.insert(0, value)
#             return list
#         elif location == 'end':
#             list = list.append(value)
#             return list
#     if command == 'remove':
#         if location == 'end':
#             list = list.remove(list[len(list)-1])
#             return list
#         elif location == 'beginning':
#             list = list.remove(list[0])
#             return list
# print(list_manipulation([1, 2, 3], 'remove', 'end'))
# print(list_manipulation([1, 2, 3], 'add', 'beginning', 1))

# def is_palindrome(string):
# 	string = string.replace(" ", "")
# 	if string == string[::-1]:
# 		return True
# 	return False

# print(is_palindrome('hannah'))
# print(is_palindrome('a man a plan a canal panama'))

def capitalize(str):
    return f'{str[0].upper()}{str[1:]}'

print(capitalize('anushka'))