def encrypt(text, shift_key):
    
    cipherText = ""

    for char in text:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_shifted = (char_index + shift_key) % 26 + ord("A")
            char_encrypted = chr(char_shifted)
            cipherText += char_encrypted
        elif char.islower():
            char_index = ord(char) - ord("a")
            char_shifted = (char_index + shift_key) % 26 + ord("a")
            char_encrypted  =chr(char_shifted)
            cipherText += char_encrypted
        else:
            text += char

    return cipherText

def decrypt(cipherText, shift_key):
    
    decryptedText = ""

    for char in cipherText:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_unshifted = (char_index - shift_key) % 26 + ord("A")
            char_decrypted = chr(char_unshifted)
            decryptedText += char_decrypted
        elif char.islower():
            char_index = ord(char) - ord("a")
            char_unshifted = (char_index - shift_key) % 26 + ord("a")
            char_decrypted = chr(char_unshifted)
            decryptedText += char_decrypted
        else:
            decryptedText += char
    
    return decryptedText

text = input("Enter text: ")
shift_key = 10
cipherText = encrypt(text, shift_key)
decryptText = decrypt(cipherText, shift_key)

print("Text: " + text)
print("Character shift: " + str(shift_key))
print("Encrypt text: " + cipherText)
print("Decrypt text: " + decryptText)