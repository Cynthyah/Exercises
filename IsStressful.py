# The function should recognise if a subject line is stressful.
# A stressful subject line means that all letters are in uppercase, 
# and/or ends by at least 3 exclamation marks, and/or contains at least
#  one of the following “red” words: "help", "asap", "urgent". 
# Any of those "red" words can be spelled in different ways -
# "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," 
# they just can't have any other letters interspersed between them. 

def is_stressful(subj):
    """
        recognize stressful subject
    """
    if subj[-3:] == '!!!' or subj.isupper():
        return True
  
    word = ' '
    for l in subj.lower():
        if l.isalpha():   
            if word[-1] != l:
                word += l
                
    red_words = ['help','asap','urgent']
    for red in red_words:
        if red in word:
            return True
   
    return False
    


if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi!") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("h!e!l!p") == True, "Second"
    assert is_stressful("He loves peace") == False, "333"
    assert is_stressful("We need you A.S.A.P.!!") == True, "333"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "333"
    assert is_stressful("Headlamp, wastepaper bin and supermagnificently") == False, "333"
    print('Done! Go Check it!')

