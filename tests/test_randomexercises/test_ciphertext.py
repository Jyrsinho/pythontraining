import source.random_exercises.ciphertext as ciphertext



def test_encrypt_ceasar_cypher():
    result = ciphertext.encrypt_ceasar_cypher("BANANA", 3, True, ciphertext.uppercase_alphabet)
    assert result != "BANANA"
    
    
def test_encrypt1(): 
    result = ciphertext.encrypt_ceasar_cypher("BANANA", 3, True, ciphertext.uppercase_alphabet)
    assert result == "EDQDQD"


def test_encrypt2():
    result = ciphertext.encrypt_ceasar_cypher("ZORRO", 1, True, ciphertext.uppercase_alphabet)
    assert result == "APSSP"

def test_encrypt3():
    result = ciphertext.encrypt_ceasar_cypher("ZORRO", 3, True, ciphertext.uppercase_alphabet)
    assert result == "CRUUR"
    

    
def test_encrypt4():
    result = ciphertext.encrypt_ceasar_cypher("KOCHAM CIEBIE", 1, True, ciphertext.uppercase_alphabet)
    assert result == "LPDIBN DJFCJF"


    
def test_encrypt5():
    result = ciphertext.encrypt_ceasar_cypher("HILJAA!!!", 1, True, ciphertext.uppercase_alphabet)
    assert result == "IJMKBB!!!"
    
    
def test_encrypt6():
    result = ciphertext.encrypt_ceasar_cypher("ABBA", 5, False, ciphertext.uppercase_alphabet)
    assert result == "VWWV"

    
def test_decrypt1():
    result = ciphertext.encrypt_ceasar_cypher("CBOBOB", 1, False, ciphertext.uppercase_alphabet)
    assert result == "BANANA"

 
def test_decrypt2():
    result = ciphertext.encrypt_ceasar_cypher("APSSP", 1, False, ciphertext.uppercase_alphabet)
    assert result == "ZORRO"

def test_decryp3():
    result = ciphertext.encrypt_ceasar_cypher("LPDIBN DJFCJF", 1, False, ciphertext.uppercase_alphabet)
    assert result == "KOCHAM CIEBIE"

def test_decrypt4():
    result = ciphertext.encrypt_ceasar_cypher("IJMKBB!!!", 1, False, ciphertext.uppercase_alphabet)
    assert result == "HILJAA!!!"


def test_decrypt5():
    result = ciphertext.encrypt_ceasar_cypher("CRUUR", 3, False, ciphertext.uppercase_alphabet)
    assert result == "ZORRO"


def test_random_cypher_array():
    result = ciphertext.create_random_cypher_array(alphabet= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    assert result != ['A','B','C','D','E','F','G','H']

    
def test_random_cypher_array_should_contain_no_duplicate_values():
    result = ciphertext.create_random_cypher_array(alphabet= ['A', 'B', 'C', 'D'])
    assert result != ['A','B','C','D']
    assert result.count('A') == 1
    assert result.count('B') == 1
    assert result.count('C') == 1
    assert result.count('D') == 1