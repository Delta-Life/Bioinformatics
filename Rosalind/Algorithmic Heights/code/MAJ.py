# Majority Element
# http://rosalind.info/problems/maj/

from collections import Counter
from utilities import get_file, get_answer_file

def majority_element(arrays, len_of_array):
    result = []
    for i in range(len(arrays)):
        tmpDict = Counter(arrays[i])
        tmpNum = max(tmpDict, key=tmpDict.get)
        if tmpDict[tmpNum] > len_of_array // 2:
            result.append(tmpNum)
        else:
            result.append(-1)

    return result

with get_file() as file:
    len_of_input, len_of_array = map(int, file.readline().split())
    arrays = []
    for i in range(len_of_input):
        arrays.append(list(map(int, file.readline().split())))

with get_answer_file() as file:
    majority_array = majority_element(arrays, len_of_array)
    print(" ".join(map(str, majority_array)), file=file)