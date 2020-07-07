from hamming_distance import hamming_distance
def neighbors(pattern, d):
    '''
    Finds d-neighborhood, or set of strings with <= d mismatches, of a pattern. Does so by
    recursively building d-neighborhoods of the pattern's suffixes and substituting each
    nucleotide to build neighborhood for previous recursive call. Runs in O(n^2) time

    Pattern:
    pattern (str): Pattern from which d-neighborhood is being generated
    d (int): Maximum Hamming Distance from pattern and accepted neighbors

    Returns:
    neighbors (str(set)): Set of all d-neighbors of pattern
    '''
    nucs = ['A', 'T', 'C', 'G']
    if d == 0:
        return set([pattern])
    if len(pattern) == 1:
        return set(['A', 'T', 'C', 'G'])
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nuc in nucs:
                neighborhood.add(nuc + neighbor)
        else:
            neighborhood.add(pattern[:1] + neighbor)
    return neighborhood
