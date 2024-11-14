# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:48:25 2024

@author: kayla
"""

import functools
'''
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
'''

### BEGIN SOLUTION
def sum(num1, num2):
    return (num1 + num2)
### END SOLUTION

### BEGIN SOLUTION
def square(math_function):
    square_function = math_function(1,2) * math_function(1,2)
    return square_function
### END SOLUTION

### BEGIN SOLUTION
answer = square(sum)
print(answer)
### END SOLUTION

### BEGIN SOLUTION
def outer():
    def inner():
        print("My string ^-^")
    return inner()

### END SOLUTION

### BEGIN SOLUTION
print(outer())
### END SOLUTION

### BEGIN SOLUTION
print(sum)
### END SOLUTION

### BEGIN SOLUTION
def maybe(response):
    def yes():
        return "Yes"
    def no():
        return "No"
    while True:
        if(response == True): return yes
        if(response == False): return no
        

### END SOLUTION 


### BEGIN SOLUTION
result = maybe(False)
print(result)
### END SOLUTION

### BEGIN SOLUTION
print(result())
### END SOLUTION

### BEGIN SOLUTION
from datetime import datetime
### END SOLUTION

### BEGIN SOLUTION
def papergirl(func):
    @functools.wraps(func)
    def wrapper_decorator():
        greeting = "HELLO LADIES AND GENTLEMAN, "
        # Do something before
        value = func()
        # Do something after
        value = greeting + value
        return value
    return wrapper_decorator

@papergirl
def get_day():
    today = datetime.today().weekday()
    if(today == 0): return "IT IS MONDAY"
    if(today == 1): return "IT IS TUESDAY"
    if(today == 2): return "IT IS WEDNESDAY"
    if(today == 3): return "IT IS THURSDAY"
    if(today == 4): return "IT IS FRIDAY"
    if(today == 5): return "IT IS SATURDAY"
    if(today == 6): return "IT IS SUNDAY"
    
print(get_day())
### END SOLUTION





