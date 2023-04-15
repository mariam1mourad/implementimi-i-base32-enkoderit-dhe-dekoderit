import base64

def base32_encode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32encode(data).decode()
    
def base32_decode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32decode(data).decode()

print('--------------------Encoded & Decoded text-----------------------')
text = "abcdefghijklmnopqrstuvwxyz"
encoded_text = base32_encode(text)
print('Encoded text:',encoded_text)    

decoded_text = base32_decode(encoded_text)
print('Decoded text:', decoded_text )


