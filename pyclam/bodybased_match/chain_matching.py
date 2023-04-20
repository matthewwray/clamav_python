from location_sep_check import location_sep_check

def initiate_match(allresults):
    #Initiates a chain match

    result = [] #An array containing all of the locations 
    # in which a match was made. Ie, all of the locations
    # the subsignature was matched at.

    # We iterate through all of the 0th subsig matches, and then chain match from these
    for indiv in allresults[0][0]:
        sep = allresults[0][1]
        length = allresults[0][2]
        if chain_matching(indiv, sep, allresults, length):
            result.append(indiv)
    return result

def chain_matching(indiv, sep, allresults, length, n=1):
    # Recursive algorithm that checks if there is any match between the indexes

    for x in allresults[n][0]:
        # Check if there is a match between any individual two indexes (in accordance with the separator)
        if location_sep_check(indiv+length, x, sep):
            
            if n+1 >= len(allresults):
                return True
        
            length = allresults[n][2]

            # Make the recursive call
            if chain_matching(x,allresults[n][1], allresults, length, n+1):
                return True
