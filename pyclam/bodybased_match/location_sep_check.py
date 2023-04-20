def location_sep_check(loc1, loc2, sep):
    #Check if there is a match between any individual two indexes (in accordance with the separator)

    loc_value = loc2 - loc1 # Shorthand to make calculations easier

    if loc_value <= 0:
        return False

    if sep == "*": #Wilcard separator.
        return True
    
    elif "-" not in sep:
        if loc1 + int(sep) == loc2: #If sep is not a range, ie is a single int.
            return True 
    
    elif sep[0] == "-": #If loc_value is equal or less than...
        sep_value = int(sep[1:])
        if loc_value <= sep_value:
            return True
    
    elif sep[-1] == "-": #If loc_value is equal or greater than...
        sep_value = int(sep[:-1])
        if loc_value >= sep_value:
            return True
    
    else: #If within range. Format: n-m
        sep_value = sep.split('-')
        sep_value[0], sep_value[1] = int(sep_value[0]), int(sep_value[1])
        if ((loc_value >= sep_value[0]) and (loc_value <= sep_value[1])):
            return True

    return False
