# Script created to create the hangman game class.

# %% 
# Import relevant Libraries needed for code
import random   # used for random numbers and selecting random things etc.

# # %% import code from the third milestone (milestone_3.py)
# import milestone_3 as m3
# import milestone_2 as m2

# %%
# Make list of favourite fruits and call variable 'word_list'
word_list  = ['blueberry', 'lemon', 'banana', 'satsuma', 'apple']

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
        self.num_letters = len(set(self.word)) + 1

        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        # ensure guess letter is lowercase
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

            for letter in self.word:
                if letter == guess:
                    self.word_guessed[self.word.find(letter)] = letter
                    print(test_game.word_guessed)
            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            self.num_lives -= 1
            print(f'ou have, {self.num_lives} left.')

    def ask_for_input(self):
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

                # Code to check how many lives are left, if 0, then the game will end.
                if self.num_lives == 0:
                    print('You have run out of lives. GAME OVER!')
                    break
                



# %%
# Call the ask_for_input method to test code.
test_game = Hangman(word_list=word_list, num_lives=3)

test_game.ask_for_input()


# %%
