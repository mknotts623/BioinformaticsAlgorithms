from neighbors import neighbors
def frequent_words_with_mismatches(text, k, d):
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
    max_val = frequency_map[max(frequency_map, key = frequency_map.get)]
    for pattern in frequency_map:
        if frequency_map[pattern] == max_val:
            patterns.append(pattern)
    return patterns

def read_file(file):
    lines = [line.rstrip() for line in open(file)]
    nums = lines.pop().split(" ")
    k, d = int(nums[0]), int(nums[1])
    seq = lines[0]
    print(" ".join(frequent_words_with_mismatches(seq, k, d)))

read_file("frequent_words_with_mismatches.txt")

