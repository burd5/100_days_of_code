# Caesar Cipher
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text,shift,direction):
    cipher_text = ''
    if shift > 26:
        shift = shift % 26
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            curr_index = alphabet.index(letter)
            new_index = curr_index + shift
            cipher_text += alphabet[new_index]
    print(f"The {direction}d text is {cipher_text}")

    restart = input('Do you want to restart the cipher? Type yes or no.').lower()

    if restart == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
    elif restart == 'no':
        return


caesar(text,shift,direction)