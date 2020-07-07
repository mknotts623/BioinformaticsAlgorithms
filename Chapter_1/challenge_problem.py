from min_skew import min_skew
from frequent_words_with_mismatches_and_reverse_complements import frequent_words_with_mismatches_and_reverse_complements

lines = [line.rstrip() for line in open('salmonella_enterica_genome.txt')]
seq = "".join(lines)

possible_ori = min_skew(seq)[0]
#min_skew returns 3764856 & 3764858. Chose the first arbitrarily since they are 2 nt's apart

window_size = 500
#window size suggested by text

print(frequent_words_with_mismatches_and_reverse_complements(seq[possible_ori: possible_ori + window_size], 9, 2))
#9-mer suggested by text. Narrowed d to 2, which returned 'GATCCAGGC' & 'GCCTGGATC', reverse
#complements, making it likely that they are the DnaA box
