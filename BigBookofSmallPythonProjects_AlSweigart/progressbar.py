#!/user/bin/env/ pythn3
# progressbar.py - Simulates a download and displays a progress bar

import random
import time

BAR = chr(9608)


def get_progress_bar(progress, total, barWidth = 40):
    progress_bar = ''
    progress_bar += '['
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
    numBars = int((progress / total) * barWidth)
    progress_bar += BAR * numBars
    progress_bar += ' ' * (barWidth - numBars)
    progress_bar += ']'
    percent_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percent_complete) + '%'
    progress_bar += ' ' + str(progress) + '/' + str(total)
    return progress_bar


def main():
    print('Progress Bar Simulation')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)
        barStr = get_progress_bar(bytesDownloaded, downloadSize)
        print(barStr, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(barStr), end='', flush=True)


if __name__ == '__main__':
    main()
