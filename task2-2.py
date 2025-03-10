from collections import Counter

# English letter frequency (most to least common in normal text)
ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def frequency_analysis(ciphertext):
    """Analyzes letter frequency in ciphertext."""
    ciphertext = ciphertext.upper()
    letter_counts = Counter([char for char in ciphertext if char.isalpha()])
    sorted_letters = [pair[0] for pair in letter_counts.most_common()]
    return sorted_letters

def decrypt_using_frequency(ciphertext, sorted_cipher_letters):
    """Attempts to decrypt based on frequency mapping."""
    decryption_map = {}
    
    # Map most frequent letters in ciphertext to standard English frequencies
    for i, letter in enumerate(sorted_cipher_letters):
        if i < len(ENGLISH_FREQ_ORDER):
            decryption_map[letter] = ENGLISH_FREQ_ORDER[i]
    
    # Perform decryption
    decrypted_text = "".join(decryption_map.get(char, char) for char in ciphertext)
    return decrypted_text

# Example Usage:
ciphertext = input("Enter the encrypted text: ").upper()
sorted_cipher_letters = frequency_analysis(ciphertext)
decrypted_text = decrypt_using_frequency(ciphertext, sorted_cipher_letters)

print("\nPossible Decryption (Frequency-Based):")
print(decrypted_text)
