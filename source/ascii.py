import string

# Pienet kirjaimet
lowercase_alphabet = list(string.ascii_lowercase)
lowercase_ascii_values = [ord(char) for char in lowercase_alphabet]

# Isot kirjaimet
uppercase_alphabet = list(string.ascii_uppercase)
uppercase_ascii_values = [ord(char) for char in uppercase_alphabet]

print("Lowercase alphabet and their ASCII values:")
for char, ascii_value in zip(lowercase_alphabet, lowercase_ascii_values):
    print(f"{char}: {ascii_value}")

print("\nUppercase alphabet and their ASCII values:")
for char, ascii_value in zip(uppercase_alphabet, uppercase_ascii_values):
    print(f"{char}: {ascii_value}")
