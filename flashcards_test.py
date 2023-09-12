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
    expected = ['This is question 0\n', 'This is question 1\n', 'This is question 2\n', 'This is question 3\n', 'This is question 4\n', 'This is question 5\n', 'This is question 6\n', 'This is question 7\n', 'This is question 8\n']
    actual = flashcards.showQuestionList()
    assert expected == actual, "Actual was this: \n"+str(actual)
    expected = ['This is answer 0\n', 'This is answer 1\n', 'This is answer 2\n', 'This is answer 3\n', 'This is answer 4\n', 'This is answer 5\n', 'This is answer 6\n', 'This is answer 7\n', 'This is answer 8']
    actual = flashcards.showAnswerList()
    assert expected == actual, "Actual was this: \n"+str(actual)
    
    #make tests for showQuestion and showAnswer later