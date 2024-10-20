encrypted_text = input("Enter the text to decrypt: ")
distance = int(input("Enter the distance value: "))

plaintext = ""

for char in encrypted_text:
    new_char = chr((ord(char) - distance) % 128)
    plaintext += new_char

print(f"Decrypted text: {plaintext}")
