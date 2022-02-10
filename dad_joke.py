from requests import get
from pyfiglet import figlet_format
from colorama import init
from termcolor import colored
from random import choice

cont = "yes"

init()
print(colored(figlet_format("DAD JOKE 3000!"), color='cyan'))
while cont == "yes":
	T = input("Let me tell you a joke! Give me a topic: ") or ""
	url = "https://icanhazdadjoke.com/search"
	res = get(
		url,
		headers={"Accept":"application/json"},
		params={"term": T})
	data = res.json()

	if data['total_jokes']:
		if data["total_jokes"] > 1:
			print(f"I've got {data['total_jokes']} jokes about {T}. Here's one: ")
		else: 
			print(f"I've got only one joke about {T}. Here it is:")
		print(choice(list(data["results"][i]["joke"] for i in range(len(data["results"])))))
	else:
		print(f"Sorry! I don't have any jokes about {T}. Please try again.")
	cont = input("Do you want me to tell you another joke? ")	