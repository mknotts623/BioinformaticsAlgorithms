def min_skew(seq):
    '''
    Computes where the minimum values of G - C occur in a sequence to predict the ori of a plasmid.
    Based on spontaneous deamination of C to T while DNA is single-stranded, which is spends a long
    time being when it is the lagging (or forward, as described in text) strand during replication.
    Thus, G - C is decreasing along the leading strand and increasing along the lagging strand,
    reaching a minimum at the origin of the replication fork. Computes the skew and returns the
    minimum location(s) in O(n) time.

    Parameters:
    seq (str): DNA sequence from which the skew is being calculated from

    Returns:
    min_positions(int(list)): Positions where the skew reaches a minimum, with 1-based indexing
    '''
    skew_vals = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    min_positions = []
    total_val = skew_vals[seq[0]]
    min_val = total_val
    min_positions.append(0)
    for i in range(1, len(seq)):
        curr = seq[i]
        total_val += skew_vals[curr]
        if total_val < min_val:
            min_positions = [i + 1]
            min_val = total_val
        elif total_val == min_val:
            min_positions.append(i + 1)
    return min_positions


def read_file(file):
    #parses text file from Rosalind to obtain sequence and trims output for submission

    lines = [line.rstrip() for line in open(file)]
    min_pos = min_skew("".join(lines))
    print(" ".join(str(x) for x in min_pos))
