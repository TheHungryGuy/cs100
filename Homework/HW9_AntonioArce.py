'''
Antonio Arce
CS100 Section 031
HW 08 November 01,2022
'''

#problem 1
def file_copy(in_file,out_file):
    #open 1st file to read thru 
    copyFrom = open(in_file,"r")
    lines = copyFrom.readlines()
    #write each line to outFile
    copyTo = open(out_file,"w")
    for line in lines:
        copyTo.write(line)
        #copyTo.write("\n")

#test
file_copy('created_equal.txt', 'copy.txt')
copy_f = open('copy.txt')
copy_f.read()

#problem 2
def file_stats(in_file):
    inputFile = open(in_file,"r")
    lines = inputFile.readlines()
    numLines = len(lines)
    numWords = 0
    numChars = 0
    for line in lines:
        numWords += len(line.split())
        numChars += len(line)
    return print(f"Lines {numLines}\nWords {numWords} \nCharacters {numChars}")
                
#test 
file_stats('created_equal.txt')    

#problem 3
import string
def repeat_words(in_file,out_file):
    inputFile = open(in_file,"r")
    outputfile = open(out_file,"w")
    lines = inputFile.readlines()
    for line in lines:
        seenWords = []
        outputText = []
        for word in line.strip(string.punctuation).split():
            lowWord = word.strip(string.punctuation).lower()
            if lowWord not in seenWords:
                seenWords.append(lowWord)
                continue;
            if lowWord not in outputText:
                outputText.append(lowWord)
                outputfile.write(lowWord+" ")
        outputfile.write('\n')        
         
#test
inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
            
    