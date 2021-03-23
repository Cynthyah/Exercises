# PassingCar -A non-empty array A consisting of N integers is given. 
# The consecutive elements of array A represent consecutive cars on a road.

# Array A contains only 0s and/or 1s: 
#       0 represents a car traveling east,
#       1 represents a car traveling west.

# The goal is to count passing cars. 
# We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, 
# is passing when P is traveling to the east and Q is traveling to the west.

# For example, consider array A = [0,1,0,1,1] return 5
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

# Write a function that, given a non-empty array A of N integers,
# returns the number of pairs of passing cars.
# The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

# Important:
# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.

def solution(A):
    p_0 = []
    p_1 = []
    i = 0
    for n in A:
        if n == 0:
            p_0.append(i)
        else:
            p_1.append(i)
        i += 1
    
    pares = 0
    for P in p_0: 
        for Q in p_1:  
            if Q > P: 
                pares += 1
                if pares > 1E9:
                    return -1
            
    return(pares)

def solution1(A):
    N = len(A)

    cars = 0
    result = 0
    for ind in range(N):
        if A[ind] == 0:
            cars += 1
        else:
            result += cars

            if result > 1E9:
                return -1

    return result

# Testing 
import random
A = [random.randint(0, 1) for _ in range(100000)] 

print(solution (A)) # Detected time complexity: O(N ** 2) - 60%

print(solution1(A)) # Detected time complexity: O(N) - 100%

