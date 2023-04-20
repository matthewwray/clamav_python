from bodymatch import bodymatch

def extended_match(sig, file):

    #Split sig into constituent parts
    virname, features, offset, scansig = sig.split(':')

    # Call bodyscan on the subsig
    scan_res = bodymatch(scansig, file)
    
    # Find if the offset matches, ie if it is a wildcard or it matches one of the results
    offset_match = False
    if offset == '*':
        offset_match = True
    elif int(offset) in scan_res:
        offset_match = True

    # If both offset and the scan result are true...
    if ((len(scan_res) > 0) and (offset_match)):
        return (True, virname)
    return False, None