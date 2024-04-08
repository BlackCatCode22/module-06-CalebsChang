class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.name=z
        print(self.name,"constructed")
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    def __del__(self):
        print('I am destructured', self.x)

s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
s.party()
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)