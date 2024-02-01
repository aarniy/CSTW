import os

def encrypt_decrypt_vigenere(message, keystream, encrypt=True, use_nonce=False, nonce_length=16):
    if use_nonce and encrypt:
        nonce = os.urandom(nonce_length)
        nonce_hex = nonce.hex()
        message_with_nonce = nonce_hex + message
    elif use_nonce and not encrypt:
        nonce_hex = message[:nonce_length * 2]
        message = message[nonce_length * 2:]

    result = []
    times_to_repeat = len(message_with_nonce if use_nonce and encrypt else message) // len(keystream) + 1
    repeated_keystream = keystream * times_to_repeat
    keystream_repeated = repeated_keystream[:len(message_with_nonce if use_nonce and encrypt else message)]

    for i, char in enumerate(message_with_nonce if use_nonce and encrypt else message):
        if encrypt:
            result_char = chr((ord(char) + ord(keystream_repeated[i])) % 256)
        else:
            result_char = chr((ord(char) - ord(keystream_repeated[i])) % 256)
        result.append(result_char)

    encrypted_with_nonce = ''.join(result)

    if encrypt:
        return encrypted_with_nonce
    else:
        return ''.join(result)
    

message1 = "Move the tables to the patio as soon as possible!"
message2 = "Move the chairs to the house as soon as possible!"
keystream = "keystream"

# Encrypted with nonce
encrypted_message1_nonce = encrypt_decrypt_vigenere(message1, keystream, encrypt=True, use_nonce=True)
print(encrypted_message1_nonce)

encrypted_message2_nonce = encrypt_decrypt_vigenere(message2, keystream, encrypt=True, use_nonce=True)
print(encrypted_message2_nonce)

# Encrypted without nonce
encrypted_message1 = encrypt_decrypt_vigenere(message1, keystream, encrypt=True, use_nonce=False)
print(encrypted_message1)

encrypted_message2 = encrypt_decrypt_vigenere(message2, keystream, encrypt=True, use_nonce=False)
print(encrypted_message2)
