from . import suffixTree

# recursive function that finds all the suffixes of the word
def getSuffixes(node,currentSuffix,suffixes):
    # adds part of the suffix to a temporary string
    currentSuffix = currentSuffix + node.suffix
    # if the node has no children then whole suffix has been found 
    if node.hasChildren()==False:
        # add suffix to list
        suffixes.append(currentSuffix)
    else:
        # if node has children the suffix isnt complete
        for i in node.getChildren():
            # recursivley calls function to find the rest of the suffix
            getSuffixes(i,currentSuffix,suffixes)
    return suffixes
    
# finds all the rotations of the string
def getRoatations (text):
    # creates suffix tree of word 
    root = suffixTree.createTree(text)
    # finds all the suffixes 
    suffixes = getSuffixes(root,"",[])
    
    roatations = []
    # adds $ to the string as the suffix tree requires it 
    text = text+"$"
    length= len(text)
    for i in suffixes:
        # finds length of suffix then adds the part of the string not included in the suffix
        # It adds this to the suffix to rotate the string
        roatations.append(i+text[:length -len(i)])
   
    return roatations
    
def Burrows_Wheeler_Transform(text):
    # gets all the rotations
    rotations = getRoatations(text)
    # sorts the list from lexicographically smallest to largest
    sortedRotations = sorted(rotations)
    transformedWord = ""
    length = len(text)
    for i in sortedRotations:
        # adds final character of each word in sorted list to the transfomred string
        transformedWord = transformedWord + i[length]
    
    return transformedWord



