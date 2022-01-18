# Rabbits and Recurrence Relations
# http://rosalind.info/problems/fib/

from utilities import get_file, get_answer_file

def fibo(n, k):
    fibArr = [1, 1]
    for _ in range (n - 2):
        fibArr.append(fibArr[-2] * k + fibArr[-1])
    return fibArr[-1]

with get_file() as file:
    n, k = map(int, file.readline().split())

with get_answer_file() as file:
    print(fibo(n, k), file=file)