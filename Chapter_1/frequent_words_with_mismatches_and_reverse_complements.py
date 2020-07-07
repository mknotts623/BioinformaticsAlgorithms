from frequent_words_with_mismatches import frequent_words_with_mismatches
from approximate_pattern_count import approximate_pattern_count
from ReverseComplement import ReverseComplement
from neighbors import neighbors

def frequent_words_with_mismatches_and_reverse_complements(text, k, d):
    '''
    Finds the most frequent k-mers within the text with at most d mismatches and with reverse
    compelements. Does so by sliding a k-sized window down the text to find a pattern, generates
    the likely d-neighborhood for that pattern, and stores the frequency of those neighbors in a
    map. It then repeats this process for the reverse complements of the pattern.Then, the patterns
    with the max frequency are returned. Runs in O(n * k^2) time, where n is the length of the text
    and k is the length of the pattern.

    Parameters:
    text (str): Sequence in which k-mers are being searched for
    k (int): size of k-mer
    d (int): maximum Hamming Distance between k-mer and neighbors

    Returns:
    patterns (str(list)): all k-mers with frequence == max
    '''
    patterns = []
    frequency_map = {}
    for i in range(len(text) + 1 - k):
        pattern = text[i: i + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor in frequency_map:
                frequency_map[neighbor] += 1
            else:
                frequency_map[neighbor] = 1

        rev_pattern = ReverseComplement(pattern)
        rev_neighborhood = neighbors(rev_pattern, d)
        for rev_neighbor in rev_neighborhood:
            if rev_neighbor in frequency_map:
                frequency_map[rev_neighbor] += 1
            else:
                frequency_map[rev_neighbor] = 1

    max_val = frequency_map[max(frequency_map, key = frequency_map.get)]
    for pattern in frequency_map:
        if frequency_map[pattern] == max_val:
            patterns.append(pattern)
    return patterns

def read_file(file):
    #parses text file from Rosalind to obtain sequence, k-mer size, and max Hamming Distance and
    #trims output for submission
    lines = [line.rstrip() for line in open(file)]
    nums = lines.pop().split(" ")
    k, d = int(nums[0]), int(nums[1])
    seq = lines[0]
    print(" ".join(frequent_words_with_mismatches_and_reverse_complements(seq, k, d)))
