plaintext = "explanation"
key = "leg"
ciphertext = ""

for i in range(len(plaintext)):
    
    letter = plaintext[i]  

    k = key[i % len(key)]

    p_num = ord(letter) - ord('a')
    k_num = ord(k) - ord('a')

    # Vigenère formula
    c_num = (p_num + k_num) % 26

    # Convert number back to a letter
    c = chr(c_num + ord('a'))

    # Add it to the ciphertext
    ciphertext += c

print(ciphertext)