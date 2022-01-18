# Introduction to Random Strings
# http://rosalind.info/problems/prob/

from collections import Counter
from utilities import get_file, get_answer_file
import math

def get_logarithm(strand, property_array):
    count = Counter(strand)
    AT = count['A'] + count['T']
    GC = count['G'] + count['C']
    return ["{:0.3f}".format(AT*math.log10((1-i)/2) + GC*math.log10(i/2)) for i in property_array]

with get_file() as file:
    strand = file.readline().rstrip()
    property_array = map(float, file.readline().split())

with get_answer_file() as file:
    logarithm_array = get_logarithm(strand, property_array)
    print(" ".join(logarithm_array), file=file)