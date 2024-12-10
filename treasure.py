treasureIslandArt = """ 

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

 
 """

print(treasureIslandArt)

print('Welcome to the Island.\nYour mission is to find the treasure')
path = input("Choose a path: left or right ? ")

if path.lower() =='left':
    path = input('Swim or wait')
    if path.lower() == 'wait':
        path = input('Which door? Blue or Red?')
    else :
        print("Attacked by trout.\nGame Over")
        if path.lower() == 'blue': 
            print('Eaten by beasts.\nGame Over')
        elif path.lower() == 'red':
            print('Burned by fire.\nGame Over')
        elif path.lower() =='yellow':
            print('You Win!')
        else: 
            print('Game Over')
else: print("Fall into a hole.\nGame Over")