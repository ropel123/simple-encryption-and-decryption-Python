import abc
from base64 import *
nama = 'satrio'
key = 'abc'
c = ''
for i in range(len(nama)):
    c += chr(ord(nama[i]) ^ ord(key[i % len(key)]))

print('Cipher'+'adalah' + c)

d = ''
for j in range(len(c)):
    d += chr(ord(c[j]) ^ ord(key[j % len(key)]))

print('Hasil Decode adalah ', d)
