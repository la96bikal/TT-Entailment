#This function extracts all the symbols out of a given sentence
def Extract_Symbols(sentence):
    result = []
    if(sentence.symbol != None):
        result.append(sentence.symbol)
    else:
        if(sentence.children != None):
            for child in sentence.children:
                result.extend(Extract_Symbols(child))
    return result

#this function checks whether a sentence is true or false
def PL_True(sentence, model):
    if (sentence.symbol != None):
        return model[sentence.symbol]

    elif sentence.connective == "and":
        for child in sentence.children:
            if(PL_True(child, model) == False):
                return False
        return True

    elif sentence.connective == "or":
        for child in sentence.children:
            if(PL_True(child, model) == True):
                return True
        return False

    elif sentence.connective == "if":
        left = sentence.children[0]
        right = sentence.children[1]
        if(PL_True(left,model) == True) and (PL_True(right, model) == False):
            return False
        else:
            return True

    elif sentence.connective == "iff":
        left = sentence.children[0]
        right = sentence.children[1]
        if (PL_True(left,model) == True and PL_True(right,model)==True) or (PL_True(left,model) == False and PL_True(right,model)==False):
            return True
        else:
            return False

    elif sentence.connective == "not":
        child = sentence.children[0]
        return not(PL_True(child,model))

#This is the function that actually does the enumeration and goes
# through all the rows in the truth table
def TT_Check_All(KB, alpha, symbols, model):
    if (len(symbols)==0):
        if PL_True(KB,model):
            return PL_True(alpha,model)
        else:
            return True

    else:
        first = symbols[0]
        remaining = symbols[1:]
        return TT_Check_All(KB, alpha, remaining, Expand(first, True, model)) and TT_Check_All(KB, alpha, remaining, Expand(first, False, model))

def Expand(symbol, bool, model):
    model[symbol] = bool
    return model

# this is the TT entailer
def TT_Entails(KB, alpha):
    KBSymbols = Extract_Symbols(KB)
    alphaSymbols = Extract_Symbols(alpha)
    symbols = list(set(KBSymbols + alphaSymbols))
    model = {}
    return TT_Check_All(KB, alpha, symbols, model)

