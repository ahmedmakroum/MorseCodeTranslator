"""
Morse Code Translator

This script provides functionality to translate text to Morse code and
Morse code back to text. It includes a dictionary for Morse code mappings,
functions to encrypt text to Morse code, and decrypt Morse code to text.

Usage:
    - Encrypt text to Morse code using the `encrypt_to_morse` function.
    - Decrypt Morse code to text using the `decrypt_from_morse` function.

Example:
    text = "HELLO WORLD"
    morse_code = encrypt_to_morse(text)
    print(f"Text: {text}\nMorse Code: {morse_code}")

    morse_code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    text = decrypt_from_morse(morse_code)
    print(f"Morse Code: {morse_code}\nText: {text}")
"""

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

# Function to encrypt text to Morse code
def encrypt_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '  # for characters not in the dictionary
    return morse_code.strip()

# Function to decrypt Morse code to text
def decrypt_from_morse(morse_code):
    text = ''
    for code in morse_code.split(' '):
        if code in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[code]
        else:
            text += ' '  # for spaces between words
    return text

# Main function to interact with the user
def main():
    choice = input("Do you want to (E)ncrypt text to Morse code or (D)ecrypt Morse code to text? (E/D): ").upper()
    
    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        morse_code = encrypt_to_morse(text)
        print(f"Text: {text}\nMorse Code: {morse_code}")
    elif choice == 'D':
        morse_code = input("Enter the Morse code to decrypt (use space to separate each Morse character): ")
        text = decrypt_from_morse(morse_code)
        print(f"Morse Code: {morse_code}\nText: {text}")
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

# Run the main function
if __name__ == "__main__":
    main()
