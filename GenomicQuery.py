# GenomicRangeQuery - Find the minimal nucleotide from a range of sequence DNA. 

# A DNA sequence can be represented as a string consisting of the letters A, C, G and T, 
# which correspond to the types of successive nucleotides in the sequence. 
# Each nucleotide has an impact factor, which is an integer. 
# Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
# You are going to answer several queries of the form: What is the minimal impact factor 
# of nucleotides contained in a particular part of the given DNA sequence?

# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N 
# characters. There are M queries, which are given in non-empty arrays P and Q, 
# each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the 
# minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

# For example, consider string S = CAGCCTA and arrays P, Q such that:
#    P[0] = 2    Q[0] = 4
#    P[1] = 5    Q[1] = 5
#    P[2] = 0    Q[2] = 6

# The answers to these M = 3 queries are as follows:

# The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
# The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
# The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

# For example, given the string S = CAGCCTA and arrays P, Q such that:
# P[2,5,0]
# Q[4,5,6
# the function should return the values [2, 4, 1], as explained above.

# Important
# N is an integer within the range [1..100,000];
# M is an integer within the range [1..50,000];
# each element of arrays P, Q is an integer within the range [0..N − 1];
# P[K] ≤ Q[K], where 0 ≤ K < M;
# string S consists only of upper-case English letters A, C, G, T.

def Solution(S,P,Q):
    result = []
    
    for p in range(len(P)):
        min_let_factor = 'T'
        for i in S[P[p]:Q[p]+1]:
            if i < min_let_factor:
                min_let_factor = i

        #min_let_factor = min(S[P[p]:Q[p]+1])
        if min_let_factor == 'A':
            factor = 1
        elif min_let_factor == 'C':
            factor = 2
        elif min_let_factor == 'G':
            factor = 3
        else:
            factor = 4
        result.append(factor) 
    return result

# Detected time complexity: O(N * M) ==> 62%


# internet
def Solution1(S,P,Q):
    l = len(S)    
    lastSeen = [[-1,-1,-1,-1] for x in range(l)]
    print(len(lastSeen))
    for x in range(len(S)):
        for i,j in enumerate(list("ACGT")):
            print(x,i,j)
            if S[x] == j:
                lastSeen[x][i] = x
            elif x>0: 
                lastSeen[x][i] = lastSeen[x-1][i]
        print(lastSeen)
    res = []
    for x in range(len(P)):
        startIdx = P[x]
        relevantLastSeen = lastSeen[Q[x]]
        res.append((min([i+1 for i,x in enumerate(relevantLastSeen) if x>=startIdx])))

    return res

# Testing
S = 'CAGCCTA'
P = [2,5,0]
Q = [2,5,6]
print(Solution1(S,P,Q))
