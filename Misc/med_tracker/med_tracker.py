import csv
import pyinputplus as pyip
import os

# Set CSV headers
header = ['id', 'date', 'morn', 'noon', 'night']
data = []
again = 'yes'

# Get user input and add to data list
while again == 'yes':
    user_input = input('Enter id, date (dd/mm/yy), morning time (e.g. 10.00am), noon time (e.g. 1.30pm), and night time (e.g. 8.00pm) \n')
    data.append(user_input.split(","))
    again = pyip.inputYesNo('Make another entry? y/n \n')


# Function for writing data to csv file
def write_rows(writer, data):
    # Check if multiple rows or 1 item in 'data'
    if len(data) == 1:
        print('Writing 1 entry...')
        writer.writerow(data)
    elif len(data) == 0:
        print('No data to add, terminating process...')
    else:
        print(f'Writing {len(data)} entries...')
        writer.writerows(data)


# Check if csv file exists
if not os.path.isfile('med_tracker.csv'):
    # Open csv file in write mode with header
    with open('med_tracker.csv', 'w', encoding='utf-8', newline='') as db:
        writer = csv.writer(db)
        # Write the header
        writer.writerow(header)
        write_rows(writer, data)
else:
    # Open CSV file in append mode with newline=''
    with open('med_tracker.csv', 'a+', encoding='utf-8', newline='') as db:
        writer = csv.writer(db)
        write_rows(writer, data)

        
print('Process complete!')
