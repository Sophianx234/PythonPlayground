

friends = ['Boruto',"Naruto", 'Sasuke']
for x in range(len(friends)):
    print(x)
    
newFriends = [x for x in friends if x !='Boruto' ]
print(newFriends)

print( 'Dormamu' in friends)

scores = [66,45,13,11,12,85,39,90,77,18,89,93]
maxScore = 0
for x in scores:
    if maxScore<x:
        maxScore = x
    else:
        maxScore = maxScore

print(maxScore)

print(max(scores))

choice = input("what is your choice mate ? right or left?")

while choice != 'left':
    print(choice)
    choice = input("what is your choice mate ? right or left?")
    