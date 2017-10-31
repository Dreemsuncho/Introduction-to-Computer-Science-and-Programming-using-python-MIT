
## Class exercises:

### Problem Set 0.

* #### Assignment: [ps0.py](https://github.com/Dreemsuncho/Introduction-to-Computer-Science-and-Programming-using-python-MIT/blob/master/Class/ps0/ps0.py)
    Write a program that does the following in order:

    1. Asks the user to enter a number “x”
    2. Asks the user to enter a number “y”  
    3. Prints out number “x”, raised to the power “y”. 
    4. Prints out the log (base 2) of “x”.  

    ##### Example:
    Enter number x: 2 <br />
    Enter number y: 3 <br />
    X**y =  8 g<br />
    log(x) = 1

<br />

### Problem Set 1.

* #### House Hunting: [ps1A.py](https://github.com/Dreemsuncho/Introduction-to-Computer-Science-and-Programming-using-python-MIT/blob/master/Class/ps1/ps1A.py)
    Write a program to calculate how many months it will take you to save up enough money for a down
    payment. You will want your main variables to be floats, so you should cast user inputs to floats.   
    1
    Your program should ask the user to enter the following variables:
    1. The starting annual salary (annual_salary)
    2. The portion of salary to be saved (portion_saved)
    3. The cost of your dream home (total_cost)

    Test Case 1 
   <br/> >>>
   <br/> Enter your annual salary: 120000
   <br/> Enter the percent of your salary to save, as a decimal: .10
   <br/> Enter the cost of your dream home: 1000000
   <br/> Number of months: 183 
   <br/> >>>
   <br/> Test Case 2 
   <br/> >>>
   <br/> Enter your annual salary: 80000 
   <br/> Enter the percent of your salary to save, as a decimal: .15
   <br/> Enter the cost of your dream home: 500000
   <br/> Number of months: 105
   <br/> >>>

* #### Saving, with a raise: [ps1.py](https://github.com/Dreemsuncho/Introduction-to-Computer-Science-and-Programming-using-python-MIT/blob/master/Class/ps1/ps1B.py)
    Write a program to calculate how many months it will take you save up enough money for a down
    payment.  LIke before, assume that your investments earn a return of r​ = 0.04 (or 4%) and the
    required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
    1. The starting annual salary (annual_salary)
    2. The percentage of salary to be saved (portion_saved)
    3. The cost of your dream home (total_cost)
    4. The semi­annual salary raise (semi_annual_raise)

    Test Case 1 
   <br/> >>>  
   <br/> Enter your starting annual salary: 120000
   <br/> Enter the percent of your salary to save, as a decimal: .05
   <br/> Enter the cost of your dream home: 500000
   <br/> Enter the semi­annual raise, as a decimal: .03
   <br/> Number of months: 142 
   <br/> >>>
   <br/> Test Case 2 
   <br/> >>>  
   <br/> Enter your starting annual salary: 80000
   <br/> Enter the percent of your salary to save, as a decimal: .1
   <br/> Enter the cost of your dream home: 800000
   <br/> Enter the semi­annual raise, as a decimal: .03
   <br/> Number of months: 159 
   <br/> >>>
   <br/> Test Case 3 
   <br/> >>>  
   <br/> Enter your starting annual salary: 75000
   <br/> Enter the percent of your salary to save, as a decimal: .05
   <br/> Enter the cost of your dream home: 1500000
   <br/> Enter the semi­annual raise, as a decimal: .05
   <br/> Number of months: 261 
   <br/> >>>

### Problem Set 2.
   
* #### Basic Hangman: [hangman.py](https://github.com/Dreemsuncho/Introduction-to-Computer-Science-and-Programming-using-python-MIT/blob/master/Class/ps2/hangman.py)
    You will implement a variation of the classic word game Hangman. If you are  unfamiliar with the rules of the game, read  http://en.wikipedia.org/wiki/Hangman_(game)​. Don’t be intimidated by this problem ­  it's actually easier than it looks! We will 'scaffold' this problem, guiding you through  the creation of helper functions before you implement the actual game.

    * A) Getting Started <br/>
        Download the files “hangman.py” and “words.txt”, and ​save them both in the same  directory​. Run the file hangman.py before writing any code to ensure your files are  saved correctly. The code we have given you loads in words from a file. You should  see the following output in your shell:                              
        Loading word list from file...<br/> 
        55900 words loaded.

        If you see the above text, continue on to Hangman Game Requirements. If you don’t, double check that both files are saved in the same place!  

    * B) Hangman Game Requirement <br/>
        You will implement a function called ​hangman​ that will allow the user to play hangman  against the computer. The computer picks the word,and the player tries to guess  letters in the word.   
        Here is the general behavior we want to implement. Don’t be intimidated! This is just  a description; ​we will break this down into steps and provide further  functional specs later on in the pset so keep reading!

        1. The computer must select a word at random from the list of available words  that was provided in words.tx​Note that words.txt contains words in all lowercase letters.<br/>
        2. The user is given a certain number of guesses at the beginning. <br/>
        3. The game is interactive; the user inputs their guess and the computer either:<br/>
            a. reveals the letter if it exists in the secret word <br/>
            b. penalize the user and updates the number of guesses remaining <br/>
        4. The game ends when either the user guesses the secret word, or the user runs  out of guesses.
