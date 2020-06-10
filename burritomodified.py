class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

# setters - can call in the terminal .set_meat('steak') to change the contents of your burrito
    def set_to_go(self, to_go):
        valid_types = [True, False]
        if to_go in valid_types:
            self.to_go = to_go
        else:
            self.to_go = False

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

    def set_rice(self, rice):
        self.rice.set_value(rice)

    def set_beans(self, beans):
        self.beans.set_value(beans)

    def set_meat(self, meat):
        self.meat.set_value(meat)


# getters - can call using .get_meat() to return the value
    def get_meat(self):
        return self.meat.get_value()

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice.get_value()

    def get_beans(self):
        return self.beans.get_value()

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
        if self.meat.get_value() == 'steak':
            extras += 1.5
        elif self.meat.get_value() == False:
            extras = 0.0
        else:
            extras = 1.0
        if self.extra_meat and (self.meat.get_value() != False):
            extras += 1.0
        if self.guacamole:
            extras += 0.75
        return base_cost + extras

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False

class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)

print(a_burrito.get_meat())
print(a_burrito.get_cost())
a_burrito.set_meat('steak')
print(a_burrito.get_meat())
print(a_burrito.get_cost())
# print(a_burrito.get_rice())
# print(a_burrito.get_beans())
# print(a_burrito.get_guacamole())
# print(a_burrito.guacamole)
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

# here, we have to query the get_value() method from the meat class, since that is where the 'return'
# statement is. 'meat' passed into burrito constructor as a Meat object. Meat object has .get_value() method
# this method, when called, returns the value of the meat.value variable (which is the type of meat)
print(a_burrito.meat.get_value())

# here, we can directly query the guacamole attribute, since it is a member of the burrito class
print(a_burrito.guacamole)

# we can also use the getter for guacamole:
print(a_burrito.get_guacamole())
