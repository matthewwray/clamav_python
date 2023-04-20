from sig_preprocessing import preprocess

def get_processed_sig(sig): #Will return either a 
                            #simple sig or a complex sig

    ## PREPROCESS TO REPLACE {n} with ??*n . ALSO REPLACE * WITH {*}
    sig = preprocess(sig)
    sig = replace_asterisk(sig)

    ## IF THERE ARE SEPARATORS, WE SPLIT THE SIG INTO MULTIPLE SUBSIGS
    if '}' in sig:
        sig = process_complex_sig(sig)
    
    else:
        sig = [sig]

    return sig
    ##ELSE, WE HAVE A SIMPLE SIG

def process_complex_sig(sig): 
    #Takes an unprocessed complex sig and turns 
    # it into the valid complex sig format
    array_of_subsigs = []
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
