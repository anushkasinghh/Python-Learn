import termcolor
from colorama import init

init()
# print(dir(termcolor))

# print(help(termcolor))

text = termcolor.colored("HI THERE", color="red", on_color="on_cyan",attrs=["blink"])
print(text)