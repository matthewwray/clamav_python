from sig_preprocessing import preprocess
subsig = "78:22{2}232c2d2522296e6573*61706528::ai"
subsig = "87:606071717220:wiaf"


def get_processed_sig(sig): #Will return either a simple sig or a complex sig

    ## FIRSTLY, GET SIGMOD AND OFFSET
    if '::' in sig:
        sigmod = sig.split('::')[1]
        subsig = sig.split('::')[0]
    else:
        sigmod = ''

    if ':' in sig:
        offset = sig.split(':')[0]
        sig = sig.split(':')[1]
    else:
        offset = '*'

    ## PREPROCESS TO REPLACE {n} with ??*n . ALSO REPLACE * WITH {*}
    sig = preprocess(sig)
    sig = replace_asterisk(sig)

    ## IF THERE ARE SEPARATORS, WE SPLIT THE SIG INTO MULTIPLE SUBSIGS
    if '}' in sig:
        sig = process_complex_sig(sigmod, offset, sig)
    
    else:
        sig = [sigmod, offset, sig]

    return sig
    ##ELSE, WE HAVE A SIMPLE SIG
    print(sig)

def process_complex_sig(sigmod, offset, sig): #Takes an unprocessed complex sig and turns it into the valid complex sig format

    
    array_of_subsigs = []
    array_of_subsigs.append(sigmod)
    array_of_subsigs.append(offset)
    sig = sig.split('}')
    for i in sig:
        if '{' in i:
            i = i.split('{')
        else:
            i = [i]

        array_of_subsigs.append(i)
    return array_of_subsigs

def replace_asterisk(string):
    return string.replace('*', '{*}')
