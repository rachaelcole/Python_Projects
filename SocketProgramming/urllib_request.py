import urllib.request

# Retrieve web page using urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


counts = dict()
for line in fhand:
    # Print each line in the retrieved web page
    print(line.decode().strip())
    # Compute frequency of each word in the retrieved web page
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

    
