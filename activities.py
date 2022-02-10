# UNITTEST
from random import choice

def eat(food, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError('is_healthy must be a boolean')
	if is_healthy:
		return f"I'm eating {food} because my body is a temple"
	return f"I'm eating {food} because YOLO!"

def nap(num_hours):
	if num_hours < 3:
		return f"I'm feeling refreshed after my {num_hours} hour nap"
	return f"UGHHH I overslept:'), should'nt have slept for {num_hours} long hours"
	
def is_funny(name):
	if name == 'tim': return False
	return True

def laugh():
	return choice(('lol', 'hahaha', 'tehehehe'))
