# Script is used to iteratively check if the input asked for is a valid guess.
# %% 
import milestone_2 as m2

# %%
# Conditional statement to see if guess is found in chosen word.
def check_guess(guess):
    # ensure guess letter is lowercase
    guess = guess.lower()
    if guess in m2.word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

# %% 
# Create while loop asking user to guess a letter, check the input, and store into a variable.
def ask_for_input():
    while True:
        # Ask user to guess a letter and assign to 'guess' variable
        guess = input('Please enter a single alphabetical letter: ')

        # Check that guess is a single alphabetical letter
        if len(guess) == 1 and guess.isalpha() == True:
            print(f'Thank you, you have entered {guess}. Good guess!')
            break
        else:
            print(f'Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)


# %%
