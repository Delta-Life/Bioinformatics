# Genome Assembly as Shortest Superstring
# http://rosalind.info/problems/long/

from utilities import get_file,read_FASTA, get_answer_file

def get_superstring(strand_array):
    strand = strand_array[0]
    strand_array.pop(0)
    while len(strand_array) != 0:
        for i in strand_array:
            for j in range(len(i)//2, len(i))[::-1]:
                if strand[-j:] == i[:j]:
                    strand = strand + i[j:]
                    strand_array.remove(i)
                elif strand[:j] == i[-j:]:
                    strand = i[:-j] + strand
                    strand_array.remove(i)
    return strand

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(get_superstring(strand_array), file=file)