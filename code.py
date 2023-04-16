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

print('--------------------Encoded & Decoded numbers--------------------')
numbers = "1234567890"
encoded_numbers = base32_encode(numbers)
print('Encoded numbers:',encoded_numbers)

decoded_numbers = base32_decode(encoded_numbers)
print('Decoded numbers:',decoded_numbers)

print('--------------------Encoded & Decoded symbols--------------------')
symbols = "!@#$%^&*()_+,./"
encoded_symbols = base32_encode(symbols)
print('Encoded symbols:',encoded_symbols)

decoded_symbols = base32_decode(encoded_symbols)
print('Decoded symbols:',decoded_symbols)
