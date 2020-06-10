#Write a class called "Burrito". A Burrito should have the
#following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
#The constructor should let any of these attributes be
#changed when the object is instantiated. The attributes
#with a default value should be optional. Both positional
#and keyword attributes should be in the order shown above
#(for the autograder to work).

class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def set_meat(self, meat):
        valid_types = ['chicken', 'pork', 'steak', 'tofu', False]
        if meat in valid_types:
            self.meat = meat
        else:
            self.meat = False

    def set_to_go(self, to_go):
        valid_types = [True, False]
        if to_go in valid_types:
            self.to_go = to_go
        else:
            self.to_go = False

    def set_rice(self, rice):
        valid_types = ['white', 'brown', False]
        if rice in valid_types:
            self.rice = rice
        else:
            self.rice = False

    def set_beans(self, beans):
        valid_types = ['black', 'pinto', False]
        if beans in valid_types:
            self.beans = beans
        else:
            self.beans= False

    def set_extra_meat(self, extra_meat):
        valid_types = [True, False]
        if extra_meat in valid_types:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_guacamole(self, guacamole):
        valid_types = [True, False]
        if guacamole in valid_types:
            self.guacamole = guacamole
        else:
            self.guacamole = False

    def set_cheese(self, cheese):
        valid_types = [True, False]
        if cheese in valid_types:
            self.cheese = cheese
        else:
            self.cheese = False

    def set_pico(self, pico):
        valid_types = [True, False]
        if pico in valid_types:
            self.pico = pico
        else:
            self.pico = False

    def set_corn(self, corn):
        valid_types = [True, False]
        if corn in valid_types:
            self.corn = corn
        else:
            self.corn= False

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

    def get_cost(self):
        base_cost = 5.00
        extras = 0
        if self.meat == 'steak':
            extras += 1.5
        elif self.meat == False:
            extras = 0.0
        else:
            extras = 1.0
        if self.extra_meat and (self.meat != False):
            extras += 1.0
        if self.guacamole:
            extras += 0.75
        return base_cost + extras


#The code below will test your class. If it is written
#correctly, this will print True, then False. Note,
#though, that we'll test your code against more complex
#test cases when you submit.
# newBurrito = Burrito("poop", True, True, True)
# print(newBurrito.to_go)
# print(newBurrito.guacamole)
# print(newBurrito.meat)
# print(newBurrito.to_go)
# print(newBurrito.meat)

a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.meat)
print(a_burrito.get_meat())
print(a_burrito.extra_meat)
print(a_burrito.get_cost())
print(a_burrito.beans)
print(a_burrito.rice)
print(a_burrito.get_rice())