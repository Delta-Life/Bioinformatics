# Finding a Spliced Motif
# http://rosalind.info/problems/sseq/

from utilities import get_file, read_FASTA, get_answer_file

def find_subsequence(strand, substrand):
    result = []
    for n, i in enumerate(strand):
        if len(substrand) == 0:
            break
        if i == substrand[0]:
            result.append(n + 1)
            substrand = substrand[1:]
    
    return result


with get_file() as file:
    name_array, strand_array = read_FASTA(file)

with get_answer_file() as file:
    index_array = find_subsequence(strand_array[0], strand_array[1])
    print(" ".join(map(str, index_array)), file=file)