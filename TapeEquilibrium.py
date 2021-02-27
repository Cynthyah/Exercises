# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
# A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# A = [3,1,2,4,3]

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7 
# function should return 1, as explained above.
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(A):
    part1 = A[0]
    part2 = sum(A[1:])
    dif = abs(part1 - part2)
    if len(A) == 2:
        return dif
    min_dif = [dif]
    for cursor in A[1:-1:]:
        part1 += cursor
        part2 -= cursor
        dif = abs(part1 - part2)
        min_dif.append(dif)
        if dif == 0:
            break
    return min(min_dif)

         
# Testing
A = [-10, -20, -30, -40, 100]
print(solution(A))

# Detected time complexity: O(N)

