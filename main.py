text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    encrypted_text += alphabet[new_index]