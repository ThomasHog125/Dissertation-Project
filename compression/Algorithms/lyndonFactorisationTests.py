import LyndonFactorisation
#  tests that a word with multiple lyndon words works correctly
def wordWithLyndonWords():
    if LyndonFactorisation.duval("abacabab") == ["abac","ab","ab"]:
        return True
    else:
        return False
# tests that the empty string isnt set as a lyndon word
def testEmpty():
    if LyndonFactorisation.duval("") == []:
        return True
    else:
        return False
# tests that the algorithm works when the only lyndon word is the string   
def wholeStringLyndonWord():
    if LyndonFactorisation.duval("abcd") == ["abcd"]:
        return True
    else:
        return False
    
######### running tests ##########
print("Tests a word with multiple lyndon words : ",wordWithLyndonWords())
print("Tests an emptry string dosent retrun any lyndon words : ",testEmpty())
print("Tests a string where  the string itself is the only lyndon word : ", wholeStringLyndonWord())
######### end of tests ########### 