# find out the missing number in a list

# A = [2,3,1,5] - the missing number is 4

# Importatnt
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

def solution(A):
    if len(A) == 0:
        return 1
    if A[0] == 1 and len(A) == 1:
        return 2
    A = sorted(A)
    current = A[0]
    for n in range(1,len(A)+1):
        if n != A[n-1]:
            return n
    return n+1
            
# Testing
A = [2,3,4,5,6,7,8,9,10,11]
print(solution(A))

# Detected time complexity: O(N) or O(N * log(N))