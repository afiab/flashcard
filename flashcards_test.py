#flashcards_test.py
import flashcards

#code to generate sample text file:
'''
for i in range(9):
    print("This is question "+str(i)+"\nThis is answer "+str(i))
'''

#testing createList()
def test_createList():
    flashcards.createList("exampleTextFile.txt")
    expected = ['This is question 0', 'This is question 1', 'This is question 2', 'This is question 3', 'This is question 4', 'This is question 5', 'This is question 6', 'This is question 7', 'This is question 8']
    actual = flashcards.showQuestionList()
    assert expected == actual, "Actual was this: \n"+str(actual)
    expected = ['This is answer 0', 'This is answer 1', 'This is answer 2', 'This is answer 3', 'This is answer 4', 'This is answer 5', 'This is answer 6', 'This is answer 7', 'This is answer 8'] 
    actual = flashcards.showAnswerList()
    assert expected == actual, "Actual was this: \n"+str(actual)
    
    #make tests for showQuestion and showAnswer later