from utils import *

values = []
for line in get_input(1):
    value = ""
    for character in line:
        if character.isdigit():
            value += character
            break
    for character in line[::-1]:
        if character.isdigit():
            value += character
            break
    values.append(int(value))
answer = sum(values)
print(answer)
