# Consensus and Profile
# http://rosalind.info/problems/cons/

from utilities import get_file, read_FASTA, argmax, get_answer_file

def consensus_strand(strand_array):
    dic = {'A':0, 'C':1, 'G':2, 'T':3}
    undic = ['A', 'C', 'G', 'T']
    mat = [[0 for _ in range(4)] for _ in range(len(strand_array[0]))]
    strand = ''

    for i in strand_array:
        for n, j in enumerate(i):
            mat[n][dic[j]] += 1

    for i in mat:
        strand += undic[argmax(i)]
    
    return strand, mat

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    con_strand, mat = consensus_strand(strand_array)
    print(con_strand, file=file)
    print("A: " + " ".join(map(str, (mat[i][0] for i in range(len(mat))))), file=file)
    print("C: " + " ".join(map(str, (mat[i][1] for i in range(len(mat))))), file=file)
    print("G: " + " ".join(map(str, (mat[i][2] for i in range(len(mat))))), file=file)
    print("T: " + " ".join(map(str, (mat[i][3] for i in range(len(mat))))), file=file)