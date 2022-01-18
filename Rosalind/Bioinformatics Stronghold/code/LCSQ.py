# Finding a Shared Spliced Motif
# https://rosalind.info/problems/lcsq/

from utilities import get_file, read_FASTA, get_answer_file

def lcs(s1, s2):
    matrix = [["" for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    cs = matrix[-1][-1]
    
    return cs

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(lcs(strand_array[0], strand_array[1]), file=file)