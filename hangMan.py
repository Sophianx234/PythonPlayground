import random
word_list = ['bucket','caramel','baboon','moon','musketeer']
incompleteWord = random.choice(word_list)
print(incompleteWord)
numReplacement = int(random.random()* len(incompleteWord))-1
target_word = ''
for x in range(numReplacement):
    index =int(random.random()*numReplacement)
    print(index)
    target_word = incompleteWord.replace(incompleteWord[index],'_')
    
print(target_word)
""" guess = input('guessa letter: ').lower() """