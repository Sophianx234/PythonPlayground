import random

random_integer = int(random.random() *2) +1
print(random_integer)

if random_integer == 1:
    print("Heads")
else: 
    print("Tails")
    
states = ['uruguay','brazil','japan','argentina']
states.pop(2)
states.insert(3,'paraguayxx')
states.remove('uruguay')
states.clear()
print(states)

friends = ['Alice','Bob','Charlie','Alexa','David','Emanuel']
random_friend = random.randrange(len(friends))
print(random_friend)

print(friends[random_friend])

girls = ["natalia",'gayley','nannet']

girls.extend(friends)[:]
fullFriends = girls[:]
print(fullFriends)