# -*- coding: utf-8 -*-
import platform
import sys
from os import system
import os.path
import hashfunctions

try:
    from googlesearch import search
except ImportError:
    print 'ImportError: google module not found. Try this "pip install google" or "apt-get install google"'
    if platform.system() == "Windows":
        system("pip install google")
    else:
        system('apt-get install google')
    exit()

if platform.system() == "Windows":
    system("cls")
else:
    system('clear')

print """$$\   $$\                     $$\                             $$\       $$\   $$\     v2.0      $$\\
$$ |  $$ |                    $$ |                            $$ |      \__|  $$ |              $$ |
$$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\         $$$$$$\        $$$$$$$\  $$\ $$$$$$\    $$$$$$$\ $$$$$$$\\
$$$$$$$$ | \____$$\ $$  _____|$$  __$$\        \____$$\       $$  __$$\ $$ |\_$$  _|  $$  _____|$$  __$$\\
$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |       $$$$$$$ |      $$ |  $$ |$$ |  $$ |    $$ /      $$ |  $$ |
$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |      $$  __$$ |      $$ |  $$ |$$ |  $$ |$$\ $$ |      $$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |      \$$$$$$$ |      $$$$$$$  |$$ |  \$$$$  |\$$$$$$$\ $$ |  $$ |
\__|  \__| \_______|\_______/ \__|  \__|       \_______|      \_______/ \__|   \____/  \_______|\__|  \__|
                                                                             coded by Super23 (aka Lord13)
"""

def show_help():
    print('searches for the given hash value in some online services\n\n'
          'USAGE:\n'
          '    {what_calld_me} HASHFUNCTION checksum\n\n'
          'OPTIONS:\n'
          '    --help'
          '    HASHFUNCION  indicates the type of the checksum\n'
          '    checksum     the checksum itself\n\n'
          'ACCEPTED HASH FUNCTIONS:\n'
          '    MD5          most commom hashing function'
          ''.format(what_calld_me=os.path.basename(sys.argv[0])))
    sys.exit(1)

def code_error():
    try:
        hashtype = sys.argv[1]
        checksum = sys.argv[2]
    except IndexError:
        return 1

    if hashtype == '--help':
        show_help()

    if hashtype not in hashfunctions.supported_functions:
        return 2

    checksum_instance = hashfunctions.supported_functions[hashtype](checksum)

    if not checksum_instance.check():
        return 3
    
    return False


def main():
    code_errors = {
        1: "[!] TOO FEW ARGUMENTS",
        2: '[!] FUNCTION NOT SUPPORTED YET',
        3: '[!] INVALID CHECKSUM'
    }

    code_error_ = something_went_wrong = code_error()

    if something_went_wrong:
        print (code_errors[code_error_])
        show_help()


    hashtype = sys.argv[1]
    checksum = sys.argv[2]

    print("[*] Identified function: " + hashtype)
    print("[*] Identified checksum: " + checksum)
    print('\n'+"==="*20)

    supported_functions = hashfunctions.supported_functions

    print("[?] SEARCHING FOR YOUR CHECKSUM...")
    decrypted_hash = supported_functions[hashtype](checksum).decrypt()

    print('\n'+"==="*20)

    for website, found_original in decrypted_hash.items():
        if found_original:
            print("[+] Found on {website}: {original}".format(website=website, original=found_original))


if __name__ == '__main__':
    main()
