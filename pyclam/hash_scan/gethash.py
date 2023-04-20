#Modified from https://stackoverflow.com/a/22058673

import sys
import hashlib

def gethash(filename):
    BUF_SIZE = 65536 #Arbitrary buffer size

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)

    return (md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest())