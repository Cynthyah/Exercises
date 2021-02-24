# Find longest sequence of zeros in binary representation of an integer. 

# Write a function that return the length of the longest binary gap
# N = 529 the binary is 1000010001 -> the longest binary gap is 4
# N = 20 the binary is 10100 -> the longest binary gap is 1
# N = 9   the binary is 1001 -> the longest binary gap is 2

# Important: N is an integer within the range [1..2,147,483,647].

def solution(N):
    binary = str(bin(N))[2:]
    longest = 0
    count = 0
    for n in binary:
        if n == "1":
            if count > longest:
                longest = count
            count = 0
        else:
            count += 1
    return longest        

# Testing
print(solution(32))
