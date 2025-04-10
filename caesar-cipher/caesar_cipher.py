import argparse

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode of operation: encrypt or decrypt")
    parser.add_argument("text", help="Text to be encrypted or decrypted")
    parser.add_argument("--shift", type=int, default=3, help="Shift value for encryption or decryption")
    args = parser.parse_args()

    result = caesar_cipher(args.text, args.shift, args.mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
# End of code snippet