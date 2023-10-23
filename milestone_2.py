
# %% 
# Import relevant Libraries needed for code
import random   # used for random numbers and selecting random things etc.

# %%  
# Make list of favourite fruits and call variable 'word_list'
word_list  = ['Blueberry', 'Lemon', 'Banana', 'Satsuma', 'Apple']

# %%
# Print out word list 
print(word_list)

# %% 
# Pick a word from word list and put into 'word' variable
word = random.choice(word_list)

# print out the word chosen
print(word)

# %%
#  create function to ask user for single letter 
def guess_letter():
    guess = input('Please guess a alphabetical letter: ')

    if len(guess) == 1 and guess.isalpha() == True:
        print(f'Thank you, you have entered {guess}. Good guess!')
    else:
        print(f'Oops! That is not a valid input. {guess} is not a single alphabetical letter')
    return guess


# %%
#guess_1 = guess_letter()


# %%
