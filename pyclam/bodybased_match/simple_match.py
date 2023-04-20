from hex_sig_conv import decodehex

def simple_match(sig, file):
    # Matches a sig in a file using a string searching algorithm

    if len(sig) % 2 == 1:
        print("ERROR IN simple_match: sig has odd number of characters")
        exit()

    # Aforementioned string searching algorithm    
    result = []
    lt=len(file)
    lw=int(len(sig)/2)
    for i in range(lt-lw+1):
        j=0
        while(j<lw):
            # Of course, unlike a normal string search alg, we can't just use ==
            # We must use a char_match
            if individual_char_match((sig[2*j]+sig[2*j+1]), file[i+j]):
                j+=1
            else:
                break
        else:
            result.append(i)
    return result

        
def individual_char_match(ch_sig, ch_file):
    # Match two hex chars with one char in the file
    if ch_sig == '??':
        return True
    elif ch_sig[0] == '?': #Match a low nibble (the four low bits)
        ch_sig = str("0"+ch_sig[1])
        if (ord(decodehex(ch_sig)) & 0x0f) == (ord(ch_file) & 0x0f):
            return True
    elif ch_sig[1] == '?': #Match a high nibble (the four high bits)
        ch_sig = str(ch_sig[0]+"0")
        if (ord(decodehex(ch_sig)) & 0xf0) == (ord(ch_file) & 0xf0):
            return True
    elif decodehex(ch_sig) == ch_file:
        return True  
    return False