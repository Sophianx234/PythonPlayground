print('Welcome to the tip calculator!')

totalBill = float(input('What was the total bill? '))
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))
tip = tipPercentage * totalBill/100
billPerPerson = (tip + totalBill)/numPeople

print(f'Each person would pay {round(billPerPerson,3)}')