# Edit Distance Alignment
# https://rosalind.info/problems/edta/

from utilities import get_file, get_answer_file, read_FASTA

def edit_distance(str1, str2):
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

    for i in range(len(cost)):
        cost[i][0] = 1 * i
    for i in range(len(cost[0])):
        cost[0][i] = 1 * i
    for i in range(1, len(cost)):
        for j in range(1, len(cost[0])):
            if str1[j-1] == str2[i-1]:
                cost[i][j] = min(cost[i-1][j]+1, cost[i][j-1]+1, cost[i-1][j-1])
            else:
                cost[i][j] = min(cost[i-1][j]+1, cost[i][j-1]+1, cost[i-1][j-1]+1)
    
    i, j = len(str2), len(str1)
    aligned_str1 , aligned_str2 = "", ""
    while i != 0 and j != 0:
        if cost[i][j] == cost[i-1][j] + 1:
            i -= 1
            aligned_str1 += "-"
            aligned_str2 += str2[i]
        elif cost[i][j] == cost[i][j-1] + 1:
            j -= 1
            aligned_str1 += str1[j]
            aligned_str2 += "-"
        else:
            i -= 1
            j -= 1
            aligned_str1 += str1[j]
            aligned_str2 += str2[i]

    return cost[-1][-1], aligned_str1[::-1], aligned_str2[::-1]


with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print("\n".join(map(str, edit_distance(strand_array[0], strand_array[1]))), file=file)