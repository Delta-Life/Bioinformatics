# Longest Increasing Subsequence
# http://rosalind.info/problems/lgis/

from utilities import get_file, argmax

def get_LIS(num_array):
    len_array = [0] * len(num_array)
    direction_array = [0] * len(num_array)
    result = []
    result_direction = []

    for i in range(len(num_array)):
        for j in range(i):
            if num_array[j] < num_array[i]:
                if len_array[i] < len_array[j]+1:
                    len_array[i] = len_array[j]+1
                    direction_array[i] = j
    
    result_direction.append(argmax(len_array))
    result.append(num_array[result_direction[-1]])
    while len_array[result_direction[-1]]!=0:
        result_direction.append(direction_array[result_direction[-1]])
        result.append(num_array[result_direction[-1]])
    
    return result[::-1]

with get_file() as file:
    num = int(file.readline())
    num_array = list(map(int, file.readline().split()))

print(" ".join(map(str, get_LIS(num_array))))
print(" ".join(map(str, get_LIS(num_array[::-1])[::-1])))