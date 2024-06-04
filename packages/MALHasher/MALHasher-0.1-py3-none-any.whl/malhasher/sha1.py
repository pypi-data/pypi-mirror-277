# mrhashing/sha1.py

def left_rotate(value, amount):
    return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF

def sha1(message):
    # Initial hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) * 8 + 64) % 512 != 0:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='big')

    # Process the message in successive 512-bit chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = [int.from_bytes(chunk[j:j + 4], byteorder='big') for j in range(0, 64, 4)]

        for j in range(16, 80):
            w.append(left_rotate((w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]), 1))

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return f'{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}'

def sha1_file(filepath):
    with open(filepath, 'rb') as f:
        message = f.read()
    return sha1(message)
