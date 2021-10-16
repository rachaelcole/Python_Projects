import os
import time

source = [r'C:\Users\Rachael\Desktop\CyberSec\Notes']

target_dir = r'C:\Users\Rachael\Desktop\Backups'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime("%d%m%Y")
now = time.strftime("%H:%M:%S")

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'compact /c {source} /I /Q'.format(source=source[0])

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')
