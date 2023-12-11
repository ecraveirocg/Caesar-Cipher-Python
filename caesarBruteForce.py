ciphertext = "tes teste teste, teste"

def caesarBruteForce(cipherText):
    for shift_key in range(0, 25):
        decryptedText = ""
        for char in cipherText:
            if char.islower():
                char_index = ord(char) - ord("a")
                char_unshifted = (char_index - shift_key) % 26 + ord("a")
                char_decrypted = chr(char_unshifted)
                decryptedText += char_decrypted
            else:
                decryptedText += char
        
        print("With a shift of " + str(shift_key) + " the decrypted text is: " + decryptedText)

caesarBruteForce(ciphertext)