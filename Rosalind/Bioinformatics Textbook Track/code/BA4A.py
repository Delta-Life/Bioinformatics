# Translate an RNA String into an Amino Acid String
# https://rosalind.info/problems/ba4a/

from utilities import get_file, get_answer_file

def get_codon_dict():
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
    return {given_codon_string[i]:given_codon_string[i+1] for i in range(0, len(given_codon_string), 2)}

def get_protein(strand):
    codon_dict = get_codon_dict()
    result = []
    for i in range(len(strand)//3):
        if codon_dict[strand[i*3:i*3+3]] == "Stop":
            break
        result.append(codon_dict[strand[i*3:i*3+3]])
    return "".join(result)

with get_file() as file:
    strand = file.readline().rstrip()

with get_answer_file() as file:
    print(get_protein(strand), file=file)