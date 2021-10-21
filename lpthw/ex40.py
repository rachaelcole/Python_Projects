class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)


happy_bday_lyrics = ["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]
bulls_on_parade_lyrics = ["They rally around tha family", "With pockets full of shells"]

happy_bday = Song(happy_bday_lyrics)
bulls_on_parade = Song(bulls_on_parade_lyrics)

happy_bday.sing()
bulls_on_parade.sing()
