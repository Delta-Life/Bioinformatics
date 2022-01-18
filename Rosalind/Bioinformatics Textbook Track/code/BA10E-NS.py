# Construct a Profile HMM
# http://rosalind.info/problems/ba10e/

from utilities import get_file, get_answer_file

def get_HMM_profile(string_array, sigma):
    print("")

def ConstructProfileHMM(theta,Alphabet,Alignment,sigma=0):
    #   CountChars
    #
    #   Used to count alphabetical characters in specified column of alignment
    #
    #   Parameters: 
    #       m     Number of sequences
    #       j     The column to be counted
    #       K     Number of symbols in Alphabet
    #
    #  Returns:
    #       Number of symbols from alphabet in column i
    
    def CountChars(m,j,K):
        Counts = [0]*K
        for i in range(m):
            if Alignment[i][j] in Alphabet:
                Counts[Alphabet.index(Alignment[i][j])]+=1
        return Counts 

    def create_states(Conserved):
        Product        = [[] for column in Conserved if column]
        Product.append([])
        return Product
        
    def create_state_indices(Conserved):
        def get_symbol(State):
            return (State,index)
        
        index   = 0
        Product = [get_symbol('S'),get_symbol('I')]
        for column in Conserved:
            if not column: continue
            index += 1
            Product.append(get_symbol('M'))
            Product.append(get_symbol('D'))
            Product.append(get_symbol('I'))
        index += 1
        Product.append(get_symbol('E'))
        return Product
    
    def create_state_counts(StateIndices):
        Product  = {}
        for s,i in StateIndices:
            for t,j in StateIndices:
                if s=='S':
                    if t=='I' and j==0:
                        Product[(s,i),(t,j)] = 0
                    elif t in ['M','D'] and j==1:
                        Product[(s,i),(t,j)] = 0
                elif s=='I':
                    if i==0:
                        if t=='I' and j==0:
                            Product[(s,i),(t,j)] = 0
                        elif t in ['M','D'] and j==1:
                            Product[(s,i),(t,j)] = 0
                    else:
                        if (t=='I' and j==i) or (t in ['M','D'] and j==i+1):
                            Product[(s,i),(t,j)] = 0
                        if t=='E' and j==i+1:
                            Product[(s,i),(t,j)] = 0                            
                elif s in ['M','D']:
                    if (t=='I' and j==i) or (t in ['M','D'] and j==i+1):
                        Product[(s,i),(t,j)] = 0
                    if t=='E' and j==i+1:
                        Product[(s,i),(t,j)] = 0
                else:
                    assert(s=='E')

        return Product

    def create_emission_counts(StateIndices,Alphabet):
        Product  = {}
        for index in StateIndices:
            for ch in Alphabet:
                Product[(index,ch)] = 0
        return Product
    
    def create_state_frequencies(StateCounts,StateIndices):
        Totals  = {i:0 for i in StateIndices}
    
        for key,count in StateCounts.items():
            ((s,i),_) = key
            Totals[(s,i)] += count
            
        Product = {}
        for key,count in StateCounts.items():
            ((s,i),_) = key
            Product[key] = count/Totals[(s,i)] if Totals[(s,i)]>0 else 0        
        return Product
    
    def create_emission_frequencies(EmissionCounts, StateIndices):
        Totals  = {i:0 for i in StateIndices}
        for key,count in EmissionCounts.items():
            ((s,i),_) = key
            Totals[(s,i)] += count        
        Product = {}
        for key,count in EmissionCounts.items():
            ((s,i),_) = key
            Product[key] = count/Totals[(s,i)] if Totals[(s,i)]>0 else 0 
 
        return Product   
    
    #    Useful constants - lengths of arrays
    
    K              = len(Alphabet)      #  Number of symbols in alphabet
    m              = len(Alignment)     #  Number of strings in alignment
    n              = len(Alignment[0])  #  Number of symbols in each alignment  
    for Sequence in Alignment[1:]:      #  All sequences should be the same length
        assert(n == len(Sequence))
        
    #    construct profile - Number of symbols from alphabet in each column
    
    Counts         = [CountChars(m,j,K) for j in range(n)]
        
    #    Indicate whether or not symbols in column are over threshold
    #    If theta is maximum proportion of deleted symbols, 1-theta is
    #    maximum number of conserved.
    
    Conserved      = [sum(Count) > (1-theta)*K for Count in Counts]
    
    column_count   = sum(1 for column in Conserved if column)
    
    Merges         = create_states(Conserved)
    Inserts        = create_states(Conserved)
    Deletes        = create_states(Conserved)
    StateIndices   = create_state_indices(Conserved)
    StateCounts    = create_state_counts(StateIndices)
    EmissionCounts = create_emission_counts(StateIndices,Alphabet)
    
    Runs        = []           
    for Sequence in Alignment:
        previous =  'S'
        States   = [previous]
        j = 0
        for i in range(n):
            ch = Sequence[i]
            if Conserved[i]:
                j+=1
                if ch in Alphabet:
                    Merges[j].append((previous,ch))
                    previous =  'M'
                    States.append(previous)
                elif ch == '-':
                    Deletes[j].append((previous,ch))
                    previous =  'D'
                    States.append(previous)
                else:
                    raise RosalindException(f'Invalid {ch}')
            else:
                if ch in Alphabet:
                    Inserts[j].append((previous,ch))
                    previous =  'I'
                    States.append(previous)
                elif ch == '-':
                    pass
                else:
                    raise RosalindException(f'Invalid {ch}')
        States.append('E') 
        Runs.append(States)
        print (f'Counting {Sequence} {"".join(States)}')
        index     = 0
        previous  = None
        seq_index = 0
        for state in States:
            while seq_index < len(Sequence)-1 and Sequence[seq_index]=='-':
                seq_index += 1
            if state in ['M','D','E']:
                index = index+1
            if previous != None:
                StateCounts[previous,(state,index)] += 1
                if state in ['M','I']:
                    EmissionCounts[(state,index),Sequence[seq_index]] += 1
                    seq_index += 1
            previous = (state, index)
            
    return (StateIndices, 
            create_state_frequencies(StateCounts, StateIndices),
            create_emission_frequencies(EmissionCounts, StateIndices))

with get_file() as file:
    threshold = float(file.readlines().rstrip())
    file.readline()
    sigma = file.readline().split()
    file.readline()
    string_array = []
    for i in file.readlines():
        string_array.append(i.rstrip())
    
with get_answer_file() as file:
    print()