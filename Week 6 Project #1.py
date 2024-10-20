plaintext = input("Enter the text to encrypt: ")
distance = int(input("Enter the distance value: "))

encrypted_text = ""

for char in plaintext:
    new_char = chr((ord(char) + distance) % 128)
    encrypted_text += new_char

print(f"Encrypted text: {encrypted_text}")
