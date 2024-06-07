import base64, itertools

def xor_cipher(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, itertools.cycle(key)))

def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

def base64_decode(encoded_string: str) -> str:
    return base64.urlsafe_b64decode(encoded_string.encode()).decode()

def xor_cipher(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, itertools.cycle(key)))

def gjp_encrypt(data):
    return base64.b64encode(xor_cipher(data, "37526").encode()).decode()

def gjp_decrypt(data):
    return xor_cipher(base64.b64decode(data), "37526")
