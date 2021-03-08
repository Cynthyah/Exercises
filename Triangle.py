# Triangle - Determine whether a triangle can be built from a given set of edges.

# A = [10,2,5,1,8,20]
# Triplet (0, 2, 4) is triangular return 1.

# A = [10,50,5,1]
# return 0

# returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
# Important
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

def solution(A):
    A = sorted(A)
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2] and A[i+1] + A[i+2] > A[i] and A[i+2] + A[i] > A[i+1]:
            return 1
        
    return 0 

# Testing
print(solution([10,2,5,1,8,20]))
print(solution([10,50,5,1]))

# Detected time complexity:O(N*log(N))