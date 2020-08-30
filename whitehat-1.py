##def countwords():
##    var = input("Enter the file name:\n")
##    numberofwords = 0
##    file = open(var,'r')
##    for line in file:
##        words = line.split()
##        numberofwords = numberofwords + len(words)
##    print("number of words:")
##    print(numberofwords)
##countwords()

def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")
    file1data = open(file1,'r+')
    file2Data = open(file2,'r+')
    for line in file2Data:
        words = line.split()
        savedData = words
    for line in file1data:
        words = line.split()
        file1 = file1 + savedData
    print(file1)
    print(file2)
swapFileData()
        
    
