#===============================================================================
# this code test writing and reading from the file
# read the contents of the file, strips all punctuation marks and special characters 
# from the words
# returns a sorted list of unique words from the file 
#===============================================================================


def readfile(filename):
    f = open(filename, "r")
    f1 = f.readlines()
    for line in f1:
        print(line, end='')
    f.close()


#===============================================================================
#  read the text string and return the list of its unique words sorted by alphabet  
#===============================================================================
def getListOfWords(filename):
    f = open(filename, "r")
    listOfWords = []
    f1 = f.readlines()
    count = 0
    for line in f1:
        count = count + 1
        #------------------------------------------------ print("line #", count)
        lineWords = line.split()
        
        for w in lineWords:
            w = w.strip(' .,;:!?1234567890-=~@#$%^&*()_+/\"\'\\\|{}[]`<>\t\u20AA\u00A9\u201D\u00BB\u05BE')
            if not w in listOfWords and w != '':
                listOfWords.append(w)
        
    listOfWords.sort()  
    f.close() 
    return listOfWords


#===============================================================================
#  generate file with word labels
#===============================================================================
def generateFileWithWords(ofilename, words):
    of = open(ofilename, 'w')
    label = 0
    for word in words:
        of.write(str(label))
        of.write(" ")
        of.write(word)
        of.write("\n")
        label = label + 1
    of.close() 


#===============================================================================
# MAIN FUNCTION
#===============================================================================
def main():
    ifilename = "ShnatHaAtalef_test.txt"
    
    words = getListOfWords(ifilename)
    ofilename = "words_and_labels.txt"
    generateFileWithWords(ofilename, words)    
    print("the number of different words is ", len(words))


#------------------------------------------------------------------------------ 
if __name__ == "__main__": 
    main()
