#! python3
# madlibs.py - Take user input and return mad libs
# e.g.  "{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with
# his {adjective} wife."
# DYNAMIC MAD LIB:
# Choose mad lib keys from a dict
# e.g. f'{exclamation}!' he said {adverb}, as he jumped into his convertible {noun1} and drove off into the {noun2} with his {adjective} wife
# if 'word_type' in 'mad_lib_chosen': get user input for 'word_type' and store that in a variable
import random

# Initialise user input variables
exclamation = ''
adverb = ''
verb = ''
noun1 = ''
noun2 = ''
adjective = ''
pronoun = ''
number = 0


# Define a function to get the keys of the chosen madlib
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
    # Store madlibs as a list of strings
    madlibs = [
        "'{exclamation}!' he said {adverb}, as he jumped into his convertible {noun1} and drove off into the {noun2} with his {adjective} wife",
        "Today {pronoun} went to the {noun1} and saw {number} {noun2}s! {pronoun} counted them {adverb}, because {pronoun} is good at {noun1}.",
        "I love to {verb}, but only when I'm feeling {adjective}. It just isn't the same when {noun1} is going {adverb}. {exclamation}!"
    ]
    # Select a madlib from the madlibs list at random:
    print("Selecting a random mad lib...")
    madlib_index = random.randint(0, len(madlibs) - 1)
    # print("DEBUG:", madlib_index)
    madlib = madlibs[madlib_index]
    # print("DEBUG:", madlib)
    print("Madlib chosen! Let's play!\n")

    tell_story(madlib)
    input("Press Enter to end the program.")


main()


