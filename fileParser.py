k = open("KB.txt",'r')
a = open("alpha.txt", 'r')
#k contains the lines read out of KB.txt
# a contains the lines read out of alpha.txt

def ExtractLinesKB():
    returnList = []
    #replacing all the parenthesis and break lines with spaces for ease of parsing
    for line in k:
        line = line.replace("(","")
        line = line.replace(")","")
        line = line.replace("\n","")
        returnList.append(line)
    return returnList

def ExtractLinesAlpha():
    returnList = []
    for line in a:
        line = line.replace("(","")
        line = line.replace(")","")
        line = line.replace("\n",'')
        returnList.append(line)
    return returnList

