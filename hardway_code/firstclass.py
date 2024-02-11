
class Song(object):

#self in this function indicates the variable belongs to this class
    def __init__(self,lyrics):
        self.lyrics = lyrics
#self in this function indicates the function belongs to this class
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    

#The object of the type Song Class is created 
happy_bday = Song(["Happy B'day to you.",
"I don't want to get sued.", 
"I will stop here."])

#The object of the type Song Class is created
bulls_on = Song(["They rally around the family",
"With pockets full of shells."])

my_lyrics = ["I went on ride",
"To hide my Pride",
"Those who wait for the Tide",
"For sure wont get the ride"]

ride = Song(my_lyrics)

#The method of the Song Class is executed
happy_bday.sing_me_a_song()
bulls_on.sing_me_a_song()

print("Something that I wrote")

ride.sing_me_a_song()

print("User, why not you give me an input??")

ready = input("> ")

if 'yes' in ready:
    print("Okay, now thats swell...")
    lines = input("How many lines> ")
    users = []
    for line in range(int(lines)):
        get_input = input("Go on Type it> ")
        users.append(get_input)
    print('Thanks and here is...')

    user_in = Song(users)

    user_in.sing_me_a_song()

elif 'next time' in ready:
    print("I will be around..")

else:
    print("Don't be shy, I won't share it with your girlfriend")