#allows objects to be treated as instances of the parent class
#makes it possible to use a single interface
#for different underlying conditions
#method overriding

class Bird:
    def sound(self):
        return "some generic bird sound"

class Parrot(Bird):
  def __init__(self,name):
      self.name = name

  def sound(self):
      return "squawks"

class Sparrow(Bird):
    def sound(self):
        return "chirps"

par1 = Parrot("parrot")
print(par1.sound())
sp1 = Sparrow()
print(sp1.sound())

