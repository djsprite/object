class Pet:
    """ This is the beginning of a class for the humble house fish 
    Attributes: can swim really fast
        Harold
        5

    """
    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight

    def add_weight(self, weight):
        self.weight = weight

    def get_name(self):
        return self.name
    

class Fish(Pet):
    """ Fish inherits from Pet """
    def speak(self, voice = 'bubble bubble bubble'):
        # print('bubble')
        return voice

f = Fish('Harold', 5)
namex = f.get_name()
whatItSays = f.speak()
print(whatItSays)


x = Fish('Gerald', 7)

fishiefriend = Fish("Friend")

x.add_weight(7)
f.add_weight(5)

print(f.name)

print(x.name)

#Class Child(Parent):
#  __init__(self, name, play):
#    self.name = name
#    self.playLikeAKid = play

print(namex)

#x.can swim really fast()
#print(f.foodDishLevel)
#print(x.foodDishLevel)
