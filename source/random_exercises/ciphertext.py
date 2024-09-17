import random
import string

test_alphabet = [
    'A', 'B', 'C', 'D', 'E'
]

uppercase_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

punctuation_list = [
    '.', ',', ';', ':', '?', '!', "'", '"', '-', '—', '–', '(', ')',
    '[', ']', '{', '}', '/', '\\', '@', '#', '*', '&', '%', '$', '^',
    '_', '~', '<', '>', '|', '`'
]


def create_random_cypher_array(alphabet):
    """
    Create a random cipher array.
    :param alphabet: array of alphabets
    :return: array of alphabets shuffled randomly
    """
    random_cypher_array = []

    for letter in alphabet:
        random_cypher_array.insert(random.randint(0, len(random_cypher_array)),letter)
    
    return random_cypher_array


def encrypt_ceasar_cypher(plaintext, steps, direction, cypher_array):
    """
    Creates a cipher text from plaintext. 
    :param plaintext: text to be encrypted
    :param steps: cipher steps
    :param direction: cipher direction if true we move forward in alphabets if false we move back. True if we cypher. False if we decypher 
    :return: the cipher text
    """
    ciphertext = ""
    
    if direction == True:                                        
        multiplyer = 1
    else:
        multiplyer = -1
    
    for letter in plaintext:
        if letter in punctuation_list or letter ==" ":
            ciphertext += letter
        else:
            try:
                index = cypher_array.index(letter)
                new_index = (index+steps*multiplyer) % len(cypher_array)
                ciphertext += cypher_array[new_index]
            except ValueError:
                ciphertext += letter
  
    return ciphertext


def check_if_punctuation(letter):
    for punctuation in punctuation_list:
        if letter == punctuation:
            return True



debug = encrypt_ceasar_cypher("DEBA",2, True, test_alphabet)

plaintext = "ZORRO" 
ciphertext = encrypt_ceasar_cypher(plaintext,1,True, uppercase_alphabet)
print(plaintext, "encrypted:", ciphertext)

print("--------------------------------------------------")

random_cypher_array = create_random_cypher_array(uppercase_alphabet)
print(random_cypher_array) 

ciphertext = encrypt_ceasar_cypher(plaintext,2,True, random_cypher_array)
print(plaintext, "encypted; ", ciphertext, " \nencrypted in plaintext:", encrypt_ceasar_cypher(ciphertext,2, False, random_cypher_array)  )