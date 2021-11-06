# To-do list application: '`tasks.py`'

A basic to-do list application built using Python that presents a list of to-do items (called `tasks`) entered by the user, which are stored in a local SQLite database.<br><br>

--------------------------
<br>


**TODOS:** 

A to-do list for my to-do list app (in order of priority):

1. Implement functions: delete_task, delete_all_tasks, etc.
2. Continue implementing functionalities outlined below...

<br>

--------------------------
<br>

## 1. Components
<br>

### 1.1. Users

<br>

The user can perform the following actions: 

* add a task
* check tasks off to complete them
* view remaining tasks to do
* view a list of completed tasks
* filter tasks by category
* delete a task
* delete all tasks
* complete all remaining tasks
* view statistics on the tasks

<br>

### 1.2. Tasks

Tasks have the following attributes:

* name
* date added
* completed flag (default = False)
* if completed = True, a date completed
* a category (one of the following):
  * employment
  * programming
  * reading
  * selfcare
  * exercise
  * relaxing
  * socialising
  * health
  * other

<br>
Tasks have the following methods:

* add a new task
* delete a new task
* complete a task
* show remaining tasks
* show completed tasks
* show statistics of task/s
<br><br>
-------------------------- 
<br>

## 2. Program lifecycle

<br>A very basic outline of the steps the program takes:

1. Access a db of tasks and present list of uncompleted tasks to the user
2. Prompt user to check off a task as they complete it
3. Prompt user for input to add a task
4. Display a list of completed tasks when user presses button
5. Allow user to filter the list of tasks by category
6. Each task can be deleted or edited by the user <br><br>
--------------------------
<br>

## 3. Implementation

<br>

First, I will implement this project as a CLI program with a single user. I will then make a Django version supporting multiple users and a GUI.

<br>

### 3.1. CLI Usage:

	Usage: python tasks.py [*args]

	For example:

	python tasks.py add "todo item"		# Add a new task

	python tasks.py ls					# Show remaining tasks

	python tasks.py ls done				# Show completed tasks

	python tasks.py ls "category"    	# Show tasks in a category

	python tasks.py del all				# Delete all tasks

	python tasks.py del NUMBER			# Delete a task

	python tasks.py done NUMBER			# Complete a task

	python tasks.py done all			# Complete all tasks

	python tasks.py help				# Show usage

	python tasks.py report				# Show statistics


<br>

### 3.2. Database outline


<br>

**Tasks** 

| id  | name      | timestamp  |completed| date_completed | category    |
| --- | --------- | ---------- | ------- | -------------- | ----------- |
| 1   | wash dog  | 05/11/2021 | 0       | NULL           | chores      |
| 2   | 5km run   | 05/11/2021 | 0       | NULL           | exercise    |
| 3   | design db | 05/11/2021 | 1       | 05/11/2021     | programming |
| ... | ...       | ...        | ...     | ...            | ...         |

<br>

----------------------

<div style="text-align: right"><sub>This document is updated periodically. 
Last update: 06/11/2021 4:09PM AEDT.</sub></div>