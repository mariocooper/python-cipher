text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text:
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift