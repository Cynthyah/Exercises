# MissingInteger - Find the smallest positive integer that does not occur in a given sequence. 
# Given an array A of N integers, returns the smallest positive integer (greater than 0) 
# that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#                    A = [1, 2, 3], the function should return 4.
#                    A = [−1, −3], the function should return 1.

# Important
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    A = sorted(set(A))
    small = 1
    for n in A:
        if n > 0: # positive
            if n > small:
                break
            small += 1
    return small

# Testing
A = [1,3,6,4,1,2] # result 5
print(solution(A))

# Detected time complexity: O(N) or O(N * log(N))
