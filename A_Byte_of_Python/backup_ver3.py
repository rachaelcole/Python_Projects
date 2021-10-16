import os
import time

source = [r'C:\Users\Rachael\Desktop\CyberSec\Notes']

target_dir = r'C:\Users\Rachael\Desktop\Backup'

today = target_dir + time.strftime('%d%m%Y')
now = time.strftime('%H:%M:%S')

comment = input('Enter a comment -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'compact /c {0} /I /Q'.format(source[0])

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')
