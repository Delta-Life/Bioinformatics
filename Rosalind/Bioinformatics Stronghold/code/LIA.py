# Independent Alleles
# http://rosalind.info/problems/lia/

from utilities import get_file, comb

def lia(gen, least):
    num = 2 ** gen
    prob = 0

    for i in range(least, num + 1):
        prob += (3/4) ** (num - i) * comb(num, i) * (1/4) ** i
    
    return prob

with get_file() as file:
    gen, least = map(int, file.readline().split())
    
print("%.3f" % lia(gen, least))