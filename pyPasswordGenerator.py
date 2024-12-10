import random 
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '^', '&', '*', '!', '?', '~', '=', '+', '-', '_', ':', ';', '<', '>', '{', '}', '[', ']', '|', '\\', '/', '(', ')', '`', '"', "'", '©', '®'];

numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like ?\n"))
numNumbers = int(input("How many numbers would you like ?\n"))
 
genPassword = []

for x in range(numLetters):
    print(x)
    genPassword.append(random.choice(letters))
for x in range(numSymbols):
    genPassword.append(random.choice(symbols))
for x in range(numNumbers):
    genPassword.append(random.choice(numbers))
print(''.join(genPassword))