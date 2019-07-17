 # here we will see the classe of python from python3 synthax 

class Dog(): 
# Capitalize the name of the class in python
# it make it more recgnizable for others developers 
    """  A simple attempt to model a dog """

    def __init__(self,name , age): 
        """ initialize name and age attributes. """
        self.name = name 
        self.age = age 
    def sit(self):
        """ Simulate dog sitting in response to a command """
        print(self.name.title() + ' is now sitting.')
    def roll_over(self):
        """Simulate dog rolling over in a respond to a command """
        print(self.name.title() + ' is rolling over.')

# to create a classe to you to use the method __init__ 
# it initialize the class and the __ help python to not mistake the 
# classe for a function instead. 

# you can set parameters to your class
# here we set 3 parameters self,name,age
# the self pramater is required in the method definition
my_dog = Dog('willie',6)
# here we created an instance from our class Dog 
# Dog('willie',6) will init our paramater from our class Dog which are name,age 
# we defined name and age here in your brackets 

my_dog.name 
# we can access attributes like this usign the dit notation we access the value 
# of my_dog attribute by writting the synthax ABOVE 

 # calling methods 
my_dog.sit()
my_dog.roll_over()
 # here we called our functions sit and roll_over 

 # Creating multiple instance 
new_dog = Dog('lucy', 3)

print( str(new_dog) + 'is the new instance')
new_dog.roll_over()
new_dog.sit()
# dont forget to the methods str to converrt number in string when 
# you need to print 
# new_dog is called an instance 

"""  you can make as any instance you want 
if they gave different varabile's name """

"""
Class  represent objects then inside those classes you ll find 
Instances. 
Instances are like the parameter of the class
"""

# Lets write a class representing a car 
# our class will store information about the kind 

class Car(): 
    """ a simple attempt to represent a car """
    def __init__(self, make, model, year):
        """ initialize attributesto describe a car """ 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted desriptive name """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ print a statement showing the cars mileage """ 
        print("this car mileage " + str(self.odometer_reading) + "miles on it")
        
my_new_car = Car('audi ', 'a4 ', 2016 )
print(my_new_car.get_descriptive_name())

# setting a default value for an attribute

