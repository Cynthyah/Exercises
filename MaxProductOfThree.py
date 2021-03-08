# MaxProductOfThree - Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).

# A = [-3,1,2,-2,5,6] 

# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Important
# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(A):
    A = sorted(A)
    return max(A[-1] * A[-2] * A[-3],A[0] * A[1] * A[-1])
        
# Testing
print(solution([-3,1,2,-2,5,-6]))
print(solution([-5, -5, -5, -4]))
print(solution([-5, -6, -4, -7, -10]))

# Detected time complexity: O(N * log(N))