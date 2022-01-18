# Find Patterns Forming Clumps in a String
# https://rosalind.info/problems/ba1e/

from utilities import get_file, get_answer_file

def clump(k, l, t, strand):
    frequency_table = {}
    result = []

    for i in range(len(strand) - k + 1):
        if strand[i:i+k] in frequency_table:
            frequency_table[strand[i:i+k]][0] += 1
            frequency_table[strand[i:i+k]].append(i)
        else:
            frequency_table[strand[i:i+k]] = [1, i]
    
    for i in frequency_table:
        if frequency_table[i][0] >= t:
            for index in range(1, len(frequency_table[i])-t+1):
                if frequency_table[i][index+t-1] - frequency_table[i][index] <= l - k:
                    result.append(i)
                    break
    
    return sorted(result)


with get_file() as file:
    strand = file.readline().rstrip()
    k, l, t = map(int, file.readline().split())

with get_answer_file() as file:
    print(" ".join(clump(k, l, t, strand)), file=file)