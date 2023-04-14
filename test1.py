import base64

def base32_encode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32encode(data).decode()

def base32_decode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32decode(data).decode()

text = "Hello, world!"
encoded_text = base32_encode(text)
print(encoded_text)

decoded_text = base32_decode(encoded_text)
print(decoded_text)
