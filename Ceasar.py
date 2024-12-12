alphabets = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def encrypt(text,shift):
    encoded = []
    for x in text:
        x in alphabets
        if x == ' ':
            continue
        encoded.append(alphabets[alphabets.index(x)+shift])
    return ''.join(encoded)
def decrypt(text,shift):
    decoded = []
    for x in text:
        x in alphabets
        if x == ' ':
            continue
        decoded.append(alphabets[alphabets.index(x)-shift])
    return ''.join(decoded)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
if direction == 'encode':
    text = input('Type your message: ')
elif direction == 'decrypt':
    text = input('Type encrypted message: ')

shift = int(input("Type the shift number: "))
if direction.strip() == 'encode':
    print(encrypt(text,shift))
if direction == 'decrypt':
    print(decrypt(text,shift))
