# Interleaving Two Motifs
# https://rosalind.info/problems/scsp/

from utilities import get_file, get_answer_file

def get_supersequence(s, t):
    supersequence = []
    align_matrix = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(t) + 1):
        align_matrix[0][i] = i
    for i in range(len(s) + 1):
        align_matrix[i][0] = i
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                align_matrix[j+1][i+1] = align_matrix[j][i]
            else:
                align_matrix[j+1][i+1] = min(align_matrix[j][i+1] + 1, align_matrix[j+1][i] + 1)
    i = len(t)
    j = len(s)

    while i != 0 and j != 0:
        if align_matrix[j][i] == align_matrix[j][i-1] + 1:
            i -= 1
            supersequence.append(t[i])
        elif align_matrix[j][i] == align_matrix[j-1][i] + 1:
            j -= 1
            supersequence.append(s[j])
        elif align_matrix[j][i] == align_matrix[j-1][i-1]:
            i -= 1
            j -= 1
            supersequence.append(s[j])
    
    if i != 0:
        supersequence.append(t[:i])
    else:
        supersequence.append(s[:j])
    
    return "".join(reversed(supersequence))

with get_file() as file:
    s = file.readline().rstrip()
    t = file.readline().rstrip()

with get_answer_file() as file:
    print(get_supersequence(s, t), file=file)