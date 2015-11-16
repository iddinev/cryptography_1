#!/usr/bin/env python


from json import load
import encr_decr

input_cipher = 'test_encryptions.txt'
ciphertexts = open(input_cipher, 'r')

ciphertexts_list = load(ciphertexts)

key = ciphertexts_list.pop(len(ciphertexts_list) - 1)

output = encr_decr.decrypt(key,ciphertexts_list[0])
print(output)
output = encr_decr.decrypt(key,ciphertexts_list[1])
print(output)
print('xor of 2 is:', encr_decr.hexxor(ciphertexts_list[1],ciphertexts_list[0]))
