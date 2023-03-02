def read_chars(): #Read the characters from chars.csv as an array
    db = []
    with open('chars.csv', 'r') as f:
        for line in f:
            
            if len(line) < 2: #Ensure blank lines don't cause errors
                continue
            
            current_value = line.split(',')
            current_value = current_value[0:-1] #Gets rid of the return character at the end
            
            if current_value[-1] == 'COMMA':
                current_value[-1] = ','
            
            elif current_value[-1] == 'NEWLINE':
                current_value[-1] = '\n'
            
            db.append(current_value)
    return db


def hexdump(string): #Takes a string as an input, returns its representation in hex
    result = []
    db = read_chars()
    for character in string:
        for i in db:
            if i[1] == character:
                result.append(i[0])
                break
    return ''.join(result)

def decodehex(hex): #Takes a string of hex values as an input, returns its corresponding text. Each hex value must take up 2 characters, eg '0a'. So an example string is '68656c6c68'
    db = read_chars()
    result = []
    hex_list = []

    if len(hex) % 2 == 1:
        return -1

    for i in range(len(hex)):
        if i % 2 == 0:
            hex_value = str(hex[i] + hex[i+1])
            hex_list.append(hex_value)
    
    for hex_value in hex_list:
        for i in db:
            if i[0] == hex_value:
                result.append(i[1])
                continue
    
    return ''.join(result)