# Enumerating k-mers Lexicographically
# http://rosalind.info/problems/lexf/

from utilities import get_file, get_answer_file

def get_kmer(array, num):
    result = []

    if num == 0:
        return [[]]

    for i in array:
        for sub_kmer in get_kmer(array, num-1):
            result += [[i] + sub_kmer]
    
    return result

with get_file() as file:
    alphabet_array = file.readline().split()
    num = int(file.readline())

with get_answer_file() as file:
    for i in get_kmer(alphabet_array, num):
        print("".join(i), file=file)