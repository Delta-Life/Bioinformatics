# Finding a Shared Motif
# http://rosalind.info/problems/lcsm/

from utilities import get_file, read_FASTA, get_answer_file

def find_common_motif(strand_array):
    minStrand = strand_array[strand_array.index(min(strand_array, key=len))]
    motif = ''

    for i in range(len(minStrand), 0, -1):
        for j in range(0, len(minStrand) - i + 1):
            flag = True
            for strand in strand_array:
                if minStrand[j:j+i+1] not in strand:
                    flag = False
            if flag == True:
                motif = minStrand[i:j+i+1]
                break
        if len(motif) != 0:
            break

    return motif


with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(find_common_motif(strand_array), file=file)