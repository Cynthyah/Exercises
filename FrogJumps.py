# Count minimal number of jumps from position X to Y.

# X - Start point    
# Y - Final point
# D - step

# X = 10, Y = 85, D = 30 -> 40,70,100
# Retun 3

# Important
# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.

def solution(X,Y,D):
    jump = (Y - X) // D
    if (Y - X) % D > 0:
        jump += 1
    return jump

# Testing   
print(solution(3, 3,7))

# Detected time complexity: O(1)