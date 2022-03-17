def readFile(name):
    with open(name, 'r') as f:
        index = 0
        matrix = []
        for line in f:
            row = []
            if not line.startswith(';'):  # this is a comment, just skip it
                for char in line.split(' '):
                    if not char == '-\n':
                        row.append(int(char))
                matrix.insert(index, row)
                index += 1
    return matrix
