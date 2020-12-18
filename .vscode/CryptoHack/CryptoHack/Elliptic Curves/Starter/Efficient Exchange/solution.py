def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

Qx = 4726
nB = 6534
a, b, p = E['a'], E['b'], E['p']

Qysq = (Qx**3 + (a * Qx) + b) % p
assert pow(Qysq, (p - 1) // 2, p) == 1 # Qysq is a quadratic residue of p
Qy = pow(Qysq, (p + 1) // 4, p) # positive or negative versions both work

QA = (Qx, Qy)
S = scalar_mult(nB, QA, E)

shared_secret = S[0] # we only want the x-coordinate of the shared secret
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
