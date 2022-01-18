# Generate the d-Neighborhood of a String
# https://rosalind.info/problems/ba1n/

import time
from itertools import combinations, product
from utilities import get_file, get_answer_file, hamming_distance
'''
neighbors function is using itertools.
neighbors2 function is using dynamic programming.
neighbors function is 8 times faster than neighbors2.
'''

def neighbors(pattern, d):
    result = []
    for i in combinations([i for i in range(len(pattern))], d):
        for j in product("ATGC", repeat=d):
            tmp_pattern = list(pattern)
            for k, l in zip(i, j):
                tmp_pattern[k] = l
            result.append(''.join(tmp_pattern))
    return set(result)

def neighbors2(Pattern, d):
    if d==0 : return {Pattern}
    if len(Pattern)==1 : return {'A','T','G','C'}
    
    Neighborhood = set()
    Suffix = neighbors2(Pattern[1:],d)
    
    for i in Suffix:
        if (hamming_distance(Pattern[1:],i) < d):
            for x in ['A','T','G','C']: Neighborhood.add(x+i)
        else: Neighborhood.add(Pattern[0]+i)
            
    return Neighborhood

with get_file() as file:
    pattern = file.readline().rstrip()
    d = int(file.readline().rstrip())

'''
start = time.time()
neighbors(pattern, d)
lap1 = time.time()
neighbors2(pattern, d)
end = time.time()
print(f"neighbors with itertools : {lap1 - start:.5f} sec")
print(f"neighbors with dynamic programming : {end - lap1:.5f} sec")
'''

with get_answer_file() as file:
    for i in neighbors(pattern, d):
        print(i, file=file)
