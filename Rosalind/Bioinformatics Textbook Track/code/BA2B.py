# Find a Median String
# https://rosalind.info/problems/ba2b/

from utilities import get_file, get_answer_file, hamming_distance

def most_frequent_kmer(k, strand_array):
    result = {}
    for i in strand_array:
        for j in range(len(i)-k+1):
            result[i[j:j+k]] = 0
    for strand in strand_array:
        kmer_dict = {i:99 for i in result.keys()}
        for i in range(len(strand)-k+1):
            for j in kmer_dict.keys():
                    kmer_dict[j] = min(hamming_distance(strand[i:i+k], j), kmer_dict[j])
        for key, value in kmer_dict.items():
            result[key] += value
    return sorted([key for key, value in result.items() if value==min(result.values())])

with get_file() as file:
    k = int(file.readline().rstrip())
    strand_array = []
    for i in file.readlines():
        strand_array.append(i.rstrip())

with get_answer_file() as file:
    print(most_frequent_kmer(k, strand_array)[0], file=file)