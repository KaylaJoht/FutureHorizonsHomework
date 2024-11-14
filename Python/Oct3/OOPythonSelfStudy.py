# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:52:43 2024

@author: kayla
"""
import nbformat
import unittest
from unittest.mock import patch

### BEGIN SOLUTION
class Person:
    def  __init__(self, name, age):
       self.name = name
       self.age = age
    def greet(self):
        print(f"Hello, {self.name}")
        
        
me = Person("Kayla", 24)
me.greet()
### END SOLUTION


### BEGIN SOLUTION
class Person:
    def  __init__(self, name, age):
       self.name = name
       self.__age = age
    def greet(self):
        print(f"Hello, {self.name}")
        
    def get_age(self):
        return self.__age
    
me = Person("Kayla", 24)
print(me.get_age())
### END SOLUTION



### BEGIN SOLUTION
class Animal:
    name = "name"
    sound = "sound"
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(f"The {self.name} says {self.sound}")
        
        
class Dog(Animal):
    breed = "breed"
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
    def make_sound(self):
        print(f"The {self.breed} {self.name} says {self.sound}")
        
        
cat = Animal("Cat", "Meow")
cat.make_sound()

dog = Dog("Dog", "Woof", "Dalmation")
dog.make_sound()
### END SOLUTION





