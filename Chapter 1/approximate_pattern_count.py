from hamming_distance import hamming_distance
def approximate_pattern_count(text, pattern, d):
    '''
    Finds the number of times a pattern appears in a text with at most d mismatches. Uses sliding
    window method. Runs in O(n*k) time, where n is the length of the text and k is the length of
    the pattern.

    Parameters:
    text (str): Text in which the pattern is being searched for
    pattern (str): Pattern that is being searched for in the text
    d (int): Max number of mismatches between text and patter.

    Returns:
    count (int): Number of times pattern appears in text with <= d mismatches
    '''
    count = 0
    for i in range(len(text) - len(pattern)):
        approx = text[i: i + len(pattern)]
        if hamming_distance(pattern, approx) <= d:
            count += 1
    return count
