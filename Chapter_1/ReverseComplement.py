def ReverseComplement(seq):
    '''
    Returns the reverse complement of a given DNA sequence

    Parameters:
    seq (str): DNA sequence which the reverse complement is to be taken of

    Returns:
    revComp (str): Reverse Complement of the input sequence
    '''
    compDict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    revComp = ''
    for i in range(len(seq)):
        if seq[i] == '<':
            print(i)
        revComp += compDict[seq[i]]
    return "".join(revComp[::-1])

def readFile(file):
    #parses text file from Rosalind to obtain input sequence
    lines = [line.rstrip() for line in open(file)]
    seq = "".join(lines)

    print(ReverseComplement(seq))
