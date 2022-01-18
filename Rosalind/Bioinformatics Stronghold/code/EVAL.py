# Expected Number of Restriction Sites
# https://rosalind.info/problems/eval/

from utilities import get_file, get_answer_file

def get_motif_probs(length, gc_content_array, strand):
    
    result = []
    for gc_content in gc_content_array:
        prob_dict = {'G':gc_content/2, 'C':gc_content/2, 'A':(1-gc_content)/2, 'T':(1-gc_content)/2}
        prob = 1

        for i in strand:
            prob *= prob_dict[i]

        result.append(prob * (length - len(strand) + 1))
    
    return result

with get_file() as file:
    length = int(file.readline().rstrip())
    strand = file.readline().rstrip()
    gc_content_array = list(map(float, file.readline().split()))

with get_answer_file() as file:
    print(" ".join(map(str, get_motif_probs(length, gc_content_array, strand))), file=file)