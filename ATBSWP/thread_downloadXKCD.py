#! python3
# thread_downloadXKCD.py - Downloads XKCD comics using multiple threads

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)      # Store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print(f'Downloading page https://xkcd.com/{urlNumber}')
        res = requests.get(f'https://xkcd.com/{urlNumber}')  # Download the page
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Parse the page's HTML
        # Find the URL of the comic image
        comicElem = soup.select('#comic img')  # Select comic by HTML tag classes
        if comicElem == []  # If no comics found
            print('Could not find comic image.')
        else:
            comicURL = comicElem[0].get('src')  # Get url of the image
            # Download the image
            print(f'Downloading image {comicUrl}...')
            res = requests.get('https:' + comicUrl)  # Downloads the image
            res.raise_for_status()
            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start Thread objects
downloadThreads = []  # A list of all the thread objects
for i in range(0, 140, 10):     # loops 14 times, creates 14 threads
    start = 1
    end = i + 9
    if start == 0:
        start = 1       # There is no comic 0, so set it to 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
