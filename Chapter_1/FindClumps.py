from FrequencyTable import FrequencyTable
def find_clumps(text, k, l, t):
    '''
    Finds all k-mers that are clumped in text at least t times in a sequence by examining a widow
    of size l. Moves the l sized window along the text to find all k-mers in all possible l sized
    clumps that appear at least k times. Algorithm is as described in text, with O(n^2) time.

    Parameters:
    text (str): Sequence which clumps of k-mers will be found
    k (int): Size of k-mer being searched for within the clump
    l (int): Size of clump within text which k-mers will be searched
    t (int): Minimum amount of occerences of k-mer within the clump

    Returns:
    patterns (int(set)): Set of all k-mers that appear at least t times in a clump
   '''
    patterns = set()
    for i in range(len(text) - l):
        window = text[i: i + l]
        freq_map = FrequencyTable(window, k)
        for key in freq_map:
            if freq_map[key] >= t:
                patterns.add(key)
    return patterns

def read_file(file):
    '''parses text file from Rosalind to obtain sequence, k-mer size, clump size, and minimum
    occurence and trims output for submission
    '''
    lines = [line.rstrip() for line in open(file)]
    seq = lines[0].rstrip()
    nums = list(map(int, lines[1].split()))
    print(" ".join(find_clumps(seq, nums[0], nums[1], nums[2])))
