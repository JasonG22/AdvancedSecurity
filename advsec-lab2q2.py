import math

# 2 x 2 key matrix
key = [
    [3, 3],
    [2, 5]
]

def encrypt(plaintext):
    plaintext = plaintext.upper()
    
    # If the plaintext has odd length, add X
    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""

    for i in range(0, len(plaintext), 2):

        # Convert letters to numbers
        x = ord(plaintext[i]) - ord('A')
        y = ord(plaintext[i + 1]) - ord('A')

       
        new_x = (key[0][0] * x + key[0][1] * y) % 26
        new_y = (key[1][0] * x + key[1][1] * y) % 26

       
        ciphertext += chr(new_x + ord('A'))
        ciphertext += chr(new_y + ord('A'))

    return ciphertext


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def decrypt(ciphertext):
 
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]


    determinant = (a * d - b * c) % 26

    
    determinant_inverse = mod_inverse(determinant, 26)


    inverse_key = [
        [(d * determinant_inverse) % 26,
         (-b * determinant_inverse) % 26],

        [(-c * determinant_inverse) % 26,
         (a * determinant_inverse) % 26]
    ]

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        x = ord(ciphertext[i]) - ord('A')
        y = ord(ciphertext[i + 1]) - ord('A')


        new_x = (inverse_key[0][0] * x +
                 inverse_key[0][1] * y) % 26

        new_y = (inverse_key[1][0] * x +
                 inverse_key[1][1] * y) % 26

        plaintext += chr(new_x + ord('A'))
        plaintext += chr(new_y + ord('A'))

    return plaintext


plaintext = input("Enter plaintext: ")

encrypted = encrypt(plaintext)

print("Encrypted:", encrypted)

decrypted = decrypt(encrypted)

print("Decrypted:", decrypted)
