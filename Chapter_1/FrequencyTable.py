def FrequencyTable(text, k):
    """
    Stores all k-mers in text as keys in a map, with values equal to their frequency, by sliding a
    window of size k through text. Allows for O(n) solving of all k-mers in a text that can
    searched by other algorithms in O(1) time.

    Parameters:
        text (str): text for which k-mers are being searched for.
        k (int): size of k-mers being searched for.

    Returns:
        freqMap (dict(str)): all possible k-mers in text mapped to their frequency values
    """
    freqMap = {}
    for i in range(len(text) + 1 - k ):
        pattern = text[i : i + k]
        if pattern in freqMap:
            freqMap[pattern] += 1
        else:
            freqMap[pattern] = 1
    return freqMap

