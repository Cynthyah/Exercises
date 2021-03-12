# FindStringusingRecursive.py 
# Create a function that you return True if the exat word is find in the string or sentence

# string = "I love bananas and apples."
# is the word ana in the string/sentence? return True
# is the word live in the string/sentence ? return False

# if the string/sentence or the word is empty return False

def solution(string, substring, i=0):
    string = ''.join(string.split()) # get rid of all spaces
    
    if len(string) == 0 or len(substring) == 0: # if string is null return False
        return False
   
    if substring == string[0:len(substring)]: # if find the substring return True
        return True

    i += 1 
    find = solution(string[i:],substring,i)
    if find: return True
    else: return False

    
    
# Testing
print(solution("amora","amor")) 
print(solution("O amor é lindo!","amora"))

