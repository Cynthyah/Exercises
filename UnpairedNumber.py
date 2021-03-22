# Find value that occurs in odd number of elements.

# Find the number in an non-empty array that does not have pair
# Array [9,3,9,3,9,7,9] pairs 
# A[0] = 9  and A[2] = 9
# A[1] = 3  and A[3] = 3    
# A[4] = 9  and A[6] = 9
# A[5] = 7 no pair
# the function should return 7, as explained in the example above.

# Important
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.

def solution(A):
    A = sorted(A) 
    current = A[0]
    count = 0
    for i in A:
        if current == i:
            count += 1
        else:
            if count % 2 != 0:
               return  current
            count = 1
            
        current = i
    return current

# Testing
print(solution([9,3,9,3,9,7,9]))

# Result
# Detected time complexity: O(N) or O(N*log(N)) 