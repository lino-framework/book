# class inheritance

class Vehicle(object):
    number_of_wheels = None

    def get_speed(self):
        """Return the maximum speed."""
        raise NotImplementedError
    
class Bike(Vehicle):
    number_of_wheels = 2
    
    def get_speed(self):
        return 20
    
    
class Car(Vehicle):
    brand = None
    number_of_wheels = 4
    
    def get_speed(self):
        return 90
    

class Benz(Car):
    star_logo = True
    brand = "Mercedes"

class OldBenz(Benz):
    star_logo = False
    
    def get_speed(self):
        return super(OldBenz, self).get_speed() - 20
        # super_object = super(OldBenz, self)
        # print type(super_object)
        # meth = super_object.get_speed
        # speed = meth()
        # return speed - 20

class VW(Car):
    brand = "Volkswagen"

class VW(VW):
    diesel = False

x = OldBenz()
print x.number_of_wheels
print x.get_speed()

    

"""
>>> my = VW()
>>> print my.number_of_weels
4
>>> print my.diesel
False

>>> print my.star_logo
AttributeError: no attribute 'star_logo'

"""

