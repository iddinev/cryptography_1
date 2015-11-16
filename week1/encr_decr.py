#!/usr/bin/env python


def hexxor(a, b):     # xor two hex strings of different lengths
    return "".join([hex(int(x, 16) ^ int(y, 16)).replace('0x', '') for (x,y) in zip(a, b)])
    # if len(a) > len(b):
        # return hex(int(a[:len(b)], 16) ^ int(b, 16)).replace('0x', '')
    # else:
        # return hex(int(a, 16) ^ int(b[:len(a)], 16)).replace('0x', '')

def strxor(a, b):     # xor two ascii strings of different lengths
    a = bytes(a, 'ascii').hex()
    b = bytes(b, 'ascii').hex()
    return hexxor(a, b)
    # if len(a) > len(b):
        # return "".join(hex(int(a[:len(b)], 16) ^ int(b, 16)).replace('0x', '')
    # else:
        # return hex(int(a, 16) ^ int(b[:len(a)], 16)).replace('0x', '')


def encrypt(key, msg):  # encrypt ascii string 'msg' using hex string 'key'
    # key = bytes(key, 'ascii').hex()
    msg = bytes(msg, 'ascii').hex()
    # ciphertext = hex(int(key[:len(msg)], 16) ^ int(msg, 16)).replace('0x', '')
    ciphertext = hexxor(key, msg)
    return ciphertext

def decrypt(key, ciphertext):   # decrypt hex string 'ciphertext' with hex string 'key'
    # msg = hex(int(key[:len(ciphertext)], 16) ^ int(ciphertext, 16)).replace('0x', '')
    # print(msg)
    msg = hexxor(key, ciphertext)
    # return bytes.fromhex(msg).decode('ascii', 'backslashreplace')
    return bytes.fromhex(msg)
