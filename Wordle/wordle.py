# Get all 5 letter words from the full English dictionary
"""
# dictionary by http://www.gwicks.net/dictionaries.htm
# Load full English dictionary
dictionary = open("Dictionary.txt", 'r')
# Load new empty dictionary
new_dictionary = open("5 letter word dictionary.txt", "w")

# Read the full English dictionary
dictionary_content = dictionary.read()
# Split the full dictionary on every new line
dictionary_content = dictionary_content.split("\n") # This returns a list of all the words in the dictionary

# Loop over all the words in the full dictionary
for i in dictionary_content:
    # Check if the current word is 5 characters long
    if len(i) == 5:
        # Write word to the new dictionary
        new_dictionary.write(f"{i}\n")

# Close out of the new dictionary
new_dictionary.close()
"""

# import the library random
import random

# Load 5 letter word dictionary
dictionary = open("5 letter word dictionary.txt", 'r')
# Read content of dictionary
dictionary = dictionary.read()
# Split the dictionary on every new line
dictionary = dictionary.split('\n') # This returns a list of all the words in the dictionary

# Choose a random word from the dictionary
word = random.choice(dictionary)

# Get all the unique letters of the word
dif_letters = list(set(word))

# Count how many times each letter occurs in the word
count_letters = {}
for i in dif_letters:
    count_letters[i] = word.count(i)

# Set tries to 0
tries = 0

# Main loop
while True:
    # Check if the user has used all of their tries
    if tries == 6:
        print(f"You did not guess the word!\nThe word was {word}")
        break
    # Get user input
    user_inp = input(">>")

    # Check if user wants to exit the program
    if user_inp == "q":
        break

    # Check if the word given by the user is 5 characters long
    if not len(user_inp) == 5:
        print("Your input must be 5 letters long")
        continue

    # Check if the word given by the user is in the dictionary
    if not user_inp in dictionary:
        print("Your word is not in the dictionary")
        continue

    # Check if the word given by the user is correct
    if user_inp == word:
        print(f"You guessed the word in {tries} tries")
        break

    # Check guess
    letter = 0
    letter_dict = {}
    letters_checked = []
    return_answer = ""
    for i in word:
        # Check if letter is already checked
        counter = 0
        cont = False
        for g in letters_checked:
            if g == user_inp[letter]:
                counter += 1
                # Check if letter has been checkd more or equal to the ammount of these letters inside of the word
                if counter >= count_letters[i]:
                    # If so set cont to true
                    cont = True

        # Check if cont is true
        if cont:
            # Set return answer to -
            return_answer += "-"
            # Append checked letter to the list letters_checked
            letters_checked.append(user_inp[letter])
            # Increase letters by 1
            letter += 1
            # Go back to the beginning of the for loop (skipping everything that comes after this)
            continue


        answer_given = False
        # Check if letter is in word
        if user_inp[letter] in word:
            # Set answer_given to true
            answer_given = True
            # Check if letter is in the correct position
            if user_inp[letter] == i:
                # Set return answer to G
                return_answer += "G"
            else:
                if not user_inp[word.index(user_inp[letter])] == word[word.index(user_inp[letter])]:
                    # Set return answer to Y
                    return_answer += "Y"

        # Check if there has already been an answer returned
        if not answer_given:
            # Set return answer to -
            return_answer += "-"

        # Append checked letter to the list letters_checked
        letters_checked.append(user_inp[letter])
        # Increase letters by 1
        letter += 1

    # Print the return answer
    print(return_answer)

    # Increase tries by 1
    tries += 1
