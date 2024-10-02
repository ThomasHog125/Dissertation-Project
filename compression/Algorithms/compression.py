from . import LyndonFactorisation
from . import burrowsWheelerTransform as BWT
# opens file and returns all text in it 
def getFileText(filename):
    #exception to catch file not found exception
    try:
        f = open("compression/Algorithms/"+filename, "r")
        text = f.read()
        # returns text
        return text
    
    except FileNotFoundError:
        # returns file not found if execption is found
        return "File not found"
        
                
# function that performs run length encoding on text        
def rle(text):
    # A list that will contain characters that turn up in the string in order
    characters=[]
    # A list that contains the frequency of the characters
    # The index of any item in the list will match the character list
    # This means if "A" is at position 0 and 5 is at position 0 
    # A has appeared 5 times in a row 
    frequency =[]
    i = 0
    # This value is to avoid an out of bounds error when searching the string
    limit = len(text)-1
 
    
    while i <= limit:
        # current letter in the string 
        current = text[i]
        # adds current letter to character string 
        characters.append(current)
        charaterCount = 1
        # This loops trough the string until a letter that isnt the current is found
        while i <= limit:
            # if i is equal to the limit then it will have already been counted
            # SO all thta needs to happen is increase i to break out of the loop
            if i == limit:
                 i = i+1
            # if the next letter is equal to the current then count it and increase i
            elif text[i+1]== current:
                charaterCount = charaterCount+ 1
                i = i+1
            # if the next leter is not the same as the current.
            # and if it is not last then it just needs i to be increased 
            else:
                i = i+1
                break   
        # add the number of times the letter has apeared to the string
    
   
        # add the number of times the letter has apeared to the string
        frequency.append(charaterCount)
    # retruns a string in the format 3A2X  if the original string was AAAXX
    return formatRLE(characters,frequency)
    
    
    
# formats the two lists into a string
def formatRLE(characters,frequency):
    compressedText = ""
    # loops thorugh all the characters in the characters list 
    for i in range(0,len(characters)):
        # if there is only one character in the set then only the character is displayed
        if frequency[i]==1:
            compressedText = compressedText + characters[i]
        # otherwise the number of characters ina row and then the character are displayed
        else:
            compressedText = compressedText + (str(frequency[i])+characters[i])
    return compressedText
    
# compresses the text to be smaller in size than before 
# This uses Burrows-Wheeler transform , lyndon factorisation and run length encoding
def compressBurrowsLyndon(text):
    # finds the lyndon factorisation of the text 
    factorisation = LyndonFactorisation.duval(text)
    transformedText=""
    # performs burrows wheeler transform on the lyndon words and adds it to a string
    for i in factorisation:
        transformedText = transformedText + BWT.Burrows_Wheeler_Transform(i)
    
    # retruns the formatted string after it has been run length encoded 
    return rle(transformedText)

# performs lyndon factorisation and run length encoding on text 
def compressLyndon(text):
    # finds the lyndon factorisation of the text 
    factorisation = LyndonFactorisation.duval(text)
    transformedText=""
    # performs burrows wheeler transform on the lyndon words and adds it to a string
    for i in factorisation:
        transformedText = transformedText + rle(i)
    
    # retruns the formatted string after it has been run length encoded 
    return transformedText

# performs run length encoding on text 
def compressRLE(text):
   
    return rle(text)

    
# performs Burrows-Wheeler transform on word and run length encodes it      
def compressBurrows(text):
    transformedText = BWT.Burrows_Wheeler_Transform(text) 
    transformedTextRle= rle(transformedText)
    return transformedTextRle

        
# creates a binary file from compressed text
def createBinaryFile(compressedFilename, compressedText):

    # opens a binary file 
    with open(compressedFilename, 'wb') as file:
        # writes the compressed text to binary file
        file.write(compressedText)
        
# performs all compression techniques          
def compressVariations(filename):
    # recieves text from file
    text = getFileText(filename)
    # compression algorithms that the result to preset files
    createBinaryFile("compression\Algorithms\CompressedRLE.dat",compressRLE(text).encode('utf-8'))
    createBinaryFile("compression\Algorithms\CompressedLyndonFactorisation.dat",compressLyndon(text).encode('utf-8'))
    createBinaryFile("compression\Algorithms\CompressedBurrows.dat",compressBurrows(text).encode('utf-8'))
    createBinaryFile("compression\Algorithms\CompressedFile.dat",compressBurrowsLyndon(text).encode('utf-8'))


    

        