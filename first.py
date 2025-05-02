def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Choose ASCII base based on uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet using modulo
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result


def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt?: ").lower()
    
    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (an integer): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    mode = 'encrypt' if choice == 'e' else 'decrypt'
    result = caesar_cipher(message, shift, mode)
    print(f"\nThe resulting message is:\n{result}")


if __name__ == "__main__":
    main()
