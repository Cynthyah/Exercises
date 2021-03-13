# MaxCounters - Calculate the values of counters after applying all alternating operations: 
# increase counter by 1; set value of all counters to current maximum. 

# You are given N counters, initially set to 0, and you have two possible operations on them:
# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.

# A non-empty array A of M integers is given. This array represents consecutive operations:
# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.

# For example, given integer N = 5 and array A such that:
# A = [3,4,4,6,1,4,4]
    
# the values of the counters after each consecutive operation will be:
#    (0, 0, 1, 0, 0)
#    (0, 0, 1, 1, 0)
#    (0, 0, 1, 2, 0)
#    (2, 2, 2, 2, 2)
#    (3, 2, 2, 2, 2)
#    (3, 2, 2, 3, 2)
#    (3, 2, 2, 4, 2)

# The function should return [3, 2, 2, 4, 2], as explained above.

# Important
# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

def solution(N, A):
    counters = {0: 0}
    max_counter = 0
    for c in A:
        if c == N + 1:
            counters = {0: max_counter}
        else:
            counters[c] = counters.get(c, counters[0]) + 1
            max_counter = max(max_counter, counters[c])
    
    return [counters.get(c, counters[0]) for c in range(1, N + 1)]

# Testing
A = [3, 4, 4, 6, 1, 4, 4]
A = [2, 1, 1, 2, 1]
print(solution(5, A))

# Detected time complexity: O(N + M)
