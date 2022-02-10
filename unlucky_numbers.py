for x in range(1, 21):
	if x == 4 or x == 13:
		print( str(x) + " is unlucky! ")
	elif x % 2 == 0:
		print(str(x) + " is even")
	else:
		print(str(x) + " is odd")