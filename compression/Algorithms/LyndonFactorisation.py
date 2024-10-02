# finds all the lyndon words in the text
def duval(Text):
    StringLength = len(Text)
    i = 0
    lyndonWords = []

    while i < StringLength:
        RightPointer = i + 1
        leftPointer = i

        while RightPointer < StringLength and Text[leftPointer] <= Text[RightPointer]:
            # new possible lyndon word set to start at i 
            # done when the lyndon word is complete.
            if Text[leftPointer] < Text[RightPointer]:
                leftPointer = i
            else:
                # increment the left pointeras lyndon word has not been found 
                leftPointer += 1
            # right pointer increased
            RightPointer += 1

        # if i <= to the left pointer means there is a lyndon word so its added to the list
        while i <= leftPointer:
            lyndonWords.append(Text[i:i + RightPointer - leftPointer])
            i += RightPointer - leftPointer

    return lyndonWords
