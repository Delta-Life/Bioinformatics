# Binary Search
# http://rosalind.info/problems/bins/

from utilities import get_file, bins, get_answer_file

with get_file() as file:
    n = int(file.readline().rstrip())
    k = int(file.readline().rstrip())
    sorted_array = list(map(int, file.readline().split()))
    num_array = list(map(int, file.readline().split()))

with get_answer_file() as file:
    print(' '.join(map(str, [bins(i, sorted_array) for i in num_array])), file=file)