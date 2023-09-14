"""
Mini Flash Card GUI
Parse text file for front/back of cards
creates a display with text
"""
from tkinter import *

#Functions:
def createList(filename):
    """parse txt file contents into respective lists"""
    global GLOBAL_QUESTIONS_LIST, GLOBAL_ANSWERS_LIST, GLOBAL_CURRENT_SIDE, GLOBAL_CURRENT_INDEX
    GLOBAL_QUESTIONS_LIST = [] #Format: [q1, ..., qn]
    GLOBAL_ANSWERS_LIST = [] #Format: [a1, ..., an]
    GLOBAL_CURRENT_SIDE = True #True=question, False=answer
    GLOBAL_CURRENT_INDEX = 0
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
    if not isQuestion: #edge case odd number of lines
        GLOBAL_ANSWERS_LIST.append("?")
    if len(GLOBAL_QUESTIONS_LIST) <= 0: #if the file was empty
        GLOBAL_QUESTIONS_LIST.append("This file was empty. Please try a different file.")
        GLOBAL_ANSWERS_LIST.append("This file was empty. Please try a different file.")

def showQuestionList():
    """accessor method for GLOBAL_QUESTIONS_LIST"""
    global GLOBAL_QUESTIONS_LIST
    return GLOBAL_QUESTIONS_LIST

def showAnswerList():
    """accessor method for GLOBAL_ANSWERS_LIST"""
    global GLOBAL_ANSWERS_LIST
    return GLOBAL_ANSWERS_LIST

def showQuestion(qNum):
    """accessor method for specified question numbered qNum"""
    global GLOBAL_QUESTIONS_LIST
    words['text']='\n'+GLOBAL_QUESTIONS_LIST[int(qNum)]

def showAnswer(aNum):
    """accessor method for specified answer numbered aNum"""
    global GLOBAL_ANSWERS_LIST        
    words['text']='\n'+GLOBAL_ANSWERS_LIST[int(aNum)]

#tkinter functions
def flip():
    """This function flips the card, and updates GLOBAL_CURRENT_SIDE"""
    global GLOBAL_CURRENT_SIDE, GLOBAL_CURRENT_INDEX
    if GLOBAL_CURRENT_SIDE:
        showQuestion(GLOBAL_CURRENT_INDEX)
    else:
        showAnswer(GLOBAL_CURRENT_INDEX)
    GLOBAL_CURRENT_SIDE = not GLOBAL_CURRENT_SIDE

def record_file():
    """This function sets up everything after getting the filename"""
    global GLOBAL_FILE_NAME, GLOBAL_CURRENT_INDEX, GLOBAL_QUESTIONS_LIST
    GLOBAL_FILE_NAME = response.get()
    createList(GLOBAL_FILE_NAME)
    currentCard['text'] = "Card {0}/{1}".format(GLOBAL_CURRENT_INDEX+1,len(GLOBAL_QUESTIONS_LIST))
    flip()

def go_Back():
    """This function goes to the previous card"""
    global GLOBAL_CURRENT_INDEX, GLOBAL_CURRENT_SIDE
    if GLOBAL_CURRENT_INDEX==0:
        GLOBAL_CURRENT_INDEX=len(GLOBAL_QUESTIONS_LIST)-1
    else:
        GLOBAL_CURRENT_INDEX-=1
    currentCard['text'] = "Card {0}/{1}".format(GLOBAL_CURRENT_INDEX+1,len(GLOBAL_QUESTIONS_LIST))
    GLOBAL_CURRENT_SIDE = False
    showQuestion(GLOBAL_CURRENT_INDEX)

def go_Next():
    """This function goes to the next card"""
    global GLOBAL_CURRENT_INDEX, GLOBAL_CURRENT_SIDE
    if GLOBAL_CURRENT_INDEX==len(GLOBAL_QUESTIONS_LIST)-1:
        GLOBAL_CURRENT_INDEX=0
    else:
        GLOBAL_CURRENT_INDEX+=1
    currentCard['text'] = "Card {0}/{1}".format(GLOBAL_CURRENT_INDEX+1,len(GLOBAL_QUESTIONS_LIST))
    GLOBAL_CURRENT_SIDE = False
    showQuestion(GLOBAL_CURRENT_INDEX)

root = Tk()
root.geometry("450x150")#minimum window size

backgroundColor = '#FFFFEA'
buttonColor = '#CFBFF7'

#getFile is section where user enters a file name
getFile = Frame(root, bg=backgroundColor)
#prompt asks user for file
prompt = Label(getFile, text="Input a file name ", bg=backgroundColor, font=('Lucida Sans',12))
prompt.pack(side=LEFT,anchor=N)
#response is where the user types the name
response = Entry(getFile, width=40, bd =5)
response.pack(side=LEFT,anchor=N)
enter = Button(getFile, text="Enter", bg=buttonColor, font=('MS UI Gothic',12), command=record_file)
enter.pack(side=RIGHT,anchor=N)

#content would be the section with the text for the cards
content = Frame(root, bg=backgroundColor)
words = Label(content, text="\nType a file name above to get started", bg=backgroundColor, font=('Lucida Sans',12))
words.pack(side=TOP)

#action is the section with button to flip the card
action = Frame(root, bg=backgroundColor)
switch = Button(action, text="FLIP", bg=buttonColor, font=('MS UI Gothic',12), command=flip)
switch.pack(side=BOTTOM)

#track is section with general stats and prev/next button
track = Frame(root, bg=backgroundColor)
currentCard = Label(track, text="Card -/-", bg=buttonColor, font=('Lucida Sans',12))
currentCard.pack(side=LEFT, anchor=S)
goNext = Button(track, text=">", bg=buttonColor, font=('MS UI Gothic',12), command=go_Next)
goNext.pack(side=RIGHT,anchor=S)
goBack = Button(track, text="<", bg=buttonColor, font=('MS UI Gothic',12), command=go_Back)
goBack.pack(side=RIGHT,anchor=S)

#determines where the sections are located
getFile.pack(side=TOP, expand=YES, fill=BOTH)
content.pack(side=TOP, expand=YES, fill=BOTH)
action.pack(side=TOP, expand=YES, fill=BOTH)
track.pack(side=BOTTOM,expand=YES,fill=BOTH)

root.mainloop()