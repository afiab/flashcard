"""
Mini Flash Card GUI
Parse text file for front/back of cards
creates a display with text
"""

#Global Variables:
GLOBAL_2DLIST_QNA = [] #FORMAT: [[Q 1,A 1],...,[Q N+1,A N+1]]

#Functions:
def createList(filename):
    """parse txt file contents into GLOBAL_2DLIST_QNA"""
    isQuestion = True
    with open(filename) as contents: 
        for line in contents:
            if isQuestion:
                '''if this is a question, 
                add a space for the q+a in GLOBAL_2DLIST_QNA
                with the question filled in'''
                GLOBAL_2DLIST_QNA.append([line,""])
            else:
                '''if this is an answer,
                replace the space from the question with the answer'''
                GLOBAL_2DLIST_QNA[len(GLOBAL_2DLIST_QNA)-1][1]=line
            isQuestion = not isQuestion

def showList():
    """accessor method for GLOBAL_2DLIST_QNA"""
    return GLOBAL_2DLIST_QNA

def showQuestion(qNum):
    """accessor method for specified question numbered qNum"""
    return GLOBAL_2DLIST_QNA[int(qNum-1)][0]

def showAnswer(aNum):
    """accessor method for specified answer numbered aNum"""
    return GLOBAL_2DLIST_QNA[int(aNum-1)][1]

#main
def main():
    createList("exampleTextFile.txt")
    print(showList())

if __name__ == "__main__":
    main()