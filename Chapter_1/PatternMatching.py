def PatternMatching(pattern, seq):
    '''
    Finds all occurences of a pattern in a sequence using a sliding window of size k and returns
    a list with the location of all occurences of that pattern, using 0-based indexing.

    Parameters:
    pattern (str): The pattern which is being searched for in the sequence
    seq (str): The sequence in which the pattern will be searched for

    Returns:
    locList ((int) list): List of starting positions where the pattern is found in the sequence
    '''
    locList = []
    for idx in range(len(seq) + 1 - len(pattern)):
        if seq[idx : idx + len(pattern)] == pattern:
            locList.append(str(idx))
    return locList

def fileReader(file):
    #parses text file from Rosalind to obtain pattern and sequence and trims output for submission
    lines = [line.rstrip() for line in open(file)]
    pattern = lines[0]
    seq = "".join(lines[1:])
    print(" ".join(PatternMatching(pattern, seq)))

