from Crypto.Cipher import AES
import binascii

# Function to add PKCS7 padding
def pad(text):
    pad_size = AES.block_size - len(text) % AES.block_size
    return text + bytes([pad_size] * pad_size)

# Function to remove PKCS7 padding
def unpad(text):
    pad_size = text[-1]
    return text[:-pad_size]

Key = b"Sixteen byte key"
PLAIN = b"Secret 16 byte key"

# Pad the plaintext
padded_plaintext = pad(PLAIN)

Cipher = AES.new(Key, AES.MODE_ECB)
ciphertext = Cipher.encrypt(padded_plaintext)

Cipher = AES.new(Key, AES.MODE_ECB)
decrypted_padded_plaintext = Cipher.decrypt(ciphertext)

# Remove padding
decrypted_plaintext = unpad(decrypted_padded_plaintext)

print(binascii.hexlify(ciphertext).decode('utf-8'))
print(decrypted_plaintext.decode('utf-8'))
