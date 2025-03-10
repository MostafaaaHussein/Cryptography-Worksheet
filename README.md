# Cryptography-Worksheet
Monoalphabetic &amp; Playfair Ciphers
# Brute Force Attack on Monoalphabetic Cipher

## Description
This project implements a brute-force attack on a monoalphabetic substitution cipher. A monoalphabetic cipher replaces each letter in the plaintext with another letter in a fixed but arbitrary mapping. The program attempts to decrypt an encrypted message by trying all possible permutations of the alphabet.

## Features
- Takes an encrypted message as input.
- Tries all possible key permutations to decrypt the message.
- Outputs all possible decrypted texts.

## How It Works
1. The program defines a function `decrypt` that decrypts a given ciphertext using a key mapping.
2. The `brute_force_attack` function generates all possible key permutations of the alphabet.
3. Each permutation is applied to attempt decryption, and the results are printed.
4. The user enters an encrypted message, which is converted to uppercase before decryption.

## Code Implementation
```python
import itertools

def decrypt(ciphertext, key_mapping):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    for char in ciphertext:
        if char in alphabet:
            decrypted_text += key_mapping[char]
        else:
            decrypted_text += char  # Keep non-alphabet characters unchanged
    return decrypted_text


def brute_force_attack(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    permutations = itertools.permutations(alphabet)  # Generate all possible key mappings

    for perm in permutations:
        key_mapping = {perm[i]: alphabet[i] for i in range(26)}  # Create decryption mapping
        decrypted_text = decrypt(ciphertext, key_mapping)
        print(f"Possible Decryption: {decrypted_text}")

# Example usage:
ciphertext = input("Enter the encrypted message: ").upper()
brute_force_attack(ciphertext)
```

## Example Output
```
Enter the encrypted message: mostafa
Possible Decryption: MOSTAFA
Possible Decryption: MOSTAFA
Possible Decryption: MOSTAFA
...
```
*(Note: The same output appears multiple times because of redundant permutations.)*

## Image Example
Below is an example output of the program:

![Image](https://github.com/user-attachments/assets/e84a505b-6ec1-4a33-a36c-11634f227b74)
## Limitations
- The approach is impractical for large texts due to the factorial complexity (26! possible permutations).
- This method is only feasible for very short encrypted texts.

## Future Improvements
- Implement frequency analysis to reduce the number of permutations tested.
- Optimize the brute-force approach using heuristics.



## Cryptanalysis of Monoalphabetic Cipher using Frequency Analysis

## Overview
This project performs cryptanalysis on a **monoalphabetic cipher** using **letter frequency analysis**. Monoalphabetic ciphers substitute each letter in the plaintext with another letter, remaining consistent throughout the text. By analyzing the frequency of letters in the ciphertext and comparing it to typical English letter frequency, this program attempts to **decrypt the text**.

## Features
- Takes an **encrypted text** as input.
- Performs **frequency analysis** to determine the most common letters.
- Maps the most frequent letters in ciphertext to standard **English letter frequency order**.
- Outputs a **possible decryption** of the text.

## How It Works
1. **Frequency Analysis**: 
   - Counts the occurrences of each letter in the ciphertext.
   - Sorts them from most to least frequent.
2. **Decryption Attempt**:
   - Maps the most frequent letters in the ciphertext to the standard English frequency order (ETAOINSHRDLCUMWFGYPBVKJXQZ).
   - Replaces letters accordingly to produce a possible plaintext.

## Code Explanation
### **Imports**
```python
from collections import Counter
```
- Imports `Counter` from the `collections` module to count occurrences of each letter in the ciphertext.

### **Define English Letter Frequency Order**
```python
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
```
- Stores the most common letters in the English language from most frequent (`E`) to least frequent (`Z`).
- This will help in mapping the ciphertext letters to likely plaintext letters.

### **Function: `frequency_analysis(ciphertext)`**
```python
def frequency_analysis(ciphertext):
    """Analyzes letter frequency in ciphertext."""
```
- Defines a function to analyze letter frequency in the input ciphertext.

```python
    ciphertext = ciphertext.upper()
```
- Converts all letters to uppercase to ensure case consistency.

```python
    letter_counts = Counter([char for char in ciphertext if char.isalpha()])
```
- Uses `Counter` to count occurrences of each letter in the ciphertext.
- Ignores non-alphabetic characters (e.g., spaces, punctuation).

```python
    sorted_letters = [pair[0] for pair in letter_counts.most_common()]
```
- Sorts letters in descending order of frequency.
- Extracts only the letters from the `(letter, count)` tuples.

```python
    return sorted_letters
```
- Returns the sorted list of most frequent letters.

### **Function: `decrypt_using_frequency(ciphertext, sorted_cipher_letters)`**
```python
def decrypt_using_frequency(ciphertext, sorted_cipher_letters):
    """Attempts to decrypt based on frequency mapping."""
```
- Defines a function to attempt decryption using frequency mapping.

```python
    decryption_map = {}
```
- Creates an empty dictionary to store the mapping between ciphertext letters and the most common English letters.

```python
    # Map most frequent letters in ciphertext to standard English frequencies
    for i, letter in enumerate(sorted_cipher_letters):
        if i < len(ENGLISH_FREQ_ORDER):
            decryption_map[letter] = ENGLISH_FREQ_ORDER[i]
```
- Loops through the sorted list of ciphertext letters.
- Maps them to the corresponding letter from `ENGLISH_FREQ_ORDER` based on frequency.

```python
    decrypted_text = "".join(decryption_map.get(char, char) for char in ciphertext)
```
- Replaces each letter in the ciphertext using `decryption_map`.
- Keeps non-alphabetic characters unchanged.

```python
    return decrypted_text
```
- Returns the decrypted text.

### **Main Program Execution**
```python
ciphertext = input("Enter the encrypted text: ").upper()
```
- Takes user input for the encrypted text.
- Converts it to uppercase.

```python
sorted_cipher_letters = frequency_analysis(ciphertext)
```
- Calls `frequency_analysis()` to determine the most common letters in the ciphertext.

```python
decrypted_text = decrypt_using_frequency(ciphertext, sorted_cipher_letters)
```
- Calls `decrypt_using_frequency()` to map and decrypt the text.

```python
print("\nPossible Decryption (Frequency-Based):")
print(decrypted_text)
```
- Displays the possible decrypted text.



## Screenshot of Program Output
![Image](https://github.com/user-attachments/assets/ba6e71af-b003-42db-9448-dd1da0b58425)
## Limitations
- This method provides a **statistical best guess**; it may not always produce the correct plaintext.
- It does not account for **context or grammar**, so manual adjustments may be needed.

## Future Improvements
- Implement **bigram and trigram frequency analysis** for better accuracy.
- Allow user **manual letter swaps** to refine the decryption.

# Playfair Cipher - Encryption & Decryption

## Overview
This program implements the Playfair cipher, a classical encryption method that encrypts and decrypts messages using a 5x5 key square. The program takes a keyword, generates a Playfair matrix, and allows users to encrypt or decrypt a message based on Playfair cipher rules.

---

## Features
- Takes a keyword from the user.
- Generates and displays the 5x5 Playfair key square.
- Encrypts or decrypts a given plaintext or ciphertext.
- Follows Playfair cipher rules for processing pairs of letters.

---

## Code Explanation (Line by Line)

```python
import itertools
```
- This imports the `itertools` module, though it is not used in the program.

```python
def prepare_key_square(keyword):
```
- This function generates the 5x5 Playfair matrix based on a given keyword.

```python
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
```
- The alphabet is defined without 'J' since 'I' and 'J' are treated as the same letter in the Playfair cipher.

```python
    key = "".join(dict.fromkeys(keyword.upper().replace("J", "I") + alphabet))
```
- The keyword is converted to uppercase, and 'J' is replaced with 'I'.
- The `dict.fromkeys()` method removes duplicate letters while maintaining order.

```python
    return [list(key[i:i+5]) for i in range(0, 25, 5)]
```
- The key string is split into a 5x5 matrix (list of lists).

```python
def find_position(letter, key_square):
```
- This function finds the row and column index of a letter in the Playfair key square.

```python
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
```
- It iterates through the 5x5 matrix to locate the given letter and returns its row and column indices.

```python
def prepare_text(text):
```
- This function prepares the plaintext by formatting it according to Playfair cipher rules.

```python
    text = text.upper().replace("J", "I").replace(" ", "")
```
- The input text is converted to uppercase, and spaces are removed.

```python
    new_text = ""
    i = 0
    while i < len(text):
```
- A loop iterates through the text to pair letters properly.

```python
        new_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            new_text += "X"
```
- If two consecutive letters are the same, an 'X' is inserted between them.

```python
        elif i + 1 < len(text):
            new_text += text[i + 1]
            i += 1
```
- Otherwise, the next letter is added to form a valid pair.

```python
        i += 1
```
- The loop continues processing the text.

```python
    if len(new_text) % 2 != 0:
        new_text += "X"
```
- If the final text length is odd, an 'X' is appended to make it even.

```python
    return new_text
```
- The formatted text is returned.

```python
def encrypt_decrypt(text, key_square, encrypt=True):
```
- This function encrypts or decrypts the text based on Playfair cipher rules.

```python
    text = prepare_text(text)
    result = ""
```
- The text is prepared, and an empty string is initialized for the result.

```python
    for a, b in zip(text[0::2], text[1::2]):
```
- The text is processed in pairs.

```python
        row1, col1 = find_position(a, key_square)
        row2, col2 = find_position(b, key_square)
```
- The positions of the letters are determined.

```python
        if row1 == row2:
```
- If the letters are in the same row:

```python
            result += key_square[row1][(col1 + (1 if encrypt else -1)) % 5]
            result += key_square[row2][(col2 + (1 if encrypt else -1)) % 5]
```
- The letters are shifted right for encryption and left for decryption.

```python
        elif col1 == col2:
```
- If the letters are in the same column:

```python
            result += key_square[(row1 + (1 if encrypt else -1)) % 5][col1]
            result += key_square[(row2 + (1 if encrypt else -1)) % 5][col2]
```
- The letters are shifted downward for encryption and upward for decryption.

```python
        else:
```
- If the letters form a rectangle:

```python
            result += key_square[row1][col2]
            result += key_square[row2][col1]
```
- The letters are swapped diagonally.

```python
    return result
```
- The encrypted or decrypted text is returned.

```python
def main():
```
- This function runs the program interactively.

```python
    keyword = input("Enter the keyword: ")
    key_square = prepare_key_square(keyword)
```
- The user enters a keyword, and the Playfair matrix is generated.

```python
    print("Playfair Key Square:")
    for row in key_square:
        print(" ".join(row))
```
- The Playfair matrix is displayed.

```python
    choice = input("Encrypt or Decrypt (E/D): ").upper()
    text = input("Enter the text: ")
```
- The user chooses encryption or decryption and inputs the text.

```python
    if choice == "E":
        result = encrypt_decrypt(text, key_square, encrypt=True)
        print("Encrypted Text:", result)
```
- If encryption is selected, the text is encrypted and displayed.

```python
    elif choice == "D":
        result = encrypt_decrypt(text, key_square, encrypt=False)
        print("Decrypted Text:", result)
```
- If decryption is selected, the text is decrypted and displayed.

```python
    else:
        print("Invalid choice!")
```
- If an invalid choice is entered, an error message is displayed.

```python
if __name__ == "__main__":
    main()
```
- This ensures the script runs when executed directly.

---

## Example Output
![Image](https://github.com/user-attachments/assets/3e80f7f0-a378-4f96-b036-5ea3dfecec96)
---

## Usage
Run the script in a Python environment, enter a keyword, and follow the prompts to encrypt or decrypt a message.


