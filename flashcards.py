"""
Mini Flash Card GUI
Parse text file for front/back of cards
creates a display with text
"""
from tkinter import *

global GLOBAL_QUESTIONS_LIST,GLOBAL_ANSWERS_LIST,GLOBAL_CURRENT_INDEX,GLOBAL_CURRENT_SIDE
GLOBAL_QUESTIONS_LIST = [] #Format: [q1, ..., qn]
GLOBAL_ANSWERS_LIST = [] #Format: [a1, ..., an]
GLOBAL_CURRENT_INDEX = 0 #the current question
GLOBAL_CURRENT_SIDE = True #True=question, False=answer

#Functions:
def createList(filename):
    """parse txt file contents into respective lists"""
    isQuestion = True
    with open(filename) as contents: 
        for line in contents:
            line = line.strip()
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
    return GLOBAL_QUESTIONS_LIST[int(qNum)]

def showAnswer(aNum=GLOBAL_CURRENT_INDEX):
    """accessor method for specified answer numbered aNum"""
    if aNum>len(GLOBAL_ANSWERS_LIST)or aNum<0:
        return showAnswer(0)
    return GLOBAL_ANSWERS_LIST[int(aNum)]

#tkinter functions
def flip():
    """This function flips the card, and updates GLOBAL_CURRENT_SIDE"""
    global GLOBAL_CURRENT_SIDE
    if GLOBAL_CURRENT_SIDE:
        words['text']=showQuestion()
    else:
        words['text']=showAnswer()
    GLOBAL_CURRENT_SIDE = not GLOBAL_CURRENT_SIDE

def record_file():
    """This function sets up everything after getting the filename"""
    #Global Variables:
    global GLOBAL_QUESTIONS_LIST
    global GLOBAL_ANSWERS_LIST
    global GLOBAL_CURRENT_INDEX
    global GLOBAL_CURRENT_SIDE
    GLOBAL_QUESTIONS_LIST = [] #Format: [q1, ..., qn]
    GLOBAL_ANSWERS_LIST = [] #Format: [a1, ..., an]
    GLOBAL_CURRENT_INDEX = 0 #the current question
    GLOBAL_CURRENT_SIDE = True #True=question, False=answer
    global GLOBAL_FILE_NAME
    GLOBAL_FILE_NAME = response.get()
    createList(GLOBAL_FILE_NAME)
    flip()

root = Tk()
root.geometry("400x200")#minimum window size

#getFile is section where user enters a file name
getFile = Frame(root)
#prompt asks user for file
prompt = Label(getFile, text="Input a file name: ")
prompt.pack(side=LEFT,anchor=N)
#response is where the user types the name
response = Entry(getFile, width=40, bd =5)
response.pack(side=LEFT,anchor=N)
enter = Button(getFile, text="Enter", command=record_file)
enter.pack(side=RIGHT,anchor=N)

#content would be the section with the text for the cards
content = Frame(root)
words = Label(content)
words['text']= "Type a file name above to get started"#showQuestion()
words.pack(side=TOP)

#action is the section with button to flip the card
action = Frame(root)
switch = Button(action)
switch['text'] = 'flip'
switch['command'] = flip#funct that changes text
switch.pack(side=TOP)

#maybe another section here for 
#buttons to go to next/prev card

#determines where the sections are located
getFile.pack(side=TOP, expand=YES, fill=BOTH)
content.pack(side=TOP, expand=YES, fill=BOTH)
action.pack(side=TOP, expand=YES, fill=BOTH)

root.mainloop()