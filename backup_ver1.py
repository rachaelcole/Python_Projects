import os
import time

# 1. The files and directories to be backed up are
# specified in a list. Example on Windows:
source = [r'C:\Users\Rachael\Desktop\CyberSec\Notes']

# 2. The backup must be stored in a main backup
# directory
target_dir = r'C:\Users\Rachael\Documents'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime("%d/%m/%Y %H:%M:%S") + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = 'compact /c {0} /I /Q'.format(source[0])

# Run the backup
print('Source is', source)
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')
