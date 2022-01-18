# Implement PatternToNumber
# https://rosalind.info/problems/ba1l/

from utilities import get_file, get_answer_file

def pattern_to_num(pattern):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    result = 0
    for n, i in enumerate(pattern[::-1]):
        result += 4 ** n * nucleo_dict[i]

    return result

with get_file() as file:
    pattern = file.readline().rstrip()

with get_answer_file() as file:
    print(pattern_to_num(pattern), file=file)