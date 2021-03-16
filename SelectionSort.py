# SelectionSort - create a function that sorted a list using Selection Sort
# Here a good explanation -> https://www.youtube.com/watch?v=f8hXR_Hvybo

def solution(A):
    """ Go through all element of the list. If the small number is founded
    then we put it as first of the list
    """
    n = len(A)
   
    for i in range(n-2):
        min = A[i]
        for j in range(i+1,n):
            if A[j] <= min:
                min = A[j]
                i_min = j
        A[i_min] = A[i]
        A[i] = min
        
    return A

# Testing
print(solution([6,4,5,1,0,9]))