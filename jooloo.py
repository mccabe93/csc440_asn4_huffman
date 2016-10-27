
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

#    print(tupleList)
#    for element in tupleList:
#        print(len(element))

    #Sort list by frequency
    sortedTupleList = sorted(tupleList, key=getKey)
    
    while len(sortedTupleList) != 2:
        #print(sortedTupleList)
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

        #add combined tuples
        #sortedTupleList.append(myTuple)

        #Resort
        for i in range(0, len(sortedTupleList)):
            if myTuple[0] <= sortedTupleList[i][0]:
                sortedTupleList.insert(i, myTuple)
                break
            
            elif i == len(sortedTupleList)-1:
                sortedTupleList.append(myTuple)
                
                                        
                
        sortedTupleList = sorted(sortedTupleList, key=getKey)
        #print(sortedTupleList)
#    for i in range(0, len(sortedTupleList)):
#        sortedTupleList[i] = tuple(list(sortedTupleList[i]).insert(1, len(sortedTupleList[i])))
    print sortedTupleList

#    currentTuple = sortedTupleList[0]

##    for i in range(0, len(sortedTupleList[0])):
##        
##        print "Current Tuple:", currentTuple

##    oldFirst = sortedTupleList[0][2]
##    print(oldFirst)
##    sortedTupleList[0][2] = sortedTupleList[0][3]
##    sortedTupleList[0][3] = oldFirst

    #MC

    firstHalf = list(sortedTupleList[0])
    #print("Here")
    #print(firstHalf)
    
    def getStr(sublist, string, destination, half):
        #print sublist
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


    print(letterDic)

code("Mike")
invLetterDic = {v: k for k, v in letterDic.iteritems()}

check = ('10' in invLetterDic.values())



##print("!!!!!!")
##print(invLetterDic)

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
        

        
codeWord = decode("10110100",invLetterDic)
print(codeWord)            

        


