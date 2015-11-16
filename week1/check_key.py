#!/usr/bin/env python


from json import load
import encr_decr


input_cipher = 'ciphertexts.txt'
ciphertexts = open(input_cipher, 'r')
ciphertexts_list = load(ciphertexts)
ciphertexts_len = [len(x) for x in ciphertexts_list]

print("================")
print("number of ciphertexts is: ", len(ciphertexts_list))
while True:
    print("--------------")
    num_cipher = input("# of cipher: ")
    ciphertext = ciphertexts_list[int(num_cipher) - 1]
    print('len of cipher is: ',len(ciphertexts_list[int(num_cipher) - 1]))
    pos = input("# of position in ciphertext: ")
    part_key = input("partial key: ")
    output = encr_decr.decrypt(part_key, ciphertext[int(pos) + 1: len(part_key)])
    print('output is: ',output.decode('ascii', 'backslashreplace'))
