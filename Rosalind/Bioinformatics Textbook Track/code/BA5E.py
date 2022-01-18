# Find a Highest-Scoring Alignment of Two Strings
# https://rosalind.info/problems/ba5e/

from utilities import get_file, get_answer_file, load_blosum62, load_protein_dictionary

def get_global_alighment(str1, str2, penalty, score_matrix):
    protein_dict = load_protein_dictionary()
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(cost)):
        cost[i][0] = -penalty * i
    for i in range(len(cost[0])):
        cost[0][i] = -penalty * i
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j]-penalty, cost[i][j-1]-penalty, cost[i-1][j-1]+score_matrix[protein_dict[str2[i-1]]][protein_dict[str1[j-1]]])
            
    i = len(str2)
    j = len(str1)
    result = [[], []]
    while i != 0 and j != 0:
        if cost[i][j-1] -penalty == cost[i][j]:
            j -= 1
            result[1].append("-")
            result[0].append(str1[j])
        elif cost[i-1][j] -penalty == cost[i][j]:
            i -= 1
            result[0].append("-")
            result[1].append(str2[i])
        else:
            j -= 1
            i -= 1
            result[0].append(str1[j])
            result[1].append(str2[i])
    return[cost[-1][-1], "".join(reversed(result[0])), "".join(reversed(result[1]))]


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    BLOSUM62 = load_blosum62()
    print("\n".join(map(str, get_global_alighment(str1, str2, 5, BLOSUM62))), file=file)
