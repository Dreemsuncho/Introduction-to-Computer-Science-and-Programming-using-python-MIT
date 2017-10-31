# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for let in secret_word:
        if let.lower() not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = ''
    if is_word_guessed(secret_word, letters_guessed):
        return secret_word
    else:
        for let in secret_word:
            if let.lower() not in letters_guessed:
                result += '_ '
            else:
                result += let

    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    result = ''
    for let in string.ascii_lowercase:
        if let not in letters_guessed:
            result += let

    return result

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    def letter_is_valid(letter):
        '''
        Return true if character is alphabetical and 
        has length of "1" and letter dosn't exist in guessed letteres. 
        Otherwise return false
        '''
        return str.isalpha(letter) and len(letter) == 1 and letter not in letters_guessed

    guesses_left = 6
    warrnings_left = 3
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print('I am taking of a word that is', len(secret_word), 'letters long.')
    print('You have', warrnings_left, 'warnings left.')

    while True:
        print('------------ ')

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            total_score = guesses_left * len(set(secret_word))
            print('Your total score for this game is:', total_score)
            break
        elif guesses_left <= 0:
            print('Sorry, you ran out of guesses. The word was:', secret_word)
            break

        print('You have', guesses_left, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))

        letter = input('Please guess a letter: ').lower()
        guesses_lose = 1
        if letter in ['a', 'e', 'i', 'o', 'u'] and letter not in letters_guessed:
            guesses_lose += 1

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if not letter_is_valid(letter):
            if warrnings_left == 0:
                warrnings_left = 3
                guesses_left -= guesses_lose
                print(
                    'Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ', guessed_word)

            elif not str.isalpha(letter) or len(letter) != 1:
                warrnings_left -= 1
                print('Oops! That is not a valid letter. You have',
                      warrnings_left, 'warnings left:', guessed_word)
            elif letter in letters_guessed:
                warrnings_left -= 1
                print('Oops! you\'ve already guessed that letter. You now have',
                      warrnings_left, 'warrnings left:')
                print(guessed_word)
            continue

        letters_guessed.append(letter.lower())

        if letter in secret_word.lower():
            print('Good guess:', get_guessed_word(
                secret_word, letters_guessed))
        else:
            guesses_left -= guesses_lose
            print('Oops! That letter is not in my word:',
                  get_guessed_word(secret_word, letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    my_word = my_word.replace(' ', '').lower()
    other_word = other_word.lower()

    is_equal = True

    if len(my_word) != len(other_word):
        is_equal = False
    else:   
        for let in other_word:
            if my_word.count(let) > 0 and my_word.count(let) != other_word.count(let):
                is_equal = False
                break

        for i, let in enumerate(my_word):
            if let != '_' and let != other_word[i] and is_equal:
                is_equal = False
                break

    return is_equal


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word,word):
            matched_words.append(word)

    if len(matched_words) == 0:
        print('No matches found')
    else:
        print(' '.join(matched_words))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    def letter_is_valid(letter):
        '''
        Return true if character is alphabetical and 
        has length of "1" and letter dosn't exist in guessed letteres. 
        Otherwise return false
        '''
        return str.isalpha(letter) and len(letter) == 1 and letter not in letters_guessed

    guesses_left = 6
    warrnings_left = 3
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print('I am taking of a word that is', len(secret_word), 'letters long.')
    print('You have', warrnings_left, 'warnings left.')

    while True:
        print('------------ ')

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            total_score = guesses_left * len(set(secret_word))
            print('Your total score for this game is:', total_score)
            break
        elif guesses_left <= 0:
            print('Sorry, you ran out of guesses. The word was:', secret_word)
            break

        print('You have', guesses_left, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))

        letter = input('Please guess a letter: ').lower()
        guesses_lose = 1
        if letter in ['a', 'e', 'i', 'o', 'u'] and letter not in letters_guessed:
            guesses_lose += 1
        elif letter == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
            continue

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if not letter_is_valid(letter):
            if warrnings_left == 0:
                warrnings_left = 3
                guesses_left -= guesses_lose
                print(
                    'Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ', guessed_word)

            elif not str.isalpha(letter) or len(letter) != 1:
                warrnings_left -= 1
                print('Oops! That is not a valid letter. You have',
                      warrnings_left, 'warnings left:', guessed_word)
            elif letter in letters_guessed:
                warrnings_left -= 1
                print('Oops! you\'ve already guessed that letter. You now have',
                      warrnings_left, 'warrnings left:')
                print(guessed_word)
            continue

        letters_guessed.append(letter.lower())

        if letter in secret_word.lower():
            print('Good guess:', get_guessed_word(
                secret_word, letters_guessed))
        else:
            guesses_left -= guesses_lose
            print('Oops! That letter is not in my word:',
                  get_guessed_word(secret_word, letters_guessed))

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # show_possible_matches("t_ _ t")
    # show_possible_matches("abbbb_ ")
    # show_possible_matches("a_ pl_ ")

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
