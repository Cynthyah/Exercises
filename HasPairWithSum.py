# PairsSum - find the pairs that is equal a given sum

# A = [1,2,3,9] 
# S = 8
# Return must be -1 -> no pairs with sum 8

# A = [1,2,4,4]
# S = 8
# Return (4,4)

def solution(A,S):
    found = []
    pairs = []
    for num in A:
        k = S - num
        if k not in found:
            found.append(num)
        else:
            pairs.append((num,k))
    return pairs

# Testing
print(solution([7,0,7,1,2,4,4,6],7))
print(solution([0,1,2,4,8],10))
print(solution([0,1,-1,0,4,8],0))