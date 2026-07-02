import random 
#this is a simple hangman game implementation in Python. The player has to guess the letters of a randomly chosen word from a predefined list.
#  The player has a limited number of attempts to guess the word correctly.

'''word_list contains the list of words that can be chosen for the game.
  The chosen_word variable randomly selects one word from this list. 
 The guessed_letters list is initialized with underscores to represent the letters that have not yet been guessed.
 The player has a total of 6 attempts to guess the word correctly, and the guessd_letters list keeps track of the letters that have already been guessed by the player.'''

word_list = ["python", "java", "javascript", "hangman", "programming"]
chosen_word = random.choice(word_list)
guessed = ["_"] * len(chosen_word) # initialize the guessed list with underscores to represent the letters that have not yet been guessed

attempts = 6
guessed_letters = [] # all the letters that have been guessed by the player stored in this list

print("Welcome to Hangman!")
print ("guess the word: " + " ".join(guessed)) # display the initial state of the guessed letters with underscores and join them with spaces for better readability

while attempts > 0 and "_" in guessed: # while loop continues until the player runs out of attempts or successfully guesses the word
    print(f"You have {attempts} attempts left.")

    guess = input("Guess a letter: ").lower() # prompt the player to input a letter and convert it to lowercase for consistency

    if not guess.isalpha() or len(guess) != 1: # check if the input is a single alphabetic character
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters: # check if the letter has already been guessed
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess) # add the guessed letter to the list of guessed letters

    if guess in chosen_word: # check if the guessed letter is in the chosen word
        print("Good guess!")

        for i in range(len(chosen_word)): # iterate through the chosen word to reveal the guessed letters
            if chosen_word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong guess.")
        attempts -= 1 # decrement the number of attempts left

    print(" ".join(guessed)) # display the current state of the guessed letters with spaces for better readability

if "_" not in guessed: # check if the player has successfully guessed the word

    print("Congratulations! You guessed the word: " + chosen_word)
    
else: # if the player runs out of attempts without guessing the word
    print("Sorry, you ran out of attempts. The word was: " + chosen_word)

print("thanks for playing!")