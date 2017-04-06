class pet:

    number_of_legs = 4
    
    def __init__(self,name):
        self.name=name

    def sound(self):
        pass
        
class dog(pet):
    def sound(self):
      return ("woof!")

class cow(pet):
    def sound(self):
        return ("moooo!")

class puppy(pet):
     def sound(self):
      return ("woof woof!")
          

pet=[dog('mary'),cow("jave"),puppy("jerry")]
              
for pet in pet:
    print( pet.name +" : "+ pet.sound())             
              

d = puppy("jerry")

print ("Pet has %s legs." %d.number_of_legs)
