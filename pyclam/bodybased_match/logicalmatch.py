import os
from time import sleep
from bodymatch import bodymatch

#sig = """Sig4;Engine:51-255,Target:1;((0|1)&(2|3))&4;*:61;78:22??232c2d252229{-15}6e657361706528;68efa311c3b9963cb1ee8e586d32aeb9043e;f9c58dcf43987e4f519d629b103375::iwf;550:6300680065005c0046006900"""


def logical_match(sig, file):
    # Main function to match a signature and a file

    #First split the signature into its constituent parts
    sig_split = sig.split(';')
    virname = sig_split[0]
    tdb = sig_split[1]
    logexp = sig_split[2]
    subsigs = sig_split[3:]

    # Convert & match subsigs
    subsigs = convert_all_subsigs(subsigs)
    subsigs = match_all_subsigs(subsigs, file)

    # Split logexp into number, structural and comparator parts
    logexp = split_logexp(logexp)

    simple_logexp = is_logexp_simple(logexp)

    if simple_logexp:
        # Convert & execute logexp
        logexp = convert_simple_le(logexp, subsigs)
        executable_logexp = ''.join(logexp)
        result = execute_logexp(executable_logexp)
    
    else:
        print("Logical expressions containing comparators ('>' '<' '=' ',') are not supported.")
        exit()
    
    return result, virname

def execute_logexp(logexp):
    if eval(logexp):
        return True
    return False

def convert_all_subsigs(subsigs): #Converts an array of 'raw' subsigs, 
    #by replacing each subsig string with an array containing:
    #the offset, the subsig body, and the sigmod
    for i in range(len(subsigs)):
        subsigs[i] = subsigs[i].replace('::', '<DOUBLECOLON_CHAR>')
        if ':' not in subsigs[i]:
            subsigs[i] = ":" + subsigs[i]
        subsigs[i] = subsigs[i].replace('<DOUBLECOLON_CHAR>', '::')
        if '::' not in subsigs[i]:
            subsigs[i] = subsigs[i] + "::"

        tmp0 = subsigs[i].split('::')
        tmp1 = tmp0[0].split(':')
        subsigs[i] = [tmp1[0], tmp1[1], tmp0[1]]
    return subsigs

def match_all_subsigs(subsigs, file): #Matches each
    #subsig and appends the result to that subsig array
    for x in range(len(subsigs)):
        
        i = subsigs[x]

        scan_res = bodymatch(i[1], file)
        offset = i[0]

        check_offset(offset)

        if offset == "*" or offset == '': #If wildcard offset
            scan_match = len(scan_res)
        elif int(offset) in scan_res: #If offset match scan results
            scan_match = 1
        else: #If the offset does not match the results
            scan_match = 0

        subsigs[x].append(scan_match)
    return subsigs

def is_logexp_simple(le_array):
    # Simple means does not contain comparator
    comparator_chars = ['=', '<', '>', ',']
    for le_value in le_array:
        for char in le_value:
            if char in comparator_chars:
                return False
    return True

def split_logexp(logexp):
    # Split logexp into number, structure and comparator parts.
    # We do this by keeping track of the type of the current sequence of characters.
    # If there is a change in type, add the sequence to the array and start a new sequence

    le_array = []
    done = False
    i=0
    current_string = ""

    # Define the different types of characters
    number_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    comparator_chars = ['=', '<', '>', ',']
    structure_chars = ['(', ')', '|', '&']
    last_type = ""

    for char in logexp:
        if (char in number_chars) and (last_type == "COMPARATOR"):
            current_string += char
            last_type = "COMPARATOR"

        elif char in number_chars:
            if last_type == "NUMBER" or last_type == "":
                current_string += char
            else:
                le_array.append(current_string)
                current_string = char
            last_type = "NUMBER"

        elif char in structure_chars:
            if last_type == "STRUCTURE" or last_type == "":
                current_string += char
            else:
                le_array.append(current_string)
                current_string = char
            last_type = "STRUCTURE"

        elif char in comparator_chars:
            if last_type == "COMPARATOR" or last_type == "":
                current_string += char
            else:
                le_array.append(current_string)
                current_string = char
            last_type = "COMPARATOR"
            
    le_array.append(current_string)

    return le_array

def convert_simple_le(logexp, subsigs):
    # Replace number characters with the subsignature that they reference
    # Also replace structural characters with their Python equivalent where appropriate
    # The purpose is to make the logexp evaluatable
    new_le = []
    for le_value in logexp:
        if is_number(le_value):
            index = int(le_value)
            new_le.append(str(subsigs[index][3]))
        else:
            le_value = le_value.replace("&", " and ")
            le_value = le_value.replace("|", " or ")
            new_le.append(le_value)
    return new_le


def check_offset(offset):
    valid_chars = ['*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    offset = str(offset)
    for char in offset:
        if char not in valid_chars:
            print("Offset type not currently supported: offsets must be either wildcard ('*') or an integer value.")
            exit()

def is_number(string):
    number_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in string:
        if char not in number_chars:
            return False
    return True


# sig = "VirusThing;Engine:51-255;(0&2)|1;6161;2:6262;63"
# file = "aabcab"
# x = logical_match(sig, file)
# print(x)