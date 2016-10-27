from bitarray import bitarray

def getAsArray(msg, tree):
    msgInCode = []
    for key, code in tree.iteritems():
        msgInCode.append(tree[key])
    return msgInCode

def reverseDictionary(dic):
    return {v: k for k, v in dic.iteritems()}
	
# Initialization: We have 'msg', a non-empty plaintext string.	
def code(msg):
    letterDic = {}
    letters = []
    
    #used to sort list
    def getKey(item):
        return item[0]
    
    tupleList = []
 
    splitMsg = list(msg)
    
    while len(splitMsg) != 0:
        char = splitMsg[0]
        letters.append(char)
        frequency = splitMsg.count(char)
        #build tuple
        tupleList.append((frequency, 1, char))
        
        #removes all instances of char from splitMsg list
        splitMsg[:] = [item for item in splitMsg if item != char]

    #Sort list by frequency
    sortedTupleList = sorted(tupleList, key=getKey)
    
    # Maintanence: Every iteration we generate a Huffman code
	
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

    #print sortedTupleList



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

    codedMsg = ""
    print letterDic
    
    for element in msg:
        print letterDic[element]
        codedMsg = codedMsg + letterDic[element]
    
    return codedMsg, (len(codedMsg), letterDic)

def decode(str, decoderRing):
    print decoderRing[1]
    decoder = reverseDictionary(decoderRing[1])
    print decoder
    string = ""
    codeWord = []

    for i in range(len(str)):

        string = string + str[i]
        
        if(string in decoder.keys()):
            codeWord.append(decoder[string])
            string = ""
            
    finalCode = "".join(codeWord)
    return finalCode            


def compress(msg, tree):
    dic = tree
    print "coded str len =", code(msg)[0], "\ncoded dict =", dic
    huffMsg = getAsArray(msg, reverseDictionary(dic))
    print "huffmsg = ", huffMsg
    a = bitarray()
    
    for b in msg:
        a.append(bool(b))

    print(a)


codeWord = "secretMsg"
msg, tree = code(codeWord)
compress(msg, tree[0])
#codeMsg, decoder = code(codeWord)
#print(codeMsg)

#myMsg= decode(codeMsg, decoder)

#print(myMsg)

#compress(codeMsg,decoder)
