# RC4 Stream Cipher

# Vector S plain Txt
def rc4_init(key):
    # Vector S got 256 data particles
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]  # Swap S[i] & S[j]
    return S

# Keystream generation from S
def rc4_generate_keystream(S, length):
    keystream = []
    i = 0
    j = 0
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap S[i] & S[j]
        keystream.append(S[(S[i] + S[j]) % 256])
    return keystream

# RC4
def rc4_encrypt_decrypt(text, key):
    # Change to ASCII chars
    key_bytes = [ord(c) for c in key]
    
    
    S = rc4_init(key_bytes)
    
    # Keystream Generation
    keystream = rc4_generate_keystream(S, len(text))
    
    # XOR the plain txt with keystream
    result = ''.join(chr(ord(c) ^ keystream[i]) for i, c in enumerate(text))
    
    return result, keystream

# Key
key = "hadongban"

# Plain Txt
text = "Hanoi University of Science and Technology"

# Encryption
ciphertext, keystream = rc4_encrypt_decrypt(text, key)

# Resultzzz
print("Original Text: ", text)
print("Ciphertext (in ASCII): ", [ord(c) for c in ciphertext])
print("Keystream (in ASCII): ", keystream)
print("Ciphertext (text): ", ciphertext)

