# NumberOfDiscIntersections - Compute the number of intersections in a sequence of discs.

# We draw N discs on a plane. The discs are numbered from 0 to N − 1. 
# An array A of N non-negative integers, specifying the radiuses of the discs, is given. 
# The J-th disc is drawn with its center at (J, 0) and radius A[J].
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# A = [1,5,2,1,4,0]
# position 0 center of radius of 1
# position 1 center of radius of 5 ... where the diameter is 10

# There are eleven (unordered) pairs of discs that intersect
# Given array A shown above, the function should return 11, as explained above.

# Important
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].

def solution(A):
    N = len(A)
    total = 0
    for i in range(N-1):
        di = i + A[i]
        total += min(A[i], N-i-1)
        for j in range(di + 1, N):
            dj = j - A[j]
            if dj <= di:
                total += 1
                if total > 10_000_000:
                    return -1
        
    return total

# Testing    
print(solution([1,5,2,1,4,0]))
print(solution([0,2,4]))
print(solution([1,1,1]))
print(solution([1,2,3]))
print(solution([0,0,3,1]))

# Detected time complexity: O(N**2) - 62% - TimeOut
