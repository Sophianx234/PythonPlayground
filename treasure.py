treasureIslandArt = """ 

 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

 
 """

print(treasureIslandArt)

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
path = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" ')

if path.lower() == 'right':
    print('Fall into a hole.\nGame Over')
if path.lower() == 'left':
    path = input('There is water? swim or wait? ')
if path.lower() == 'swim':
    print('Attacked by trout.\nGameover')
if path.lower() == 'wait':
    path = input('There are doors in the room which one do you want? Red, Blue or Yellow? ')
    if path.lower() == 'red':
        print("Burned by fire.\n Game Over")
    elif path.lower() == 'blue':
        print("Eaten by beasts.\nGame Over")
    elif path.lower() == 'yellow':
        print('You win!')
    else: 
        print("Game Over")
