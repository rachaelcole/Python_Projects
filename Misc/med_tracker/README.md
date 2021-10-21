# Med tracker
Write a program that writes the time the user took medications 3x #each day to a csv file

For example:

ID	|	DATE	|	MORN	|	NOON	|	NIGHT
 
0	  18/10/2021		10.00AM		2.00PM		8.00PM
 
1	     19/10/2021         10.30AM         2.00PM          8.30PM
  
2         20/10/2021         11.00AM		2.00PM		8.00PM

### Example .csv file:

ID,DATE, MORN, NOON, NIGHT

0,18/10/2021,10.00am,2.00pm,8.00pm,
1,19/10/2021,10.30am,2.00pm,8.30pm,
2,20/10/2021,11.00am,2.00pm,8.00pm


--------------------------------------------------------------
### Requirements: 

`import csv, pyinputplus as pyip, os`


--------------------------------------------------------------
### Pseudocode:
1. Get data as a list of inputs
2. Open the CSV file for writing using with and open()
3. Create a CSV writer object using csv.writer()
4. Write data to CSV file using csv.writerow()/csv.writerows()

--------------------------------------------------------------
### Known bugs/errors:
1. No input validation
2. Non-alphanum, /, :, and comma (,) characters should not be permitted to be written to the CSV file
3. When adding a single entry, the "[]" list chars are also written to the csv file
