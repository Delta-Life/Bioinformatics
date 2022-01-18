# Implement NumberToPattern
# https://rosalind.info/problems/ba1m/

from utilities import get_file, get_answer_file

def num_to_pattern(index, length):
    nucleo_dict = {0:'A', 1:'C', 2:'G', 3:'T'}
    result = ''
    while index !=0:
        key = index % 4
        index = index // 4
        result += nucleo_dict[key]
    
    while len(result) < length:
        result += 'A'

    return result[::-1]

with get_file() as file:
    index = int(file.readline().rstrip())
    length = int(file.readline().rstrip())

with get_answer_file() as file:
    print(num_to_pattern(index, length), file=file)