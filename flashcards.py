"""
Mini Flash Card GUI
Parse text file for front/back of cards
creates a display with text
"""
from tkinter import *

#Global Variables:
GLOBAL_QUESTIONS_LIST = [] #Format: [q1, ..., qn]
GLOBAL_ANSWERS_LIST = [] #Format: [a1, ..., an]
GLOBAL_CURRENT_INDEX = 0 #the current question

#Functions:
def createList(filename):
    """parse txt file contents into respective lists"""
    isQuestion = True
    with open(filename) as contents: 
        for line in contents:
            if isQuestion:
                '''if this is a question, 
                add the question to the list of questions'''
                GLOBAL_QUESTIONS_LIST.append(line)
            else:
                '''if this is an answer,
                add the answer to the list of answers'''
                GLOBAL_ANSWERS_LIST.append(line)
            isQuestion = not isQuestion

def showQuestionList():
    """accessor method for GLOBAL_QUESTIONS_LIST"""
    return GLOBAL_QUESTIONS_LIST

def showAnswerList():
    """accessor method for GLOBAL_ANSWERS_LIST"""
    return GLOBAL_ANSWERS_LIST

def showQuestion(qNum=GLOBAL_CURRENT_INDEX):
    """accessor method for specified question numbered qNum"""
    if qNum>len(GLOBAL_QUESTIONS_LIST) or qNum<0:
        return showQuestion(0)
    return GLOBAL_QUESTIONS_LIST[int(qNum-1)][0]

def showAnswer(aNum=GLOBAL_CURRENT_INDEX):
    """accessor method for specified answer numbered aNum"""
    if aNum>len(GLOBAL_ANSWERS_LIST)or aNum<0:
        return showAnswer(0)
    return GLOBAL_ANSWERS_LIST[int(aNum-1)][1]

root = Tk()
root.geometry("400x400")

content = Frame(root)
words = Label(content)
words['text']= 'placeholder'#showQuestion()
words.pack(side=TOP)

action = Frame(root)
switch = Button(action)
switch['text'] = 'flip'
#switch['command'] = #funct that changes text

content.pack(side=TOP, expand=YES, fill=BOTH)
action.pack(side=TOP, expand=YES, fill=BOTH)

root.mainloop()

#main
"""#commented out for testing:
def main():
    createList("exampleTextFile.txt")
    print(showQuestionList())
    print(showAnswerList())

if __name__ == "__main__":
    main()
"""