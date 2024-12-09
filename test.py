import datetime

items = ['Avocado','Pear','Pomegrade','Peaches','Tangerine']
items.append('Pineapple')



numbers = [16,100,10,2,66,43,32,11]


animeChar = ['Boruto','Deku','Bakugo','Sarada','Saitama','Kankuro']
# animeChar.sort(key = str.upper)

newAnimeList = animeChar
newAnimeList.append('Dormamu')
print(newAnimeList)
print(animeChar)

myTuple = ('Damian','Gohan','Sarada')
x = list(myTuple)
x[1] = 'Fareeda'
myTuple = tuple(x)
print(myTuple)

myDictionary = dict(name = "Boruto", age =  32)

for x in myDictionary:
    print(myDictionary[x])

x = 5 
y = 6 

print(x) if x >y else print(y)

i = 0 
while i< 10:
    if i == 6:
        print("hooray it's six")
        
    print(i)
    i= i+1
    
def test(*num):
    print(num[2])
    
test(6,4,2,8)

class greet:
    def __init__(self,name, Gtype):
        self.name = name
        self.Gtype = Gtype
        
    def __str__(self):
        print(f'Good {self.Gtype} {self.name}')

g1 = greet('Boruto','Morning')


x = datetime.datetime.now()
print(x.strftime('%A'))