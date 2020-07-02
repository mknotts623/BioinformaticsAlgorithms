from min_skew import min_skew
from frequent_words_with_mismatches_and_reverse_complements import frequent_words_with_mismatches_and_reverse_complements

lines = [line.rstrip() for line in open('salmonella_enterica_genome.txt')]
seq = "".join(lines)
#select o
print(min_skew(seq))
possible_ori = min_skew(seq)[0]

window_size = 500

print(frequent_words_with_mismatches_and_reverse_complements(seq[possible_ori: possible_ori + window_size], 9, 2))
