import fileParser as fp
import log_entails as ent
import queue as q

# Importing the lines out of KB.txt
e = fp.ExtractLinesKB()

class Tree:

    #constructor for the tree class
    def __init__(self, expr = None , symbol=None, connective=None, children = None):
        self.symbol = symbol
        self.connective = connective
        self.children = children
        self.expr = expr
        # If an expression is passed. Here an expression is a line of string
        if(expr):
            # splitting the string using spaces
            expr = expr.split(" ")
            if(expr[0]=="and" or expr[0]=="iff" or expr[0]=="if" or expr[0]=="not" or expr[0]=="and" or expr[0]=="or"):
                self.connective = expr[0]
                # parsing the list into string as expr can only be string when passed as a parameter
                # also taking [,] and , off of the string so that the expression will be usable
                # Here, L is list of expressions starting from 2nd element
                # and M is the list of expression starting from 3rd element
                L = str(expr[1:])
                L = str(L)
                L = L.replace("[","")
                L = L.replace("]","")
                L = L.replace(","," ")
                L = L.replace("'" , "")
                self.children=[]

                self.children.append(Tree(expr = L))

                M = str(expr[2:])
                M = str(M)
                M = M.replace("[", "")
                M = M.replace("]", "")
                M = M.replace(",", "")
                M = M.replace("'", "")
                self.children.append(Tree(expr = M))

            #checking if an expression is a symbol by checking if "_" is in the expression "_" is an underscore
            elif("_" in expr[0]):
                self.symbol = expr[0]

        #If children is passed as a parameter, the if block below handles it
        if(children):
            self.children=[]
            for i in children:
                self.children.append(i)



    #the prefix string representaion of the object
    def __str__(self, level=0):
        #here level determines the spacing
        ret = "\t" * level

        if(self.symbol != None):
            ret = ret + repr(self.symbol)
        if (self.connective != None):
            ret = ret + repr(self.connective)
        ret = ret + "\n"
        if self.children != None:
            for child in self.children:
                ret += child.__str__(level + 1)
        return ret

    #A method to print out the Tree class in infix notation
    def Infix_Print(self):
        #this is the base case. the recursion stops when it finds a symbol
        if(self.symbol):
            return str(self.symbol)
        #handling all the connective conditions
        if(self.connective):
            if(self.connective == "not"):
                l=self.children[0].symbol
                string = ""
                string = string + str(self.connective) + "(" + l + ")"
                return string

            if(self.connective == "iff" or self.connective == "if" or self.connective == "or"):
                string = "("
                first = self.children[0].Infix_Print()
                second = self.children[1].Infix_Print()
                string = string + first + " " + str(self.connective)+" " + second+ ")"
                return string

            if(self.connective == "and"):
                #handling connective "and"
                if(len(self.children)==2):
                    left = self.children[0].Infix_Print()
                    right = self.children[1].Infix_Print()
                    string = "("
                    string = string + left + " " + str(self.connective) + " " + right
                    return string

                if(len(self.children)>2):
                    string = ""
                    for child in self.children:
                        string = string + "(" + str(child.Infix_Print()) + ")" + str(self.connective)
                    string = string[:len(string)-3]
                    return string



# a list for holding all the sentences parsed out of KB.txt
KB = []
for i in e:
    b = Tree(i)
    KB.append(b)

# KnowBase is the Knowledge base in Tree structure
KnowBase = Tree(connective="and", children = KB)

#aalphaLInes holds the lines extracted from alpha .txt
alphaLines= fp.ExtractLinesAlpha()


alpha = []
#alpha is the list of sentences
for lines in alphaLines:
    alpha.append(Tree(expr=lines))

print("Printing the Knowledge base and alpha values:::")
print("Knowledge Base in prefix format::")
print(KnowBase)
print("Knowledge Base in infix notation::")
print(KnowBase.Infix_Print())

print("First alpha value in infix notation::")
print(alpha[0].Infix_Print())
print("Second alpha value in infix notation::")
print(alpha[1].Infix_Print())

print("Now, checking if the Knowledge Base entails first alpha value ...  ")
if(ent.TT_Entails(KnowBase, alpha[0])):
    print("Knowledge Base entails first alpha value!")
else:
    print("Knowledge base does not entail first alpha value!")

print()
print("Now, checking if the Knowledge Base entails second alpha value ...  ")
if(ent.TT_Entails(KnowBase, alpha[1])):
    print("Knowledge Base entails second alpha value ")
else:
    print("Knowledge Base does not entail second alpha value")

