# Enumerating Gene Orders
# http://rosalind.info/problems/perm/

from utilities import get_file


def get_permutations(arr, num):
    result = []
    
    if num == 0:
        return [[]]
    
    for n, i in enumerate(arr):
        for sub_permutation in get_permutations(arr[:n] + arr[n+1:], num-1):
            result += [[i] + sub_permutation]
    
    return result

with get_file() as file:
    num = int(file.readline())

arr = [i for i in range(1, num + 1)]
permutations = get_permutations(arr, num)
print(len(permutations))
for i in permutations:
    print(" ".join(map(str, i)))