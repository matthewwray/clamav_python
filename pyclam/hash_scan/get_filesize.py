import os

def get_filesize(filename):
    filesize = os.path.getsize(filename)
    return filesize