# MinAvgTwoSlice - Find the minimal average of any slice containing at least two elements. 

# A non-empty array A consisting of N integers is given. 
# A pair of integers (P, Q), such that 0 ≤ P < Q < N, 
# is called a slice of array A (notice that the slice contains at least two elements). 
# The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] 
# divided by the length of the slice. 
# To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A = [4,2,2,5,1,5,8] - return 1
# contains the following example slices:
# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

# Given a non-empty array A consisting of N integers, 
# returns the starting position of the slice with the minimal average. 
# If there is more than one slice with a minimal average, you should 
# return the smallest starting position of such a slice.

# Important
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].


def solution(A): # 60% (Time Out) Detected time complexity: O(N ** 2) 
    min = A[0] + A[1] / 2
    position =0
    for m in range(len(A)):
        avg = A[m]
        for n in A[m+1:]:
            avg = (avg + n) / 2
            if avg < min:
                min = avg
                position = m
    return position

# Testing
print(solution([4,2,2,5,1,5,8])) # 1
print(solution([5, 6, 3, 4, 9])) # 2
print(solution([10, 10, -1, 2, 4, -1, 2, -1])) # 5
print(solution([-10000, -10000])) # 0
print(solution([1,2,3])) 
