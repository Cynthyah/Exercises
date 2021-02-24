# Rotate an array to the right by a given number of rotation

# Array [1,2,3,4] rotate 2 times
# [4,1,2,3] -> [3,4,1,2] return [3,4,1,2]

# Important
# The length of array(N) and the number of rotatio(K) are integers between [0..100];
# Each element of array(A) is an integer between [−1,000..1,000].


def solution(A,K): # A - array, K - number of rotation
    if A != []: # checking if empty to avoid error      
        for rotation in range(K):
            A_rotated = []
            A_rotated.append(A[-1])
            for i in A[:-1]:
                A_rotated.append(i)
            A = A_rotated
    return (A) 

# Testing
print(solution([1,2,3,4],2))