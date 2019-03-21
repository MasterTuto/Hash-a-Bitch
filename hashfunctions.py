#coding: utf-8
import requests
from hashlib import *
import re

class MD5():
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        def check(self):
            return re.match(r"[A-Za-z\d]{32}", self.checksum)

        def __init__(self, checksum):
            self.checksum = checksum

            self.claveycontrasena_url = 'http://descodificar.claveycontraseña.es/'+self.checksum+'.html'
            self.md5decoder_url = 'http://md5decoder.org/'+self.checksum
            self.gromweb_url = 'https://md5.gromweb.com/?md5='+self.checksum


        def decrypt(self):
            sites_to_get_from = [
                self.get_from_claveylacontrasena,
                self.get_from_md5decoder,
                self.get_from_gromweb
                #self.get_from_md5decrypt
            ]

            results = {}

            for site in sites_to_get_from:
                decryption_result = site()

                if decryption_result:
                    results[decryption_result[0]] = decryption_result[1]

            return results


        def get_from_claveylacontrasena(self):
            try:
                claveycontrasena = requests.get(self.claveycontrasena_url, headers=self.headers).text
            except requests.exceptions.ConnectionError:
                return False

            try:
                if 'showkey' in claveycontrasena:
                    i = 1
                    k = 'a'
                    while k[-1] != ')':
                        k = claveycontrasena[claveycontrasena.index('showkey'):claveycontrasena.index('showkey')+len('showkey')+i]
                        i += 1
                    return 'claveycontrasena.es:', k.split('\'')[1]
                else:
                    return False #"claveycontrasena.es: not found"
            except:
                return False # "claveycontrasena.es: ERROR WHILE CONNECTING"

        def get_from_md5decoder(self):
            md5decoder = requests.get(self.md5decoder_url, headers=self.headers).text
            
            try:
                if 'md2' in md5decoder:
                    i = 1
                    k = 'a'
                    while k[-1] != ')':
                        k = md5decoder[md5decoder.index('md2'):md5decoder.index('md2')+len('md2')+i]
                        i += 1
                    return 'md5decoder.org:', k
                else:
                    return False #'md5decoder.org: not found', None
            except:
                return False #"ERROR WHILE CONNECTING"

        def get_from_gromweb(self):
            gromweb = requests.get(self.gromweb_url, headers=self.headers).text

            if '"long-content string">' in gromweb:
                original_value = gromweb.split('"long-content string">')[1].split('</em>')[0]

            return 'gromweb', original_value
            
        def get_from_md5decrypt(self):
            try:
                for url in search(self.checksum, stop=5):
                    if 'md5decrypt.org' in url:
                        md5decrypt = requests.get(url, headers=self.headers).text
                        if 'style=\'color:red;\'>' in md5decrypt:
                            i = 1
                            k = 'a'
                            while k[-1] != '<':
                                k = md5decrypt[md5decrypt.index('style=\'color:red;\'>'):md5decrypt.index('style=\'color:red;\'>')
                                               + len('style=\'color:red;\'>') + i]
                                i += 1
                            return 'md5decrypt.com:', k.split('>')[1].strip('<')
                        else:
                            return False # 'md5decrypt.com: not found'
            except ImportError:
                return False#'md5decrypt: ERROR'

class SHA1():
    def __init__(self, checksum):
        self.checksum = checksum

class SHA256():
    def __init__(self, checksum):
        self.checksum = checksum

class SHA512():
    def __init__(self, checksum):
        self.checksum = checksum

class RipeMD160():
    def __init__(self, checksum):
        self.checksum = checksum

class CRC32():
    def __init__(self, checksum):
        self.checksum = checksum

supported_functions = {
    'MD5': MD5
}

def verify_checksum(original, checksum, function):
    try:
        if function(original) == checksum:
            return True
        else:
            return False
    except NameError:
        return None

if __name__ == '__main__':
    print MD5('76a2173be6393254e72ffa4d6df1030a').decrypt()