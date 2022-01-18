# Locating Restriction Sites
# http://rosalind.info/problems/revp/

from utilities import get_file, read_FASTA, get_complement_strand

def find_palindrome(strand):
    complement_strand = get_complement_strand(strand)
    palindrom_array = []
    for i in range(len(strand)):
        palindrome_length = 0
        for j in range(4, 13):
            if(strand[i:i+j] == complement_strand[len(strand)-j-i:len(strand)-i]):
                palindrome_length = j
        if palindrome_length != 0:
            palindrom_array.append([i+1, palindrome_length])
    
    return palindrom_array


with get_file() as file:
    _, strand = read_FASTA(file)

strand = strand[0]
palindrome_array = find_palindrome(strand)

for i in palindrome_array:
    print(i[0], i[1])