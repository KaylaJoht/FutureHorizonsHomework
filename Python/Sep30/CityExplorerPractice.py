# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:29:18 2024

@author: kayla
"""
character = {'energy':50, 'money': 0, 'inventory':[]}
print(character)

city_layout = [
{'block': 0, 'name': 'Downtown', 'places': [
    {'name': 'Park', 'items': ['Frisbee', 'Sunscreen'], 'money': 10},
    {'name': 'Cafe', 'items': ['Coffee', 'Pastry'], 'money': 15},
    {'name': 'Bookstore', 'items': ['Book', 'Notebook'], 'money': 5}
]},

{'block': 1, 'name': 'Residential Area', 'places': [
    {'name': 'Supermarket', 'items': ['Groceries', 'Snacks'], 'money': 20},
    {'name': 'Gym', 'items': ['Protein Shake', 'Towel'], 'money': 8},
    {'name': 'Library', 'items': ['Novel', 'Magazine'], 'money': 3}
]}]



places = city_layout[0]['places']
for i,loc in enumerate(places):
    print(places[i]['name'])
#print(places[0]['name'])

items = places[0]['items']
cnt = len(items)
print(items)
print(cnt)
character['energy'] -= cnt

for thing in items:
    character['inventory'].append(thing)
print(character)

places[0]['items'] = ""
print(places[0]['items'])