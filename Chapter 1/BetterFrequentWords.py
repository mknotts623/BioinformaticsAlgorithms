from FrequencyTable import FrequencyTable
import numpy as np
def BetterFrequentWords(text, k):
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
    lines = [line.rstrip() for line in open(file)]
    k = lines.pop()
    text = ''.join(lines)
    print(' '.join(BetterFrequentWords(text, int(k))))

readFile('BetterFrequentWords.txt')


