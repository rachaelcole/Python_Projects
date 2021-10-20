#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along wih the answer key.

import random

# The quiz data. Keys are states and values are capital cities.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California':
            'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana':
            'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana':
            'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
            'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
            'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
            'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia':
            'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':
            'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(2):                                                   # loops 35 times
    # Create the quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')                  # open a new file in write mode called
                                                                            # capitalsquiz<x>.txt

    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')     # open new file in write mode called
                                                                            # capitalsquiz_answers<x>.txt

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())                                          # save the names of the states in a list
    random.shuffle(states)                                                  # shuffle the order of the list

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())                              # gets a list of all the capital cities
        del wrongAnswers[wrongAnswers.index(correctAnswer)]                 # removes the correct answer from the list
        wrongAnswers = random.sample(wrongAnswers, 3)                       # select 3 random cities from the list
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)                                       # randomise order of answerOptions

        # Write the question and answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')

        # Write answer to key file
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
