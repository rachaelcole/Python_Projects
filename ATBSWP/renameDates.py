#! python3
# renameDates.py - Renames files with American MM-DD-YYYY format to European/Australian DD-MM-YYYY format

import shutil
import os
import re

# Create a regex that matches files with an American date format
date_pattern = re.compile(r"^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$", re.VERBOSE)

# Loop over files in the working directory
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date
    if mo is None:
        continue

    # Get the different parts of the file name
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Form the European-style filename
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amer_filename = os.path.join(absWorkingDir, amer_filename)
    euro_filename = os.path.join(absWorkingDir, euro_filename)

    # Rename the files
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    shutil.move(amer_filename, euro_filename)
