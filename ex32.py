# Modules, Classes, and Objects

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!\n")


thing = MyStuff()
thing.apple()
print(thing.tangerine)

####################################

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells\n"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

########################################

class Music():
    def __init__ (self, lyrics):
        self.lyrics = lyrics
        for line in self.lyrics:
            print(line)


pray_for_me = Music(["Who gon' pray for me?",
                     "Take my pain for me?",
                     "Save my soul for me?",
                     "'Cause I'm alone, you see",
                     "If I'm gon' die for you",
                     "If I'm gon' kill for you",
                     "Then I'll spill this blood for you.\n"])

past_lives = Music(["Past lives",
                    "Couldn't ever hold me down",
                    "Lost lives",
                    "Is sweeter when it's finally found",
                    "I've got the strangest feeling",
                    "This isn't out first time around."])
