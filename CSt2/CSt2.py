def welcome():
    print("******************************************")
    print("*    Welcome to the Caesar Cipher Tool!   *")
    print("******************************************")
    print("* This tool allows you to encrypt and     *")
    print("* decrypt messages using the Caesar       *")
    print("* cipher algorithm.                       *")
    print("******************************************")
    print("*      Made with ♥ by Nirah Shaheen       *")
    print("******************************************")
    print()

def encrypt(text, shift):
    result = ""

    # Loop through each character in the input text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Leave non-alphabetic characters unchanged
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    # Display the welcome page
    welcome()

    # User input for the message and the shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Perform encryption
    encrypted_message = encrypt(message, shift)
    print(f"\nEncrypted Message: {encrypted_message}")

    # Perform decryption
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")
