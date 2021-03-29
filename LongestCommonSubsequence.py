# LongestCommonSubsequence.py
# The longest common subsequence (LCS) problem is the problem of finding the 
# longest subsequence common to all sequences in a set of sequences 
# (often just two sequences). 

def lcs(s1,s2):
    long = 0
    comon = []
    for c1 in s1:
        if c1 in comon: next
        for c2 in s2:
            if c1 == c2:
                if c1 not in comon:
                    comon.append(c1)
                    long += 1
                break
    
    return long

# Testing
print(lcs("ABCDGH","AEDFHR"))
print(lcs("abc","def "))
print(lcs("ACADB","CBDA"))
print(lcs("AGGTAB","GXTXAYB"))
print(lcs("ABCDGH","AEDFHR"))