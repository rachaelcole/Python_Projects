#! python3
# madlibs.py - Take user input and return mad libs
# e.g.  "{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with
#       his {adjective} wife."
# DYNAMIC MAD LIB:
# Choose a random mad lib from a txt file of formatted mad lib strings (no quotation marks)
# Dynamically choose mad lib keys from the selected file using find() and dicts

import random

# Initialise user input variables
exclamation = ''
adverb = ''
verb = ''
noun1 = ''
noun2 = ''
noun3 = ''
adjective = ''
pronoun = ''
number = 0


# Define a function to get the keys of the chosen mad lib
def get_keys(string):
    key_list = list()
    end = 0
    repetitions = string.count('{')
    for i in range(repetitions):
        start = string.find('{', end) + 1
        end = string.find('}', start)
        key = string[start:end]
        key_list.append(key)
    return set(key_list)


# Define a function to add words to the user's picked words
def add_pick(cue, dictionary):
    prompt_format = "Enter an example for {name}: "
    prompt = prompt_format.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response


# Define a function to get the user's picks for each word
def get_user_picks(cues):
    user_picks = dict()
    for cue in cues:
        add_pick(cue, user_picks)
    return user_picks


# Define a function tell the story
def tell_story(story):
    cues = get_keys(story)
    user_picks = get_user_picks(cues)
    story = story.format(**user_picks)
    print(story)


# Main function
def main():
    madlibs = list()
    # Prompt the user for the name of a file that should contain a mad lib format string as text
    file_name = input("Enter a file (e.g. madlibs.txt): ")
    # Open the file in read mode
    madlibs_file = open(file_name, "r")
    # Read each row of the file and store in the variable madlibs, which is a list of strings
    madlibs = madlibs_file.readlines()
    # Select a mad lib from the mad libs list at random:
    print("Selecting a random mad lib...")
    madlib_index = random.randint(0, len(madlibs) - 1)
    madlib = madlibs[madlib_index]
    print("Mad lib chosen! Let's play!\n")
    # Call the tell_story() func to print the mad lib with the user's words inserted
    tell_story(madlib)
    # Close the madlibs_file
    madlibs_file.close()
    # Prompt user to exit program
    input("Press Enter to end the program.")


main()


