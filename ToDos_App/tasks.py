# tasks.py - A basic to-do list application built using Python and a SQLite database

# TODO: very very unfinished code !!! 
        # CONSULT pseudocode.md AND TODO items below to continue
        # TODO: change ALL_USERNAMES global variable to sqlite3 db (same for Tasks)

import sys
import datetime

# SET GLOBAL VARIABLES

# Set global categories variable
CATEGORIES =  ['employment', 'programming', 'reading', 'self_care', 'exercise', 'relaxing', 'socialising',
               'health', 'chores', 'other']
# Set global users list variable that holds User objects as list items - TODO: change to sqlite3 db
ALL_USERNAMES = list()


# DECLARE CLASSES

# User class
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.task_list = []
        # Add user to global variable on initialisation - TODO: change to sqlite3 db
        ALL_USERNAMES.append(self.username)
    
    def add_task(self, task, category):
        task_add = Task(task, category)
        self.task_list.append(task_add)
            
    def __repr__(self):
        return f'User: {self.username}\nTasks: {[x for x in self.task_list]}'

# Task class
class Task(object):
    def __init__(self, task, category):
        self.name = task
        self.category = category
        self.completed = False
        self.date_added = datetime.datetime.now()


# EXECUTE THE PROGRAM

# Main program execution
def main():
    # Initialise a sample User() for testing
    sample_user = User('sample_user', 'test_password')
    # Add a task for our sample_user
    sample_user.add_task('wash dog', 'chores')
    sample_user.add_task('5km run', 'exercise')
    # Print the string representation of our user:
    # print(sample_user)
    # Print a list of all the users
    #print(f'All users: {ALL_USERNAMES}')
    # Print the sample_user's first task and its category:
    #first = sample_user.task_list[0]
    #print(f'First task: {first.name}\nCategory: {first.category}')
    # Print all of sample_user's tasks and their categories:
    tasks = sample_user.task_list
    for task in tasks:
        print(f'{task.name} ({task.category})')


if __name__ == "__main__":
    main()