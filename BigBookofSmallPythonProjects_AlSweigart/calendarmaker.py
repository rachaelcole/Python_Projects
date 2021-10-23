#!/user/bin/env python3
# calendarmaker.py - Generates a multiline string to display a monthly calendar page

import datetime

# Initialise constants
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

print('Calendar Maker')

while True:  # Loop to get a year from the user
    print('Enter the year for the calendar:')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please enter a numeric year, e.g., 2023.')
    continue

while True:  # Loop to get a month from the user
    print('Enter the month for the calendar (1 - 12):')
    response = input('> ')
    if not response.isdecimal():
        print('Please enter a numeric month, e.g., 3 for March.')
        continue
    month = int(response)
    if 1 <= month <= 12:
        break
    print('Please enter a number from 1 to 12.')


def get_calendar(year, month):
    cal_text = ''  # cal_text will contain the string of our calendar
    # Put the month and year at the top of the calendar
    cal_text += (' ' * 34) + months[month - 1] + ' ' + str(year) + '\n'
    # Add the days of the week labels to the calendar
    cal_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    week_separator = ('+----------' * 7) + '|\n'
    blank_row = ('|          ' * 7) + '\n'
    current_date = datetime.date(year, month, 1)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)
    while True:  # Loop over each week in the month
        cal_text += week_separator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Go to next day
        day_number_row += '|\n'  # Add vertical line after Saturday
        # Add the day number row and 3 blank rows to the cal text
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row
        if current_date.month != month:
            break
    # Add the horizontal line at the bottom
    cal_text += week_separator
    return cal_text

cal_text = get_calendar(year, month)
print(cal_text)

calendar_filename = f'calendar_{year}_{month}.txt'
with open(calendar_filename, 'w') as file_object:
    file_object.write(cal_text)

print(f'Saved to {calendar_filename}.')
