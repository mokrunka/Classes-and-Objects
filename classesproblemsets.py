class Dog:
     def __init__(self, name = "", owner = None):
         self.name = name
         self.owner = owner
     def speak(self):
         print("WOOF!")

class Owner:
     def __init__(self, name):
         self.name = name
     def speak(self):
         print("My name is:", name)

owner = Owner('bob')
doggo = Dog('buck', owner)

print(owner.name)
print(doggo.owner.name)
print(doggo.name)

##############

# fido = Dog("Fido", Owner('bob'))
#
# # since the Dog class has been passed the Owner class as it's owner argument, the .name method
# # from the Owner class is available
# print(fido.owner.name)
# print(fido.name)