#!/user/bin/env python3
# clickbaitgenerator.py - Are Millenials Killing the Cat Industry?
# Generates random clickbait headlines in a Mad Libs-style program

import random

# Initialise constants
object_pronouns = ['Her', 'Him', 'Them']
possessive_pronouns = ['Her', 'His', 'Their']
personal_pronouns = ['She', 'He', 'They']
states = ['Victoria', 'New South Wales', 'Tasmania', 'Queensland', 'South Australia', 'Northern Territory',
          'Australian Capital Territory', 'Western Australia']
nouns = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Dealer', 'Chicken', 'Robot',
         'Video Game', 'Avocado', 'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
places = ['House', 'Attic', 'ATM', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


# Each of these functions returns a different type of headline
def generate_are_millenials_killing():
    noun = random.choice(nouns)
    return f'Are Millenials Killing the {noun} Industry?'


def generate_what_you_dont_know():
    noun = random.choice(nouns)
    plural_noun = random.choice(nouns) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {plural_noun} Could Kill You {when}'


def generate_big_companies_hate_her():
    pronoun = random.choice(object_pronouns)
    state = random.choice(states)
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def generate_you_wont_believe():
    state = random.choice(states)
    noun = random.choice(nouns)
    pronoun = random.choice(possessive_pronouns)
    place = random.choice(places)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generate_dont_want_you_to_know():
    pluralnoun1 = random.choice(nouns) + 's'
    pluralnoun2 = random.choice(nouns) + 's'
    return f"What {pluralnoun1} Don't Want You To Know About {pluralnoun2}"


def generate_gift_idea():
    num = random.randint(7, 15)
    noun = random.choice(nouns)
    state = random.choice(states)
    return f'{num} Gift Ideas To Give Your {noun} From {state}'


def generate_reasons_why():
    num1 = random.randint(3, 19)
    pluralnoun = random.choice(nouns) + 's'
    num2 = random.randint(1, num1)
    return f'{num1} Reasons Why {pluralnoun} Are More Interesting Than You Think (Number {num2} Will Blow Your Mind!!)'


def generate_job_automated():
    state = random.choice(states)
    noun = random.choice(nouns)
    i = random.randint(0, 2)
    pronoun1 = possessive_pronouns[i]
    pronoun2 = personal_pronouns[i]
    if pronoun1 == 'Their':
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong."


# Main program function
def main():
    print('Clickbait Headline Generator')
    print()
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            num_headlines = int(response)
            break
    for i in range(num_headlines):
        clickbait_type = random.randint(1, 8)
        if clickbait_type == 1:
            headline = generate_are_millenials_killing()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_to_know()
        elif clickbait_type == 6:
            headline = generate_gift_idea()
        elif clickbait_type == 7:
            headline = generate_reasons_why()
        elif clickbait_type == 8:
            headline = generate_job_automated()
        print(headline)
    print()

    website = random.choice(['website', 'blog', 'Facebook', 'Google', 'Twitter', 'Instagram', 'TikTok'])
    when = random.choice(WHEN).lower()
    print(f'Post these to our {website} {when} or you\'re fired!!')


if __name__ == '__main__':
    main()
