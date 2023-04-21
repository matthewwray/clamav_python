from extendedmatch import extended_match
from os import system as run
from os import remove
from time import sleep

# To test if our project works properly, we perform a series of scans on files and sigs
# We then check if the official clamav build gives the same outputs with the same inputs
# If it does, then the test has passed
# Otherwise a failure has occured

# THIS ASSUMES CLAMAV IS ALREADY INSTALLED

def get_clamav_result(sig, file):
    with open('database.ndb', 'w') as f:
        f.write(sig)
    
    with open('testingfile.txt', 'w') as f:
        f.write(file)
    
    run("clamscan testingfile.txt --quiet -d database.ndb -l scan_output.txt")
    sleep(3)
    res = read_result()
    sleep(1)
    clean_test_files()
    sleep(1)

    return res
    
def clean_test_files():
    files = ['database.ndb', 'testingfile.txt', 'scan_output.txt']
    for f in files:
        try:
            remove(f)
        except:
            pass

def read_result(): #Return True if infected, False otherwise
    with open('scan_output.txt', 'r') as f:
        scan_result = f.read()
        if scan_result.find('Infected files: 0') == -1: #If cannot find 'Infected files: 0', then there is infection, so return True
            return True
        return False

files = [
    "aabbbbccdd",
    "ba1ba1ba1ba1ba1ba1ba1ba1ba12ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1ba1",
    "3aaa3aa3aaa3b",
    "XXXXWWWWWWX",
    "XWWWXW"
]

sigs = [
    "signature0:0:*:62626262",
    "signature1:0:*:3132626131626131626131626131626131626131626131626131626131626131626131",
    "signature2:0:*:3361616133{2-4}336161613362",
    "signature3:0:*:585858{6}58",
    "signature4:0:*:5858{4}5858"
]

overall_result = True

for i in range(0, len(sigs)):
    cap_res = ( extended_match(sigs[i], files[i])[0] )
    clamav_res = ( get_clamav_result(sigs[i], files[i]))
    if cap_res == clamav_res:
        print("Both matching " + str(cap_res) + " for sig: " + str(i))
    else:
        print("Not bothing match for sig: " + str(i))
        overall_result = False

if overall_result:
    print("\tTEST PASSED\nThe results of each scan were identical")
else:
    print("\tTEST FAILED\nThe results of each scan were NOT identical")