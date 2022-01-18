# Mortal Fibonacci Rabbits
# http://rosalind.info/problems/fibd/

from utilities import get_file, get_answer_file

def fibd(n, m):
    birth_array = [1, 0]

    for i in range(n - 2):
        if m <= len(birth_array):
            birth_array.append(sum(birth_array[-m:-1]))
        else:
            birth_array.append(sum(birth_array[0:-1]))
    
    return sum(birth_array[-m:])


with get_file() as file:
    n, m = map(int, file.readline().split())

with get_answer_file() as file:
    print(fibd(n, m), file=file)