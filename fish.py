class Fish:
    """ This is the beginning of a class for the humble house cat """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight


c = Cat('Harold')


x = Cat('Gerald')

print(c.name)

print(x.name)
