# How many distinct numbers in Array

# Given an array A consisting of N integers, returns the number of distinct values in array A.
# A = [2,1,1,2,3,1] -> should return 3 because we have 3 different numbers

# Important
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    return len(set(A))   

# Testing     
print(solution([2,1,1,2,3,1]))

# Detected time complexity: O(N*log(N)) or O(N)