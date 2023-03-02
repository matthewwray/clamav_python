def getdb(filename):

    with open(filename, 'rb') as f:
        lines = f.readlines()

    db = []

    for i in lines:
        i = str(i)
        i = i[2:-3] # Otherwise return characters are in the output

        i = i.split(':')
        db.append(i)
    
    return db