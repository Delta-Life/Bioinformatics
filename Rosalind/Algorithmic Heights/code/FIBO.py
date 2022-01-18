# Fibonacci Numbers
# http://rosalind.info/problems/fibo/

from utilities import get_file, get_answer_file

def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n

with get_file() as file:
    num = int(file.readline())

with get_answer_file() as file:
    print(fibo(num), file=file)