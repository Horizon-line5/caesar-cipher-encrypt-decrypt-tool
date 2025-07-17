import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("Caesar Tool", font="slant")
    print("=" * 60)
    print(banner)
    print("=" * 60)

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isupper():
            start = ord('A')
            shifted = (ord(char) - start + shift) % 26
            result.append(chr(start + shifted))
        elif char.islower():
            start = ord('a')
            shifted = (ord(char) - start + shift) % 26
            result.append(chr(start + shifted))
        else:
            result.append(char)
    return ''.join(result)

def main():
    print_banner()
    
    action = input("Choose an action - encrypt (e) or decrypt (d): ").strip().lower()
    if action not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if action == 'e':
        encrypted = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher(message, -shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()