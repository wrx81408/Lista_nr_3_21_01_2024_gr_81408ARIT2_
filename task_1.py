import base64

def encode_base64(text):
    encoded_text = base64.b64encode(text.encode('utf-8'))
    return encoded_text.decode('utf-8')

original_text = "2023 was probably the warmest year in the last 125 thousand years"
encoded_text = encode_base64(original_text)
print("Encoded text:", encoded_text)
decoded_text = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
print("Decoded text:", decoded_text)

#Encoded text: MjAyMyB3YXMgcHJvYmFibHkgdGhlIHdhcm1lc3QgeWVhciBpbiB0aGUgbGFzdCAxMjUgdGhvdXNhbmQgeWVhcnM=
#Decoded text: 2023 was probably the warmest year in the last 125 thousand years
