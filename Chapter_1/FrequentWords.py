from PatternCount import PatternCount
import numpy as np

def FrequentWords(text, k):
    """
    Finds the most common k-mers in a given text. Does by sliding window of size k through text,
    counting how many times that k-mer appears in the text, keeps track of the max occurences,
    returning a set that has all k-mers with frequency equal to the maximum of all k-mers in
    the text, all described by Section 1.2 of the text. This is not a particularly efficient
    algorithm, with O(n^2) efficiency, where n = len(text), but it will be improved on with
    FrequencyTable.

    Parameters:
        text (str): The text for which the most frequent k-mers is being searched for.
        k (int): The size of the k-mers being searched for

    Returns:
        FrequentPatterns (set(str)): set of most frequent k-mers in text
    """
    FrequentPatterns = set()
    count = np.zeros(len(text) + 1 - (k))
    max = 0
    for i in range(len(text) + 1 - k):
        pattern = text[i: i + k]
        currcount = PatternCount(text, pattern)
        if currcount > max:
            max = currcount
        count[i] = currcount
    for i in range(len(text) + 1 - k):
        if count[i] == max:
            FrequentPatterns.add(text[i: i + k])
    return FrequentPatterns
