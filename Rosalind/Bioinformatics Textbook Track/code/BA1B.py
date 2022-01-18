# Find the Most Frequent Words in a String
# https://rosalind.info/problems/ba1b/

from utilities import get_file, get_answer_file

def most_frequent_kmer(k, strand):
    kmer_dict = {strand[i:i+k]:0 for i in range(len(strand)-k+1)}
    for i in range(len(strand)-k+1):
        kmer_dict[strand[i:i+k]] += 1
    return [k for k,v in kmer_dict.items() if max(kmer_dict.values())==v]

with get_file() as file:
    strand = file.readline().rstrip()
    k = int(file.readline().rstrip())

with get_answer_file() as file:
    print(" ".join(most_frequent_kmer(k, strand)), file=file)