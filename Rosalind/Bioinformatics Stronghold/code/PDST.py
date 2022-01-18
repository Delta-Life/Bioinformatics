# Creating a Distance Matrix
# https://rosalind.info/problems/pdst/

from utilities import get_file, get_answer_file, read_FASTA, hamming_distance

def get_distance_matrix(strand_array):
    length = len(strand_array[0])
    result = []
    for i in strand_array:
        result.append([])
        for j in strand_array:
            result[-1].append("{:.5f}".format(hamming_distance(i, j)/length))
    
    return result

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    for i in get_distance_matrix(strand_array):
        print(" ".join(map(str, i)), file=file)