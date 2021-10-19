tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    # Create new list of length 3
    col_width = [0] * len(data)
    for list in range(len(data)):                               # iterate over the lists in the data set
        for word in data[list]:                           # iterate over the words in each list
            if col_width[list] < len(word):    # Find the longest string in each of the inner lists
                col_width[list] = len(word)              # set col_width to max length of words in list
    # Display each list in a rjust(col_width) table
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(col_width[y]), end=' ')
        print()


printTable(tableData)
