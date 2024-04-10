import base64
import msgpack

# Base64 encoded MessagePack data
encoded_message = "halzZW5zb3JfaWSmMTI2NTMxrnNlbnNvcl92ZXJzaW9upUZSLXY4qHBsYW50X2lkzgAAAAOkdGltZbQyMDI0LTA0LTEwVDE2OjMzOjA4WqhtZWFzdXJlc4KrdGVtcGVyYXR1cmWlMTTCsEOoaHVtaWRpdGWjMTgl"

# First, decode from Base64
base64_decoded_bytes = base64.b64decode(encoded_message)

# Then, unpack the MessagePack data
decoded_data = msgpack.unpackb(base64_decoded_bytes)

print(decoded_data)
