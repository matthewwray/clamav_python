from simple_match import simple_match

def extended_sig_scan(sig, file):
    sig = sig.split(':')  #sig[0] = virname, sig[1] = type, sig[2] = offset, sig[3] = signature

    search_results = simple_match(sig[3], file) # Perform the scan itself. This function returns an array of indexes where the signature has been matched

    match = False

    if sig[2] == '*': #if wildcard offset
        if len(search_results) > 0:
            match = True
    else: #if fixed size offset, then we must see if the offset matches the signature.
        if int(sig[2]) in search_results: # If the offset equals a match of the signature, then a match has been made.
            match = True
    
    if match:
        print("\tDETECTED")
        print("Malware:", sig[0], "has been matched.")
        return True
    return False

with open('freegames.txt', 'r') as f:
    file = f.read()