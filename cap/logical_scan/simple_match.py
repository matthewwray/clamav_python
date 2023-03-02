from hex_sig_conv import decodehex

def simple_match(sig, file):
    if len(sig) % 2 == 1:
        print("ERROR IN simple_match: sig has odd number of characters")
        exit()
        
    result = []
    lt=len(file)
    lw=int(len(sig)/2)
    for i in range(lt-lw+1):
        j=0
        while(j<lw):
            if individual_char_match((sig[2*j]+sig[2*j+1]), file[i+j]):
                j+=1
            else:
                break
        else:
            result.append(i)
    return result

        
def individual_char_match(ch_sig, ch_file):
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
        
sig = '7375646f2072'

#with open('freegames.txt', 'r') as f:
#    file = f.read()

sig = '486f7720646f2049206c6f6f6b20696e206865783f'
file = 'How do I look in hex?'

print(simple_match(sig, file))
