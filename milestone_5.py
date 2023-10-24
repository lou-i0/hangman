# final script of the hangman Project Game.

# %% 
# Import relevant Libraries needed for code
import random   # used for random numbers and selecting random things etc.

# %%
# Create a class called 'Hangman'
class Hangman:
    # Initialise class with attributes
    def __init__(self, word_list : list, num_lives : int = 5):
        # Pick a word from word list and put into 'word' variable
        self.word = random.choice(word_list)

        # a list of letters of the selected word, with '_' for each letter not guessed
        self.word_guessed = ['_' for i in self.word]

        # The UNIQUE letter count in the word that have not been guessed yet
        self.num_letters = len(set(self.word))

        self.num_lives = num_lives
        self.word_list = [word.lower() for word in word_list]
        self.list_of_guesses = []
        

    def ask_for_input(self):
        ''' 
        This method asks the user for an input, validates the input given
        , then calls the check_guess method to se if the guess is in the selected word.

        Additionally , there are no parameters but has a infinite while loop to check and await feedback before
        going down a particular route. It also provides feedback to the user of the guesses made, how many lives left if used (GAME OVER!)
        
        The Loop ends when either all lives have been used, or all letters have been found (GAME COMPLETE).
        '''
        while True:
            # Ask user to guess a letter and assign to 'guess' variable
            guess = input('Please enter a single alphabetical letter: ')

            if len(guess) != 1 or guess.isalpha == False :
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

                # # Code to check how many lives are left, if 0, then the game will end.
                if self.num_lives == 0:
                    print('You have run out of lives. GAME OVER!')
                    break
                
                # Code to check if all letters for word have been guessed
                if ''.join(self.word_guessed) == self.word:
                    print(f'You have found all the letters for {self.word}, Congratulations! GAME COMPLETE')
                    break
                else:
                    print(f'You still have {self.num_letters} letters to find.')


    def check_guess(self, guess):
        '''
         The check_guess method takes in the guess entered by the user as a parameter. Then, 
         checks if the guess is in the selected word. If so, provides feedback saying this and where the letter is placed in the word and asks 
         to enter another letter to guess.If not, a life is lost and shows this to the user, before asking to try again.
        '''
        # ensure guess letter is lowercase
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

            # find guess and replace in right positon in 'word_guessed'
            for i,  letter_in_word in enumerate(self.word):
                if letter_in_word == guess:
                    #self.word_guessed[self.word.find(letter)] = letter
                    self.word_guessed[i] = letter_in_word
                    
            self.num_letters -= 1
            print(self.word_guessed)

        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1
            print(f'You have, {self.num_lives} left.')
# %%
def play_game(word_list):
    '''
        'play_game' function is defined to  kick off the hangman game. there where notes on AIcore to follow to implement
        the commented out code, but found the code i did previously, to fit the situation better (sorry AICore!).
    '''
    # set number of lives/ attempts user has to guess the word / letter.
    num_lives = 5

    game = Hangman(word_list = word_list, num_lives = num_lives)

    # set off the 'ask_for_input method to begin the game
    game.ask_for_input()

    # As instructed by AICORE, but commented, as previous code works better.
    # while True:
    #     if num_lives == 0:
    #         print('You Lost! GAME OVER.')
    #     elif game.num_letters > 0:
    #         game.ask_for_input()
    #     else:
    #         print('Congratulations! You won the game. GAME COMPLETE')
        
# %% 
# Call 'play_game' function to play the hangman game
play_game(word_list = ['berry', 'toffee','apple'])