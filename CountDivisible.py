# CountDivisible - Compute number of integers divisible by k in range [a..b]. 

# Given three integers A, B and K, 
# returns the number of integers within the range [A..B] 
# that are divisible by K, i.e.:

#    { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, 
# function should return 3, because there are three numbers 
# divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Important
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def solution(A,B,K): # Detected time complexity: O(B-A)

    i = 0
    for n in range(A,B+1):
        if n % K == 0:
            i += 1        
    return i

def solution1(A,B,K): # Detected time complexity: O(1)
    ret = 0
    if B == K:
        if A == 0 and B!= 0:
            return 2
        return 1
    if A == 0:
        ret = 1
        A += K
    if K > A:
        d = K%A
    else:
        d = A%K
    A = A + d
    if A%K == 0:
        ret += 1
    ret += int((B-A) / K)
    return ret
    
import math
def solution2(A, B, K): # Detected time complexity: O(1)
    if 0 < B < K:
        return 0
    else:
        mA = math.ceil(A / K)
        mB = math.floor(B / K) + 1
        return mB - mA

# Testing
print(solution2(0, 2000000000, 1))

# Detected time complexity: O(1)