from .import compression

######################Tests for the function getFileText ##########

# Test to check that valid file is being opened
def ExisitingFile():
        f = compression.getFileText("Algorithms/testFile.txt")
        if f == "File not found":
            return False
        else:
            return True
# Test to check that filenotfound exception is thrown
def invalidFile():
        f = compression.getFileText("Algorithms/invalid.txt")
        if f == "File not found":
            return True
        else:
            return False

# Test to check if correct text is being returned 
def getFileText():
    f = compression.getFileText("Algorithms/testFile.txt")
    if f == "aaaTestaa":
        return True
    else:
        return False

# this tests that the algorithms encodes correctly
def encodingTest():
    compressedText = compression.rle("TTEESSSSSSTTTT")
    if compressedText == "2T2E6S4T":
        return True
    else: return False
    
# tests that the format rle function works correctly when empty
def testformatRLEempty():
    if compression.formatRLE([],[]) == "":
        return True
    return False 
 
   
def testformatRLEword():
    # should return string with a number representing how many consecutive charcters there are
    # and then the character
    if compression.formatRLE(["T","E","S","T","a"],[2,3,4,5,1]) == "2T3E4S5Ta":
        return True
    return False 
    




print("Existing File when reading :",ExisitingFile()) 
print("Exception is caught when given invalid file :",invalidFile()) 
print("File Text is recieved :",getFileText()) 
print("Run length encoding works with valid input :",encodingTest())
print("Test format RLE with empty string :", testformatRLEempty())
print("Test format RLE with multiple characters:", testformatRLEword())


