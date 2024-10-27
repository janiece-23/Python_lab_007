import sys
from pydoc import plain, plaintext

from string import ascii_uppercase as l
#!/usr/bin/evn python3

##Part 1: Building a Vigenere Square##
def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f'| {" | ".join( row )} |' )
        if i == 0:
            print(f"|{'---|' * len(row)}")

def vigenere(alphabet):
    vigenere_sq_print(vigenere_sq(alphabet))

def vigenere_sq(alphabet):
    result = []
    for i in range(len(alphabet)):
        if i == 0: #insert header row
            result.append(list( ' ' + alphabet[i:] + alphabet[0:i] ))
        result.append(list(alphabet[i] + alphabet[i:] + alphabet[0:i]))
    return result


def letter_to_index(letter, alphabet):
    for i,  l in enumerate(alphabet):
        if l == letter:
            return i
    return -1

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''


def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    c = letter_to_index(cipher_letter, alphabet)
    k = letter_to_index(key_letter, alphabet)
    p = (c - k + len(alphabet)) % len(alphabet)
    return index_to_letter(p, alphabet)


def vigenere_index(key_letter, plaintext_letter, alphabet):
    p = letter_to_index(plaintext_letter, alphabet)
    k = letter_to_index(key_letter, alphabet)
    c = (p + k) % len(alphabet)
    return index_to_letter(c, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    ct = []
    for i, l in enumerate(plaintext):
        if l == ' ':
            ct.append(' ')
        else:
            ct.append(vigenere_index(key[i % len(key)], l, alphabet))
    return ''.join(ct)


def decrypt_vigenere(key, cipher_text, alphabet):
    pt = []
    for i, l in enumerate(cipher_text):
        if l == ' ':
            pt.append(' ')
    else:
        pt.append(undo_vigenere_index(key[i % len(key)], l, alphabet))
    return ''.join(pt)

# Part 4: Application
""" Using the some of the answers found in Mr.Hartman's answers 
for this lab. I am referencing the main structure that is important 
to creating a menu for:

        1.) 'Encryption
        2.)' Decryption
        3.) Dumping Decryption
        4.) Printing Vigenere Square'
        5.) and Quit/Exit
        [1,2,3,4,5] # for valid inputs"""


def execute(menu, skip):
    while True:
        for i in range(len(menu) - skip):
            print( menu[i][0] )
        try:
            selected = int( input( "Please Choose the option you want to complete today: " + str(menu[-1])))
            if selected in menu[-1]:  # When this is selected, this is equal to one of the valid options below.
                selected -= 1 # This the shift index that goes back to 0.
                # Making sure that a function object does exist.#
                if menu[selected][1] is None: #This is assumed that its a quit menu option.
                    return
                if menu[selected][3] is not None:# This is for there being a return list defined.
                    menu[selected][3].append(menu[selected][1](*menu[selected][2]))
                else:    # Just all the function object otherwise.
                    menu[selected][1](*menu[selected][2])
            else:
                 raise ValueError
        except ValueError:
            print("You have made an improper selection. You must choose one of the following: " + str(menu[-1]))


def encryption_menu(key_list, encrypted_list, alphabet):
    plaintext = input( "Please Enter the message you wish to encrypt: ")
    key_index = len(encrypted_list) % len(key_list)
    return encrypt_vigenere( key_list[key_index], plaintext, alphabet)


def decryption_menu(key_list, encrypted_list, alphabet):
    key_len = len(key_list)
    for i, ciphertext in enumerate(encrypted_list):
        key_index = i % key_len
        print(decrypt_vigenere( key_list[key_index], ciphertext, alphabet))


def decryption_dump_menu(encrypted_list):
    for ciphertext in encrypted_list:
        print(ciphertext)

def key_entry_option(alphabet, key_list):
    key_selection = int( input( " How many keys are you  wanting to enter? "))
    for _ in range(key_selection):
        keys = input(" Enter a key: ")
        #TODO: Remove any key characters, that are not in the alphabet.
        key_list.append(keys)








#Testing functions list#
def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 'DAVINCI'
    vig_list = vigenere_sq(alphabet)
    encrypted_list = []
    key_list = []

    # Each Row will be: 'menu-item', 'function object', 'function parameters', 'return list/lists'
    key_menu = [ ['1). Enter Keys', key_entry_option, [alphabet, key_list], None],
        ['2). Quit', None, [0], None],
        [1, 2] ]# Valid options]
    execute(key_menu, 1)

    menu = (
        ['1). Encryption', encryption_menu, [key_list, encrypted_list, alphabet], encrypted_list],
        ['2). Decrypt', decryption_menu, [key_list, encrypted_list, alphabet], None],
        ['3). Dump Decrypt', decryption_dump_menu, [encrypted_list], None],
        ['4). Show Vigenere Square ', vigenere, [alphabet, None],
         '5). Quit/Exit', sys.exit, [0], None],
        [1, 2, 3, 4, 5],  #Valid menu options]
    execute(menu, 1))


    #pretty_print_vigenere(vig_list)
    #print(letter_to_index( 'z' , alphabet))
    #print(index_to_letter(2, alphabet))
    #print(vigenere_index('d', 't', alphabet))
    #print(undo_vigenere_index('v', 'e', alphabet))
    #print(decrypt_vigenere(key, encrypt_vigenere(key, 'the eagle has landed', alphabet), alphabet))
    #print(encrypt_vigenere(key, 'the eagle has landed', alphabet))


if __name__ == '__main__':
    main()


