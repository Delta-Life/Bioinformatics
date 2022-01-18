'''
codes of common fuctions

list:
argmax
comb
convert_DNA_to_RNA
factor
get_answer_file
get_codon_table
get_complement_strand
get_file
read_all
read_FASTA
translate_strand
'''

import sys

def argmax(tmp_array):
    return tmp_array.index(max(tmp_array))

def binary_search(target, data):
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def comb(n, k):
    return factor(n) / (factor(n-k) * factor(k))

def convert_DNA_to_RNA(strand):
    return strand.replace('T', 'U')

def factor(n):
    return n * factor(n-1) if n > 1 else 1

def get_answer_file():
    filePath = sys.argv[0].split("\\")
    return open("/".join(filePath[:-1]) + "/../answer/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'w')

def get_codon_table():
    given_codon_string = """UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G""".split()
    return list([given_codon_string[i]] + [given_codon_string[i+1]] for i in range(0, len(given_codon_string), 2))

def get_complement_strand(strand):
    translator = str.maketrans("ATGC", "TACG")
    return strand[::-1].translate(translator)

def get_file():
    filePath = sys.argv[0].split("\\")
    return open("/".join(filePath[:-1]) + "/../data/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'r')

def read_all(file):
    return "".join(line.rstrip() for line in file.readlines())

def read_FASTA(file):
    name_array = []
    strand_array = []
    for line in file.readlines():
        line = line.rstrip()
        if line[0] == '>':
            name_array.append(line[1:])
            strand_array.append('')
        else:
            strand_array[-1] += line
    return name_array, strand_array

def translate_strand(strand):
    codon_dict = dict(get_codon_table())
    while len(strand) % 3 != 0:
        strand = strand[:-1]
    codon_string = "".join(codon_dict[strand[i:i+3]] for i in range(0, len(strand), 3))
    return codon_string