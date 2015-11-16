#!/usr/bin/env python


from json import load
import encr_decr


input_cipher = 'ciphertexts.txt'
# input_cipher = 'test_encryptions.txt'
input_words = 'english_most_used_words.csv'
# input_cipher = 'jsontest.txt'
ciphertexts = open(input_cipher, 'r')
english_words = open(input_words, 'r')

most_used_words = load(english_words)
most_used_words = most_used_words[:6]
ciphertexts_list = load(ciphertexts)
ciphertexts_len = [len(x) for x in ciphertexts_list]
max_len_ciphertext = max(ciphertexts_list, key=lambda x: len(x))
print("================")
print("# of max len ciphertext is:", ciphertexts_list.index(max_len_ciphertext) + 1)
# print('max len cipher is', max_len_ciphertext)
# target_ciphertext = ciphertexts_list.pop()
work_list = ciphertexts_list
work_list.remove(max_len_ciphertext)


for cipher in work_list:
    print("--------------")
    print("ciphertext#:", ciphertexts_list.index(cipher) + 1)
    work_cipher = encr_decr.hexxor(max_len_ciphertext, cipher)
    work_len = len(work_cipher)
    for word in most_used_words:
        print("")
        print('next word: "{}"'.format(word))
        add = 'yes'
        while add == 'yes':
            add = input('Add something or change whole word?(a/c/else): ')
            if add == 'a':
                add_word = input('Add what??: ')
                word = word + add_word
            elif add == 'c':
                new_word = input('Change word to what??: ')
                word = new_word
            hex_word = bytes(word, 'ascii').hex()
            print('trial word is: "{}", hex: "{}"'.format(word, hex_word))
            print('..............')
            brk = ""
            for i  in range(0,(len(work_cipher)-len(hex_word))):
                if brk != "":
                    break
                else:
                    has_word = encr_decr.decrypt(hex_word, work_cipher[i:i+len(hex_word)])
                    print('result is: {}/{}, "{}", hex: "{}"'.format(i+1, work_len, has_word.decode('ascii', 'backslashreplace'), has_word.hex()))
                    brk = input("anykey cancels: ")
