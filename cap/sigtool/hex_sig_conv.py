HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def hexdump(string):
    result = []
    for character in string:
        hex_val = ord(character)
        result.append(HEX[(hex_val >> 4) & 0x0f])
        result.append(HEX[hex_val & 0x0f])
    return ''.join(result)

def decodehex(hex):
    result = []
    for i in range(len(hex)):
        if i % 2 == 1:
            continue

        if (hex[i] == '?') and (hex[1+1] == '?'):
            result.append("\\{WILDCARD_IGNORE}")
        else:
            result.append(chr(int(str(hex[i] + hex[i+1]), 16)))
    return ''.join(result)
    