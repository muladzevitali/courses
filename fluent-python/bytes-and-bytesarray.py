import struct

a = 'my_string'
bytes_a = bytes(a, encoding='utf-8', )
bytes_array_a = bytearray(a, encoding='utf-8')

image_path = r"C:\Users\vmuladze\Downloads\asd546.PNG"
fmt = '<3s3sHH'
with open(image_path, 'rb') as input_stream:
    image = memoryview(input_stream.read())
header = bytes(image[:10])

struct.unpack(fmt, header)
