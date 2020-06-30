from FrequencyTable import FrequencyTable
import numpy as np
def BetterFrequentWords(text, k):
    '''
    Improvement on FrequentWords, as this runs in O(n) time vs. FrequentWords' O(n^2) time. Achieves
    by using FrequencyMap and returning array with all k-mers with frequency == max.

    Parameters:
        text (str): The text for which the most frequent k-mers is being searched for.
        k (int): The size of the k-mers being searched for

    Returns:
        freqPatterns (numpy ndarray): all k-mers with frequency == max
    '''
    freqMap = FrequencyTable(text, k)
    freqPatterns = np.full(len(freqMap), "", dtype = object)
    numPatterns = 0
    #Could be implemented better with custom map that stores max value as field for O(1) access
    maxFreq = freqMap[max(freqMap, key = freqMap.get)]
    for pattern in freqMap:
        if freqMap[pattern] == maxFreq:
            freqPatterns[numPatterns] += pattern
            numPatterns += 1
    return freqPatterns[0:numPatterns]

def readFile(file):
    #parses text file from Rosalind to separate text from pattern and trims output for submission

    lines = [line.rstrip() for line in open(file)]
    k = lines.pop()
    text = ''.join(lines)
    print(' '.join(BetterFrequentWords(text, int(k))))
