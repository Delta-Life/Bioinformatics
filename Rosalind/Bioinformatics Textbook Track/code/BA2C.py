# Find a Profile-most Probable k-mer in a String
# https://rosalind.info/problems/ba2c/

from utilities import get_file, get_answer_file, hamming_distance

def most_probable_kmer(k, strand, pro_mat):
    index = 0
    most_pro = 0
    nucleo_idct = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(len(strand)-k+1):
        prob = 1
        for n, j in enumerate(strand[i:i+k]):
            prob *= pro_mat[nucleo_idct[j]][n]
        if most_pro < prob:
            most_pro = prob
            index = i
    
    return strand[index:index+k]

with get_file() as file:
    strand = file.readline().rstrip()
    k = int(file.readline().rstrip())
    pro_mat = []
    for i in file.readlines():
        pro_mat.append(list(map(float, i.split())))

with get_answer_file() as file:
    print(most_probable_kmer(k, strand, pro_mat), file=file)