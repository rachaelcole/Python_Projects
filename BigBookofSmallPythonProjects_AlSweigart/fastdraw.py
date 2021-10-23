#!/user/bin/env python3
# fastdraw.py - A 'quickdraw' game

import random, sys, time

print('Fast Draw!!\n\nTime to test your reflexes and see if you are the fastest draw in the west!\n\n'
      'When you see DRAW, you have 0.3 seconds to press Enter.\n\n')
input('Press Enter to begin...')

while True:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawtime = time.time()
    input()
    timeElapsed = time.time() - drawtime

    if timeElapsed < 0.01:
        print('You drew too early! You lose!')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print(f'You took {timeElapsed} seconds to draw.\nToo slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print(f'You took {timeElapsed} seconds to draw.\nYou are the fastest draw in the west! You win!\n')
    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
