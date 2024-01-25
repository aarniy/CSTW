from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

message = b'\x00' * 32

def encrypt_message():
    ecb_cipher = AES.new(key, AES.MODE_ECB)
    cbc_cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    ctr_cipher = AES.new(key, AES.MODE_CTR, nonce=get_random_bytes(8))

    ecb_encrypted = ecb_cipher.encrypt(message)
    cbc_encrypted = cbc_cipher.encrypt(message)
    ctr_encrypted = ctr_cipher.encrypt(message)

    return ecb_encrypted, cbc_encrypted, ctr_encrypted

ecb_encrypted, cbc_encrypted, ctr_encrypted = encrypt_message()


output = f"ECB: {ecb_encrypted}\nCBC: {cbc_encrypted}\nCTR: {ctr_encrypted}"
print(output)
