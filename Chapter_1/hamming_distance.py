def hamming_distance(seq1, seq2):
    '''
    Calculates the number of mismatches between two sequences of equal length. Runs in O(n) time.

    Parameters:
    seq1, seq2 (str): The two sequences being compared

    Returns:
    dist (int): Number of mismatches between seq1 and seq2
    '''
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist

def read_file(file):
    #parses text file from Rosalind for both sequences
    seqs = [line.rstrip() for line in open(file)]
    print(hamming_distance(seqs[0], seqs[1]))
