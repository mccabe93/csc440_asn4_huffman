from bitarray import bitarray

def getReverseDictionary(dic):
    return {v: k for k, v in dic.iteritems()}

def getHuffmanTree(frequencyList, msg):
    #used to sort list
    def getKey(item):
        return item[0]
    
    #Sort list by frequency
    sortedTupleList = sorted(frequencyList, key=getKey)
    
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
                
    return sortedTupleList

# Initialization: We have 'msg', a non-empty plaintext string.	
def code(msg):
    letterDic = {}
    tupleList = []
    letters = []

    splitMsg = list(msg)
    
    while len(splitMsg) != 0:
        char = splitMsg[0]
        letters.append(char)
        frequency = splitMsg.count(char)
        #build tuple
        tupleList.append((frequency, 1, char))
        
        #removes all instances of char from splitMsg list
        splitMsg[:] = [item for item in splitMsg if item != char]

    sortedTupleList = getHuffmanTree(tupleList, msg)

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
        #print letterDic[element]
        codedMsg = codedMsg + letterDic[element]
    
    return codedMsg, (len(codedMsg), letterDic)

def decode(str, decoderRing):
    print decoderRing[1]
    decoder = getReverseDictionary(decoderRing[1])
    #print decoder
    string = ""
    codeWord = []

    for i in range(len(str)):

        string = string + str[i]
        
        if(string in decoder.keys()):
            codeWord.append(decoder[string])
            string = ""
            
    finalCode = "".join(codeWord)
    return finalCode            


def compress(msg):
    msg, tree = code(msg)
    a = bitarray()
    for b in msg:
        a.append(bool(int(b)))
    return (a.tobytes(), tree)

def decompress(msg, tree):
    b = bitarray()
    b.frombytes(msg)
    bitsAsString = ""
    for bit in range(0, tree[0]):
        bitsAsString += str(int(b[bit]))
    return decode(bitsAsString, tree)

codeWord = "secretMsg"#"the quick brown frog jumped over the lazy fox"
print "codeword len =", len(codeWord)
msg, tree = compress(codeWord)
print msg, tree
print(decompress(msg, tree))
