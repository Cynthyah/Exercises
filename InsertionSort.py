# InsertionSort - create a function that sorted a list using Insertion Sort
# Here a good explanation -> https://www.youtube.com/watch?v=K4CuPzdiAIo

def solution(A):
    """ 
    Go through the list and separated the list in sorted <-- | --> unsorted
    """
    n = len(A)
    for i in range(0,n-1):
        x = A[i+1]
        j = i
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] = x
    return A

# Testing
print(solution([6,4,5,1,0,9]))