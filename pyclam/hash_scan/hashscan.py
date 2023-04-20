from gethash import gethash
from load_clamav_data import getdb
from get_filesize import get_filesize

file_to_scan = "gethash.py"
database_file = "main.hsb"

hashes = gethash(file_to_scan)
db = getdb(database_file)
filesize = get_filesize(file_to_scan)

detected = False

for i in db:
    if len(i) != 3: # Prevents invalid lines from causing errors
        continue

    filesize_match = False
    if i[1] == "*":
        filesize_match = True
    elif i[1] == str(filesize):
        filesize_match = True

    if (i[0] in hashes) and (filesize_match == True):
        detected = True
        virname = i[2]
        break

if detected:
    print("\tDETECTED")
    print("File matches entry in database.")
    print("Malware name:", virname)
else:
    print("No malware detected.")