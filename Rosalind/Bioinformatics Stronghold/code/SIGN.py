# Enumerating Oriented Gene Orderings
# http://rosalind.info/problems/sign/

from utilities import get_file, get_permutations, get_answer_file

def get_sign(len):
    result = []
    if len == 0:
        return[[]]

    for i in [-1, 1]:
        for sub_sign in get_sign(len-1):
            result += [[i] + sub_sign]
    
    return result

with get_file() as file:
    num = int(file.readline().rstrip())
    arr1 = [-i for i in range(1, num+1)]

with get_answer_file() as file:
    perm_array = get_permutations(arr1, num)
    arr2 = get_sign(len(arr1))
    print(len(perm_array)*len(arr2), file=file)
    for i in perm_array:
        for j in arr2:
            for k, l in zip(i, j):
                print(k*l, end=" ", file=file)
            print("", file=file)