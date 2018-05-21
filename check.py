#! /usr/bin/env python

import crypt
import subprocess

for line in subprocess.check_output(["sudo", "cat", "/etc/shadow"]).split('\n'):
    if line != '':
        # print(line)
        items = line.split(':')
        account = items[0]
        password = items[1]
        if password not in ['!!', '*']:
            passitems = password.split('$')
            crypt_type = passitems[1]
            salt = passitems[2]
            hash_ = passitems[3]
            hash__ = crypt.crypt(account, "${0}${1}".format(crypt_type, salt)).split('$')[3]
            # print("{0} {1} {2} {3} {4} {5}".format(account, password, crypt_type, salt, hash_, hash__))
            if hash_ == hash__:
                print("{0}: Identical with user name".format(account))
