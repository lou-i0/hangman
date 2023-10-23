
# %% 
# Import relevant Libaries needed for code
import random   # used for random numbers and selecting random things etc.

# %%  
# Make a list of favourite fruits call the variable 'word_list'
word_list  = ['Blueberry', 'Lemon', 'Banana', 'Satsuma', 'Apple']

# %%
# Print out word list 
print(word_list)

# %% 
# Pick a word from the word list and put into the 'word' variable
word = random.choice(word_list)

# print out the word chosen
print(word)