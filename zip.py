# def max_magnitude(ls):
# 	return max(abs(x) for x in ls)
# print(max_magnitude([1, 2, -3]))

# a =[1.2, 3, [], {}]
# for x in a:
# 	print(type(x))

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
# final_grades = [pair for pair in zip(midterms, finals)]
# print(final_grades)
# fg = [max(x) for x in final_grades]
# print(fg)
# result = dict(zip(students, fg))
# print(result)

# result = {x[0]: max(x[1], x[2]) for x in zip(students, midterms, finals)}
# print(result)

# scores = dict(zip(
# 	list(
# 	map(
# 	lambda pair: max(pair),
# 	zip(midterms, finals)
# 	))
# 	, students))
# print(scores)

grades = {x[0]: (x[1]+x[2])/2 for x in zip(students, midterms, finals)}
print(grades)

grades1 = dict(
	zip(
		students, 
		list(
			map(lambda x: (x[0]+x[1])/2, 
				zip(midterms, finals)
				)
			)
		)
	)
print(grades1)