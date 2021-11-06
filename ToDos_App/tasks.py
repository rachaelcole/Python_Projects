# tasks.py - A basic to-do list application built using Python and a Peewee Sqlite database
import datetime
from operator import add
from peewee import *


db = SqliteDatabase('tasks.db')


class Task(Model):
    task_name = CharField()
    date_added = TimestampField(default=datetime.datetime.now())
    completed = BooleanField(default=False)
    date_completed = DateTimeField(null=True, default=None)
    category = TextField()

    class Meta:
        database = db


def initialise():
    """ Create the database and the tables if they don't exist """
    db.connect()
    db.create_tables([Task], safe=True)


def add_task(name, cat):
    """ Add a task to the tasks table """
    new_task = Task.create(task_name=name, category=cat,)
    new_task.save()
    return new_task

#TODO: def delete_task(task), def delete_all_tasks()

def check_task_completed(task):
    """ Toggle a task's completed attribute """
    if task.completed == 0:
        task.completed = 1
        task.date_completed = datetime.datetime.now()
    elif task.completed == 1:
        task.completed = 0
        task.date_completed = None
    task.save()
    return task

# TODO: check/uncheck ALL tasks

def print_all_tasks():
    """Print all tasks"""
    print('Printing all tasks:\n')
    rows = Task.select()
    for row in rows:
        if row.completed == 0:
            completed_task = 'no'
        elif row.completed == 1:
            completed_task = 'yes'
        print(f'''Task: {row.task_name}
Date added: {row.date_added}
Completed? {completed_task}
Date completed: {row.date_completed}\n''')

#TODO: implement task statistics


def main():
    """ Boot up db """
    initialise()
    print('Welcome to Tasks.py, a local to-do list app!\n')



if __name__ == "__main__":
    main()
    
    print_all_tasks()


    # Close DB connection:
    db.close()
