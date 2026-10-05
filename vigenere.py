# Name: Tyler Vasquez, Dat Nguyun, Sunny Palaco
# Date: 10/6/2026
# Purpose: Provides encryption and decryption functions for a Vigenere cipher.


def encrypt(plaintext, key):
    """Encrypts plaintext using the Vigenere cipher and the given key."""
    ciphertext = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isalpha():
            # Get the corresponding key character.
            key_char = key[i % len(key)]

            # Convert letters to numbers from 0 to 25.
            plain_value = ord(char.upper()) - ord("A")
            key_value = ord(key_char.upper()) - ord("A")

            # Add the values and wrap around after Z.
            cipher_value = (plain_value + key_value) % 26

            # Convert the number back into a letter.
            cipher_char = chr(cipher_value + ord("A"))

            ciphertext += cipher_char
        else:
            # Keep spaces and punctuation unchanged.
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):
    """Decrypts ciphertext using the Vigenere cipher and the given key."""
    plaintext = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if char.isalpha():
            # Get the corresponding key character.
            key_char = key[i % len(key)]

            # Convert letters to numbers from 0 to 25.
            cipher_value = ord(char.upper()) - ord("A")
            key_value = ord(key_char.upper()) - ord("A")

            # Subtract the key value to reverse the encryption.
            plain_value = (cipher_value - key_value) % 26

            # Convert the number back into a letter.
            plain_char = chr(plain_value + ord("A"))

            plaintext += plain_char
        else:
            # Keep spaces and punctuation unchanged.
            plaintext += char

    return plaintext
