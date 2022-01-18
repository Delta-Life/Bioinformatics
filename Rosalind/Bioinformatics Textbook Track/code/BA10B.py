# Compute the Probability of an Outcome Given a Hidden Path
# http://rosalind.info/problems/ba10b/

from utilities import get_file, get_answer_file

def readDic(f):
    return dict((state, i) for i, state in enumerate(f.readline().split()))
def readMat(f):
    states = f.readline().split()
    return [list(map(float, i.split()[1:])) for i in f.readlines()]

with get_file() as file:
    str1 = file.readline().rstrip()
    file.readline()
    dic1 = readDic(file)
    file.readline()
    str2 = file.readline().rstrip()
    file.readline()
    dic2 = readDic(file)
    file.readline()
    mat = readMat(file)
    p = 1

for i, j in zip(str1, str2):
    p *= mat[dic2[j]][dic1[i]]

with get_answer_file() as file:
    print('%.12g' % p, file=file)