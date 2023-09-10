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