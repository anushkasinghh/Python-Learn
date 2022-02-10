# try:
# 	foobar
# except:
# 	print("PROBLEM!!!")
# print("after the try!")  

# d = {"name": "Ricky"}
# d['city']
# def get(d,key):
# 	try:
# 		d[key]
# 	except KeyError:
# 		return None

# d = dict(name="Ricky")
# print(get(d,'city'))
# print(get(d,'name'))



# try
# except
# else
# finally
# while True:
# 	try:
# 		num = int(input("please enter a number: "))
# 	except ValueError:
# 		print("that's not a number! ")
# 	else:
# 		print("GOOD JOB YOU ENETERED A NUMBER")
# 		break
# 	finally:
# 		print("RUNS NO MATTER WHAT")
# print("rest of game logic runs")


def divide(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError("Please do not divide by zero")
    if type(num1) and type(num2) != float and type(num1) and type(num2) != int :
        raise TypeError("Please provide two integers or floats")
    return num1/num2
    
print(divide(1,0))