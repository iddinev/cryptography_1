#!/usr/bin/env python


import json
import encr_decr

MSGS = ('and the a', 'be ofaaaa')
# MSGS = ('dev', 'all')

# def strxor(a, b):     # xor two ascii strings of different lengths.
    # a = bytes(a, 'ascii').hex()
    # b = bytes(b, 'ascii').hex()
    # if len(a) > len(b):
        # return hex(int(a[:len(b)], 16) ^ int(b, 16))
    # else:
        # return hex(int(a, 16) ^ int(b[:len(a)], 16))

def random(size=16):
    return open("/dev/urandom", 'rb').read(size)

# def encrypt(key, msg):
    # # key = bytes(key, 'ascii').hex()
    # msg = bytes(msg, 'ascii').hex()
    # ciphertext = hex(int(key[:len(msg)], 16) ^ int(msg, 16)).replace('0x', '')
    # return ciphertext

# def decrypt(key, ciphertext):
    # msg = hex(int(key[:len(ciphertext)], 16) ^ int(ciphertext, 16)).replace('0x', '')
    # return bytes.fromhex(msg).decode('ascii')

def main():
    key = random(50).hex()
    print('key is', key)
    ciphertexts = [encr_decr.encrypt(key, msg) for msg in MSGS]

    with open('test_encryptions.txt', 'w') as fl:
        # ciphertexts.append(key)
        json.dump(ciphertexts, fl)

main()

