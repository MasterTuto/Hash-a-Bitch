# -*- coding: utf-8 -*-
import requests
import platform
from os import system

try:
    import google
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

print """$$\   $$\                     $$\                             $$\       $$\   $$\     v1.0      $$\\
$$ |  $$ |                    $$ |                            $$ |      \__|  $$ |              $$ |
$$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\         $$$$$$\        $$$$$$$\  $$\ $$$$$$\    $$$$$$$\ $$$$$$$\\
$$$$$$$$ | \____$$\ $$  _____|$$  __$$\        \____$$\       $$  __$$\ $$ |\_$$  _|  $$  _____|$$  __$$\\
$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |       $$$$$$$ |      $$ |  $$ |$$ |  $$ |    $$ /      $$ |  $$ |
$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |      $$  __$$ |      $$ |  $$ |$$ |  $$ |$$\ $$ |      $$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |      \$$$$$$$ |      $$$$$$$  |$$ |  \$$$$  |\$$$$$$$\ $$ |  $$ |
\__|  \__| \_______|\_______/ \__|  \__|       \_______|      \_______/ \__|   \____/  \_______|\__|  \__|
                                                                             coded by Super23 (aka Lord13)
"""
md5hash = raw_input("MD5 Hash>>")
while len(md5hash) != 32:
    md5hash = raw_input("MD5 Hash>>")
print("")

headers = {
    'User-Agent': 'Mozilla/5.0'
}

claveycontrasena = requests.get('http://descodificar.claveycontraseña.es/'+md5hash+'.html', headers=headers).text
md5decoder = requests.get('http://md5decoder.org/'+md5hash, headers=headers).text
gromweb = requests.get('http://md5.gromweb.com/?md5='+md5hash, headers=headers).text

try:
    if 'showkey' in claveycontrasena:
        i = 1
        k = 'a'
        while k[-1] != ')':
            k = claveycontrasena[claveycontrasena.index('showkey'):claveycontrasena.index('showkey')+len('showkey')+i]
            i += 1
        print 'claveycontrasena.es:', k.split('\'')[1]
    else:
        print "claveycontrasena.es: not found"
except:
    print "claveycontrasena.es: ERROR WHILE CONNECTING"

try:
    if 'md2' in md5decoder:
        i = 1
        k = 'a'
        while k[-1] != ')':
            k = md5decoder[md5decoder.index('md2'):md5decoder.index('md2')+len('md2')+i]
            i += 1
        print 'md5decoder.org:', k
    else:
        print 'md5decoder.org: not found'
except:
    print "ERROR WHILE CONNECTING"

try:
    if 'content string"' in gromweb:
        i = 1
        k = 'a'
        while k[-1] != '<':
            k = gromweb[gromweb.index('content string"'):gromweb.index('content string"')+len('content string"')+i]
            i += 1
        print 'gromweb.com:', k.split('>')[1].strip('<')
    else:
        print 'gromweb.com: not found'
except:
    print "ERROR WHILE CONNECTING"

try:
    for url in google.search(md5hash, stop=5):
        if 'md5decrypt.org' in url:
            md5decrypt = requests.get(url, headers=headers).text
            if 'style=\'color:red;\'>' in md5decrypt:
                i = 1
                k = 'a'
                while k[-1] != '<':
                    k = md5decrypt[md5decrypt.index('style=\'color:red;\'>'):md5decrypt.index('style=\'color:red;\'>')
                                   + len('style=\'color:red;\'>') + i]
                    i += 1
                print 'md5decrypt.com:', k.split('>')[1].strip('<')
            else:
                print 'md5decrypt.com: not found'
except ImportError:
    print 'md5decrypt: ERROR'
input('Press any button to continue...')
