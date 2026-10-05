# Name: Tyler Vasquez, Dat Nguyun, Sunny Palaco
# Date: 10/6/2026
# Purpose: Runs the Vigenere cipher program.


from vigenere import encrypt, decrypt


def main():
    """Gets input from the user and displays encryption and decryption results."""
    print("========== VIGENERE CIPHER ==========")

    # Get the plaintext and key from the user.
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    # Encrypt the plaintext.
    ciphertext = encrypt(plaintext, key)

    # Decrypt the ciphertext.
    decrypted_text = decrypt(ciphertext, key)

    # Display the results.
    print()
    print("Plaintext:  ", plaintext)
    print("Key:        ", key)
    print("Ciphertext: ", ciphertext)
    print("Decrypted:  ", decrypted_text)


if __name__ == "__main__":
    main()
