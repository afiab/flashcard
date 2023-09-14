# flashcard
I decided to make this because the flashcard sites I was previously using started capitalizing on their users. 

## How it Works:
Clone this repository (https://github.com/afiab/flashcard/tree/main) and open up a terminal. 

For your flashcards, have a plain text file (file should end with `.txt`) and have each question and answer on a new line. This file should be saved in the same folder as this repository. There is a file in this repository for reference on formatting called `exampleTextFile.txt`. 

Once in the terminal, type ```python3 flashcards.py``` to run the program. (This assumes you previously installed Python version 3 or higher)

Once the window opens up, it should look like this:

<img width="339" alt="A window that says 'Input a file name' with an entry box and an enter button at the top. Towards the middle, it tells a user to type a file name to get started, and has a flip button under. The bottom left corner shows the current card number, and the bottom right has forward and backward buttons." src="https://github.com/afiab/flashcard/assets/90729548/a40ec7c1-69cc-46e5-aedd-e33795e0ca68">

In the entry box at the top, type the name of your file with the `.txt` at the end. Once you've finished typing, click the Enter button. 

Click the flip button to switch back and forth between the different sides of the current card. The two buttons on the bottom right let you go back and forth between cards, and the bottom left tells you which card you are currently on. When you switch cards, it will always start with the first line provided for that card. For example, in `exampleTextFile.txt`, the first 9 cards will start with the question side. 
