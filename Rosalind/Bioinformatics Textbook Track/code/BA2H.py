# Implement DistanceBetweenPatternAndStrings
# https://rosalind.info/problems/ba2h/

from utilities import get_file, get_answer_file, hamming_distance

def distance_between_pattern_and_strings(pattern, strand_array):
    k = len(pattern)
    distance = 0
    for strand in strand_array:
        min_distance = k
        for i in range(len(strand)-k+1):
            tmp_distance = hamming_distance(pattern, strand[i:i+k])
            if tmp_distance < min_distance:
                min_distance = tmp_distance
                if min_distance == 0:
                    break
        distance += min_distance
    return distance
            

with get_file() as file:
    pattern = file.readline().rstrip()
    strand_array = file.readline().split()

with get_answer_file() as file:
    print(distance_between_pattern_and_strings(pattern, strand_array), file=file)