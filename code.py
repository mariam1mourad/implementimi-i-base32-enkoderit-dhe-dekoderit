import base64

def base32_encode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32encode(data).decode()
    
 def base32_decode(data):
    if isinstance(data, str):
        data = data.encode()
    return base64.b32decode(data).decode()
