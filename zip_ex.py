# def interleave(s1, s2):
# 	t = ''
#     for x in list(zip(s1, s2)):
#     	t += f"{x[0]}{x[1]}"
#     return t
# print(interleave('hi', 'ho'))
# #[('h', 'h'), ('i', 'o')]
s1 = 'hi'
s2 = 'ho'
print(list(''.join(x) for x in zip(s1, s2)))