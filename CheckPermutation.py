# CheckPermutation - Check whether array A is a permutation. 

# A non-empty array A consisting of N integers is given.
# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A = [4,1,3,2] is a permutation - return 1
# but array A = [4,1,3] is not a permutation, because value 2 is missing - return 0

# the function need return 1 if it is permutation or 0 if it is not.

# Important
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    seq = 1
    for n in sorted(A):
        if n == seq:
            seq += 1
        else:
            return 0
    return 1

# Testing
A = [4,1,2,3]
print(solution(A))

# Detected time complexity: O(N) or O(N * log(N)) 