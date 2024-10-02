 
def match(str1, str2):
    i = 0 
    # checks for letters that are the same in the string (prefix)
    while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
        i += 1  # increase i when there is a match

    # Returns the part of the string that matches
    return str1[:i]    


# a class for the nodes of the suffix tree
class suffixTreeNode:
    def __init__(self,children,startPosition,endPosition,suffix):
        # a list that will contain ither nodes 
        self.children = children
        # The index of the beginning of the suffix 
        self.startPosition = startPosition
        # The index of the end of the suffix 
        self.endPosition = endPosition
        self.suffix = suffix
        
    # appends a new node to the list of children
    def addChild(self,child):
        self.children.append(child)   
    
    # gets the list of children and returns it
    def getChildren(self):
        return self.children 
    
    # checks whether the node has any child nodes
    def hasChildren(self):
        if len(self.children) == 0:
            return False
        else:
            return True
        

# function that will start the creation of the suffix tree
def createTree(text):
    # adds $ as a pointer to the end of the string 
    text = text + "$"
    # root node is created
    # the root node of a suffix tree has no suffix 
    root  = suffixTreeNode([],None,None,"")
    # loops through length of sting
    for i in range(1,len(text)+1):  
        # this returns i letters from the end of the sting  
        suffix = text[-i:]
        startpoint = len(text)-i
        # adds suffix to tree
        addSuffix(suffix,root,startpoint,len(text)-1,text)
    return root
    

# function to add suffix to tree
def addSuffix(suffix,node,startPoint,originalLength,originalText):
    #checks if the root node is empty 
    if node.hasChildren() == False and node.suffix == "":
        node.addChild(suffixTreeNode([],startPoint,originalLength,suffix))
    else:
        # boolean value to determine whether a new bracnh is to be made 
        createBranch = True
        #loops through chilfren of node 
        for i in node.getChildren():
            # Checks whether a suffix needs to be added to the current node
            if len(match(suffix,originalText[i.startPosition:i.endPosition+1]))==len(originalText[i.startPosition:i.endPosition+1]):
                i.addChild(suffixTreeNode([],startPoint+len(originalText[i.startPosition:i.endPosition+1]),originalLength,originalText[startPoint+len(originalText[i.startPosition:i.endPosition+1]):originalLength+1]))
                createBranch = False
            else:
                # checks if any of the branches contain any matching prefixes of the suffixes 
                if len(match(suffix,originalText[i.startPosition:i.endPosition+1]))>0:
                    createBranch = False
                    prefix = match(suffix,originalText[i.startPosition:i.endPosition+1])
                
                    # this splits the suffix if there are no children
                    if i.hasChildren() == False:
                        # splits the current suffix
                        i.addChild(suffixTreeNode([],i.startPosition+len(prefix),originalLength,originalText[i.startPosition+len(prefix):i.endPosition+1]))
                        #splits the suffix passed into function
                        i.addChild(suffixTreeNode([],startPoint+len(prefix),originalLength,originalText[startPoint+len(prefix):originalLength+1]))
                        #changes the current suffixes end position to change the suffix of the branch
                        i.endPosition = (len(prefix)+i.startPosition)-1
                        #changes the text suffix in the class accordingly 
                        i.suffix = originalText[i.startPosition:i.endPosition+1]
                    else:
                        # recursive function to loop tthrough any more branches
                        addSuffix(originalText[startPoint+len(prefix):originalLength],i,startPoint+len(prefix),originalLength,originalText)
                    
        # creates new branch if there are no matching prefixes of suffixes in the tree
        if createBranch == True:
            node.addChild(suffixTreeNode([],startPoint,originalLength,suffix))
       