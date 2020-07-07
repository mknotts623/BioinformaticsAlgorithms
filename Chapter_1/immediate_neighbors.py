def immediate_neighbors(pattern):
    '''
    Given a pattern, returns all single point mutations by changing each index at a time with all
    possible nucleotides. Runs in O(n) time. Implemented as described in pseudocode in text.

    Parameters:
    pattern(text): Pattern for which the neighbors are being generated from.

    Returns:
    neighborhood (str(set)): All neighbors of pattern
    '''
    other_nucs = {'A': ['T', 'C', 'G'], 'T': ['A', 'C', 'G'], 'C': ['A', 'T', 'G'], 'G': ['A', 'T', 'C']}
    neighborhood = set([pattern])
    for i in range(len(pattern)):
        curr = pattern[i]
        for nuc in other_nucs[curr]:
            neighbor = pattern[0:i] + nuc + pattern[i+1:]
            neighborhood.add(neighbor)
    return neighborhood
