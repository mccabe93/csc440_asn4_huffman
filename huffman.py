import os
import sys
import marshal
import array
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
	
    while len(sortedTupleList) != 1:
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
        if len(sortedTupleList) == 0:
            sortedTupleList.append(myTuple)
            break
        
        #Resort
        for i in range(0, len(sortedTupleList)):
            if myTuple[0] <= sortedTupleList[i][0]:
                sortedTupleList.insert(i, myTuple)
                break
            
            elif i == len(sortedTupleList)-1:
                sortedTupleList.append(myTuple)
                
    return sortedTupleList

try:
    import cPickle as pickle
except:
    import pickle

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
    
    def getStr(sublist, string, destination):
        if (sublist[1] == 1 and sublist[2] == destination):
            letterDic[sublist[2]] = string
        elif len(sublist[2]) < 2:
            return
        else:
            getStr(sublist[2], string + "0", destination)
            getStr(sublist[3], string + "1", destination)
            
    for letter in letters:
        getStr(sortedTupleList[0], "", letter)

    codedMsg = ""
    
    for element in msg:
        codedMsg = codedMsg + letterDic[element]
    
    return codedMsg, (len(codedMsg), letterDic)

def decode(str, decoderRing):
    decoder = getReverseDictionary(decoderRing[1])
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

def decompress(msg, decoderRing):
    b = bitarray()
    b.frombytes(msg)
    bitsAsString = ""
    for bit in range(0, tree[0]):
        bitsAsString += str(int(b[bit]))
    return decode(bitsAsString, tree)

def usage():
    sys.stderr.write("Usage: {} [-c|-d|-v|-w] infile outfile\n".format(sys.argv[0]))
    exit(1)

if __name__=='__main__':
    if len(sys.argv) != 4:
        usage()
    opt = sys.argv[1]
    compressing = False
    decompressing = False
    encoding = False
    decoding = False
    if opt == "-c":
        compressing = True
    elif opt == "-d":
        decompressing = True
    elif opt == "-v":
        encoding = True
    elif opt == "-w":
        decoding = True
    else:
        usage()

    infile = sys.argv[2]
    outfile = sys.argv[3]
    assert os.path.exists(infile)

    if compressing or encoding:
        fp = open(infile, 'rb')
        str = fp.read()
        fp.close()
        if compressing:
            msg, tree = compress(str)
            fcompressed = open(outfile, 'wb')
            marshal.dump((pickle.dumps(tree), msg), fcompressed)
            fcompressed.close()
        else:
            msg, tree = code(str)
            print(msg)
            fcompressed = open(outfile, 'wb')
            marshal.dump((pickle.dumps(tree), msg), fcompressed)
            fcompressed.close()
    else:
        fp = open(infile, 'rb')
        pickled_tree, msg = marshal.load(fp)
        tree = pickle.loads(pickled_tree)
        fp.close()
        if decompressing:
            str = decompress(msg, tree)
        else:
            str = decode(msg, tree)
            print(str)
        fp = open(outfile, 'wb')
        fp.write(str)
        fp.close()
