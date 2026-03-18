# Encryption program in Python

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Chars: {chars}")
print(f"Key: {key}")

# Encryption
plain_text = input("Enter a message to encrypt: ")
encrypted_txt = ""

for char in plain_text:
    index = chars.index(char)
    encrypted_txt += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {encrypted_txt}")


# Decrypting
encrypted_txt = input("Enter a message to encrypt: ")
plain_text = ""

for char in encrypted_txt:
    index = key.index(char)
    plain_text += chars[index]

print(f"Encrypted text: {encrypted_txt}")
print(f"Decrypted text: {plain_text}")