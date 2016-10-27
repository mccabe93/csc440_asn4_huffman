
letterDic = {}


def code(msg):
    letters = {}
    
    #used to sort list
    def getKey(item):
        return item[0]
    
    tupleList = []

    splitMsg = list(msg)
    
    while len(splitMsg) != 0:
        char = splitMsg[0]
        letters[char] = 'L'
        frequency = splitMsg.count(char)
        #build tuple
        tupleList.append((frequency, 1, char))
        
        #removes all instances of char from splitMsg list
        splitMsg[:] = [item for item in splitMsg if item != char]

    #Sort list by frequency
    sortedTupleList = sorted(tupleList, key=getKey)
    
    while len(sortedTupleList) != 2:
        #get first two in list, sum frequencys, to make new tuple.
        firstTuple = sortedTupleList[0]
        secondTuple = sortedTupleList[1]

        firstTupleFreq = sortedTupleList[0][0]
        secondTupleFreq = sortedTupleList[1][0]

        mySum = firstTupleFreq + secondTupleFreq


        myTuple = (mySum, ((firstTuple[1] + secondTuple[1])), firstTuple, secondTuple)
        
        #remove used tuples from list
        sortedTupleList.remove(firstTuple)
        sortedTupleList.remove(secondTuple)

        #Resort
        for i in range(0, len(sortedTupleList)):
            if myTuple[0] <= sortedTupleList[i][0]:
                sortedTupleList.insert(i, myTuple)
                break
            
            elif i == len(sortedTupleList)-1:
                sortedTupleList.append(myTuple)
                
                                        
                
        sortedTupleList = sorted(sortedTupleList, key=getKey)

    firstHalf = list(sortedTupleList[0])
    
    def getStr(sublist, string, destination, half):
        if (sublist[1] == 1 and sublist[2] == destination):
            letterDic[sublist[2]] = string
        elif len(sublist[2]) < 2:
            return
        else:
            x = 3
            y = 2
            if half == 1:
                x = 2
                y = 3
            getStr(sublist[x], string + "0", destination, half)
            getStr(sublist[y], string + "1", destination, half)
            
    for letter in letters:
        if getStr(sortedTupleList[0], "0", letter, 0) == None:
            getStr(sortedTupleList[1], "1", letter, 1)
    
    msgInCode = "".join(getAsArray(msg))
    return msgInCode
    
aCode = code("MiMiiIlkeeee") 
print(aCode)
invLetterDic = {v: k for k, v in letterDic.iteritems()}
print(invLetterDic)
print(invLetterDic["10"])
check = ('10' in invLetterDic.values())
print(check)

def decode(str, decoderRing):
    string = ""
    codeWord = []

    for i in range(len(str)):
        string = string + str[i]
        if(string in decoderRing.keys()):
            codeWord.append(decoderRing[string])
            string = ""
            
        finalCode = "".join(codeWord)
    return finalCode

def getAsArray(msg):
    msgInCode = []
    for element in msg:
        msgInCode.append(letterDic[element])
    return msgInCode

def compress(string):
    
        
codeWord = decode(aCode,invLetterDic)
print(codeWord)            

    

        

