def sum_all_nums(*args):
	print(args)
	t = 0
	for num in args:
		t += num
	print(t)

nums = [1, 2, 3, 4, 5, 6]
sum_all_nums(*range(1, 100))
sum_all_nums(*nums)




	 #args is a tuple containing
	# all the arguments that we pass in

# print(sum_all_nums(2, 4, 5))
# print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def ensure_correct_info(*args):
# 	if 'Colt' in args and 'Steele' in args:
# 		return 'Welcome back Colt'
# 	return 'Not sure who you are :/'
# print(ensure_correct_info('Anushka', 'Singh'))
# print(ensure_correct_info('Colt', 'Steele', True, 12))