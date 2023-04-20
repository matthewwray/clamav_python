from format_sigs import get_processed_sig
from simple_match import simple_match
from chain_matching import initiate_match

# TODO: Current error in the code # THIS IS NOW FIXED
# Separators, eg {1-3}, means 1-3 bytes between the subsignature before and after the sep. 
# Ie, match any 1-3 bytes.
# However, currently the code checks for 1-3 bytes between the START of subsig1 and the START of subsig2.
# It should instead be the END of subsig1 and the START of subsig2.
# Potential solution: Add a new 'column' to allresults array that contains the length of the subsig
# Then, when calling location_sep_check, add the length of the array to loc1

# TODO: Return not True/False for matching, but the index of where it was matched. Will be useful for logical signatures & offsets. # FIXED

#sig = "22{2}232c2d252{1-3}2296e6573*61706528"from bodymatch import bodymatch

def bodymatch(sig, file):
    # bodymatch refers to ClamAV's bodymatching format, shared across both logical expressions and extended expressions
    # More info: https://docs.clamav.net/manual/Signatures/BodySignatureFormat.html

    sig = get_processed_sig(sig)
    #  Determine if the signature is simple or complex
    if len(sig) > 1:
        is_simple = False
    else:
        is_simple = True
        sig = sig[0]

    #SIMPLE MATCHING
    # We can just match the signature as is using simple_match
    if is_simple:
        result = simple_match(sig, file)
        return result

    #COMPLEX MATCHING
    # We have to match each individual subsig and then check if they match each other
    else:
        #Firstly, we create an 'allresults' list, which contains the results of simple_match
        # for each subsig, alongside its separator, and length of subsig
        allresults = []
        for subsig in sig:
            length = int(len(subsig[0])/2)
            if len(subsig) == 1:
                allresults.append([simple_match(subsig[0], file), length])
            else:
                allresults.append([simple_match(subsig[0], file), subsig[1], length])

        return initiate_match(allresults) #Initiates a chain match to check if there is a match among the subsigs