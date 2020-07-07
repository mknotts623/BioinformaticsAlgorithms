import sys
sys.path.insert(1, "../Chapter_1")

from neighbors import neighbors
from hamming_distance import hamming_distance

def motif_enumeration(dna, k, d):
    '''
    Finds all k-mers that appear in multiple DNA sequences with no more than d mismatches. Does so
    by generating all k-mer neighbors for the first sequence, and checking if they occur in other
    sequences with a hamming distance <= d. Time complexity is very poor (O(n^2 * k^3 * s), where
    n = len(seq[0]), k = len(k-mer), and s = len(seq)

    Parameters:
    dna (str): dna sequences for which motifs are being found, separated by \n
    k (int): size of motif
    d (int): maximum Hamming Distance between sequence and pattern

    Returns:

    patterns (set): motifs found in all dna strands
    '''
    seqs = dna.split('\n')
    if seqs[-1] == '':
        seqs.pop()
    patterns = set()
    #O(n)
    for i in range(len(seqs[0])+1-k):
        pattern = seqs[0][i:i+k]
        #O(k^2)
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            all_match = True
            #O(s). Checks that k-mer with <= d mismatches appears in all seqs
            for seq in seqs:
                match = False
                #O(n^2)
                for l in range(len(seq)+1-k):
                    window = seq[l:l+k]
                    #O(k)
                    if hamming_distance(neighbor, window) <= d:
                        match = True
                if not match:
                    all_match = False
            if all_match:
                patterns.add(neighbor)
    return patterns


def read_file(file):
    #parses text file from Rosalind to obtain k, d, and DNA and trims output for submission
    lines = [line for line in open(file)]
    dna = "".join(lines[1:])
    nums = lines[0].split(" ")
    k, d = int(nums[0]), int(nums[1])
    print(" ".join(motif_enumeration(dna, k, d)))
