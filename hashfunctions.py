#coding: utf-8
from bs4 import NavigableString
from bs4 import BeautifulSoup
import requests
import hashlib
import re

class MD5():
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        def check(self):
            return re.match(r"[A-Fa-f\d]{32}", self.checksum)

        def __init__(self, checksum):
            self.checksum = checksum

            self.claveycontrasena_url = 'http://descodificar.claveycontraseña.es/'+self.checksum+'.html'
            self.md5decoder_url       = 'http://md5decoder.org/'+self.checksum
            self.gromweb_url          = 'https://md5.gromweb.com/?md5='+self.checksum
            self.md5decrypt_url       = 'https://md5decrypt.net/en/'


        def decrypt(self, search_many=False):
            sites_to_get_from = [
                self.get_from_claveylacontrasena,
                self.get_from_md5decrypt,
                self.get_from_md5decoder,
                self.get_from_gromweb
            ]

            results = {}

            for site in sites_to_get_from:
                decryption_result = site()

                if decryption_result:
                    results[decryption_result[0]] = decryption_result[1]

                    if search_many:
                        continue
                    else:
                        break

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
                md5decrypt_session = requests.Session()
                md5decrypt_session.headers.update(self.headers)

                md5decrypt_get = md5decrypt_session.get(self.md5decrypt_url).text

                rootSoup = BeautifulSoup(md5decrypt_get, 'lxml')

                formData = {
                    "decrypt": "Decrypt",
                    "hash": self.checksum
                }

                for child in rootSoup.find('form').children:
                    if isinstance(child, NavigableString): continue
                    dont_names = ['crypt', 'decrypt', 'hash']
                    name = child.get('name')

                    if name:
                        if name in dont_names: continue
                        
                        value = child.get("value")
                        if value:
                            formData[name] = value

                md5decrypt_post = md5decrypt_session.post(self.md5decrypt_url, data=formData).text

                original = md5decrypt_post.split(self.checksum + " : <b>")[1].split('</b>')[0]

                return 'md5decrypt', original

            except:
                return False

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
    if function not in hashlib.algorithms_available:
        return False

    try:
        hashed_original = hashlib.new(function)
        hashed_original.update(original)
        
        if hashed_original.hexdigest() == checksum:
            return True
        else:
            return False
    except NameError:
        return None

if __name__ == '__main__':
    print MD5('76a2173be6393254e72ffa4d6df1030a').decrypt()