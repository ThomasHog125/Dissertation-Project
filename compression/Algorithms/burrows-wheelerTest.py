import suffixTree
import burrowsWheelerTransform

#Tests that if an empty string is submitted there are noo errors
def getSuffixesEmpty():
    root =suffixTree.createTree("")
    # should equal ["$"] as when suffix tree is created an end pointer $ is added
    if burrowsWheelerTransform.getSuffixes(root,"",[]) == ["$"]:
        return True
    else:
        return False
# test that function works on a simple word  
def getSuffixesSimple():
    root =suffixTree.createTree("abc")
    if burrowsWheelerTransform.getSuffixes(root,"",[]) == ["$","c$","bc$","abc$"]:
        return True
    else:
        return False
# test that function works on a complex word  
def getSuffixesComplex():
    root =suffixTree.createTree("abacsbasdsaedssd")
    if burrowsWheelerTransform.getSuffixes(root,"",[]) == ['$', 'd$', 'dssd$', 'dsaedssd$', 'sd$', 'ssd$', 'saedssd$', 'sdsaedssd$', 'sbasdsaedssd$', 'edssd$', 'aedssd$', 'asdsaedssd$', 'acsbasdsaedssd$', 'abacsbasdsaedssd$', 'basdsaedssd$', 'bacsbasdsaedssd$', 'csbasdsaedssd$']:
        return True
    else:
        return False
# tests that the only item in the resturned list is $ when string is empty
def getemptyrotations():
    if burrowsWheelerTransform.getRoatations("") == ["$"]:
        return True
    else:
        return False
# test that the rotations are recieved when a word is entered 
def getRotationsFullWord():
    if burrowsWheelerTransform.getRoatations("") == ['$ABABC', 'C$ABAB', 'BC$ABA', 'BABC$A', 'ABC$AB', 'ABABC$']:
        return True
    else:
        return False
# tests that the BWT of an empty string is $
def BWTempty():
    if burrowsWheelerTransform.Burrows_Wheeler_Transform("") == "$":
        return True
    else:
        return False
# tests that the BWT of a simple word is correct  
def BWTsimple():
    if burrowsWheelerTransform.Burrows_Wheeler_Transform("AbAsd") == "d$bAsA":
        return True
    else:
        return False

# tests that the BWT of a scentence is correct
def BWTcomplex():
    if burrowsWheelerTransform.Burrows_Wheeler_Transform("This is a long test string") == "ssatgg$ tnnTr h oilt he s s":
        return True
    else:
        return False
    
    
print("Test getSuffixes works when empty string is submitted : ", getSuffixesEmpty())
print("Test getSuffixes works with simple string : ", getSuffixesSimple())
print("Test getSuffixes works with complex string : ", getSuffixesComplex())
print("Test getRotations works with empty string : ", getemptyrotations())
print("Test getRotations works with non empty string : ", getRotationsFullWord())
print("Test Burrows-wheeler works with empty string : ", BWTempty())
print("Test getRotations works with simple string : ", BWTsimple())
print("Test getRotations works with complex string : ", BWTcomplex())
