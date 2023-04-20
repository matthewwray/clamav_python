import hashlib

def get_hashes(string):
    md5_val    = get_md5(string)
    sha1_val   = get_sha1(string)
    sha256_val = get_sha256(string)
    return [md5_val, sha1_val, sha256_val]

def get_md5(string):
    md5_val    = hashlib.md5(string.encode('utf-8')).hexdigest()
    return md5_val

def get_sha1(string):
    sha1_val   = hashlib.sha1(string.encode('utf-8')).hexdigest()
    return sha1_val

def get_sha256(string):
    sha256_val = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return sha256_val