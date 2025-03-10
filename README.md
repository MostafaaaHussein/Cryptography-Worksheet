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
