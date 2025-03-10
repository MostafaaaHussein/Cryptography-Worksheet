import itertools

def prepare_key_square(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(keyword.upper().replace("J", "I") + alphabet))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def find_position(letter, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            new_text += "X"
        elif i + 1 < len(text):
            new_text += text[i + 1]
            i += 1
        i += 1
    if len(new_text) % 2 != 0:
        new_text += "X"
    return new_text

def encrypt_decrypt(text, key_square, encrypt=True):
    text = prepare_text(text)
    result = ""
    for a, b in zip(text[0::2], text[1::2]):
        row1, col1 = find_position(a, key_square)
        row2, col2 = find_position(b, key_square)
        
        if row1 == row2:  # نفس الصف
            result += key_square[row1][(col1 + (1 if encrypt else -1)) % 5]
            result += key_square[row2][(col2 + (1 if encrypt else -1)) % 5]
        elif col1 == col2:  # نفس العمود
            result += key_square[(row1 + (1 if encrypt else -1)) % 5][col1]
            result += key_square[(row2 + (1 if encrypt else -1)) % 5][col2]
        else:  # تبديل المستطيل
            result += key_square[row1][col2]
            result += key_square[row2][col1]
    return result

def main():
    keyword = input("Enter the keyword: ")
    key_square = prepare_key_square(keyword)
    print("Playfair Key Square:")
    for row in key_square:
        print(" ".join(row))
    
    choice = input("Encrypt or Decrypt (E/D): ").upper()
    text = input("Enter the text: ")
    
    if choice == "E":
        result = encrypt_decrypt(text, key_square, encrypt=True)
        print("Encrypted Text:", result)
    elif choice == "D":
        result = encrypt_decrypt(text, key_square, encrypt=False)
        print("Decrypted Text:", result)
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()
