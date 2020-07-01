from FrequencyTable import FrequencyTable
def find_clumps(text, k, l, t):
    '''
    Finds all k-mers that appear in text at least t times in a sequence by examining a clump of size l.
    Moves the l sized clump along the text to find all k-mers in all possible l sized clumps that
    appear at least k times.

    Parameters:
    text (str):

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
    lines = [line.rstrip() for line in open(file)]
    seq = lines[0].rstrip()
    nums = list(map(int, lines[1].split()))
    print(" ".join(find_clumps(seq, nums[0], nums[1], nums[2])))
