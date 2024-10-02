import suffixTree
# tests that the whole word is returned when two words that are the same 
def testMatchSameWord():
    if suffixTree.match("Test","Test") == "Test":
        return True
    else:
        return False
# tests that  a word matched with another with some f the same letters returns the matching prefix 
def testMatchWithPrefix():
    if suffixTree.match("Test","Te") == "Te":
            return True
    else:
        return False
# tests that two completley different words returns no match
def testMatchNoPrefix():
    if suffixTree.match("Test","G") == "":
            return True
    else:
        return False
############ running matching tests #############################
print("Same word :",testMatchSameWord())
print("Word with prefix :",testMatchWithPrefix())
print("Word without prefix :",testMatchNoPrefix())
################################################################

# function that goes through the suffix tree and adds each suffix to an array for testing
def suffixarray(root):
    array = []
    for i in root.getChildren():
        array.append(i.suffix)
        suffixarray(i)
        
# tests that the suffix tree correctly sperates a word into its suffixes
def testCreateSuffixTreeWithWord():
    array=suffixarray(suffixTree.createTree("AAGTC"))
    if array == ["$","c$","TC$","A","GTC$","AGTC$"]:
        return True
    else:
        return False
    
# tests that when an empty word is inputted only $ is in the suffix tree 
def testcreateSuffixTreeNoword():
    array=suffixarray(suffixTree.createTree(""))
    if array == ["$"]:
        return True
    else:
        return False
################## running suffix tree tests ##############
print("suffix Tree with word : ",testCreateSuffixTreeWithWord())
print("suffix Tree without word :",testMatchWithPrefix())
############################################################