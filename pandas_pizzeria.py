# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:45:07 2024

@author: kayla
"""

import os
import pandas as pd

orders, order_details, pizzas, pizza_types = None, None, None, None
absolute_path = os.path.abspath(os.path.dirname('archive'))

# This is for JH filesystem. It may be different on your computer.
orders = pd.read_csv(absolute_path + '/archive/orders.csv', encoding='latin-1')

### BEGIN SOLUTION
order_details = pd.read_csv(absolute_path + '/archive/order_details.csv', encoding='latin-1')
pizza_types = pd.read_csv(absolute_path + '/archive/pizza_types.csv', encoding='latin-1')
pizzas = pd.read_csv(absolute_path + '/archive/pizzas.csv', encoding='latin-1')
### END SOLUTION

### BEGIN SOLUTION
print(orders.head(10))
### END SOLUTION

### BEGIN SOLUTION
print(order_details.head(10))
### END SOLUTION

### BEGIN SOLUTION
print(pizzas.head(10))
### END SOLUTION

### BEGIN SOLUTION
print(pizza_types)
### END SOLUTION

print(pizza_types.loc[29])
#ANSWER = spin_pesto


merged_data = None

### BEGIN SOLUTION
merged_data = order_details.merge(orders)
merged_data = merged_data.merge(pizzas)
merged_data = merged_data.merge(pizza_types)
### END SOLUTION

print(merged_data)


### BEGIN SOLUTION
print(merged_data['category'].value_counts())
### END SOLUTION

### BEGIN SOLUTION
print(merged_data['size'].value_counts())
### END SOLUTION

print(merged_data[['category', 'size']].value_counts())

#ANSWER = based on the data it's 'Classic Large' but if you run merged_data[['category', 'size']].value_counts(), you discover that it's classic small.

# Overview of tasks in this cell (each can be done in one line of code):
# 1. Convert the 'date' column to a datetime object
# 2. Convert the 'time' column to a datetime.dt.time object using `format='%H:%M:%S'` to specify the format.
#   - Include .dt.time to get the time component of the datetime object (e.g. 12:30:00)
# 3. Create a new column called 'datetime' that combines the 'date' and 'time' columns (as strings - use the `.astype()` method)

### BEGIN SOLUTION
merged_data['date'] = pd.to_datetime(merged_data['date'])
merged_data['time'] = pd.to_datetime(merged_data['time'], format = '%H:%M:%S').dt.time
merged_data['datetime'] = merged_data['date'].astype(str) + " " + merged_data['time'].astype(str)
merged_data['datetime'] = pd.to_datetime(merged_data['datetime'])

### END SOLUTION

print(merged_data)


### BEGIN SOLUTION
merged_data['weekday'] = merged_data['date'].dt.day_name()
### END SOLUTION

print(merged_data)


### BEGIN SOLUTION
print(merged_data.info())
### END SOLUTION


### BEGIN SOLUTION
print(merged_data.isnull().sum())
### END SOLUTION

#ANSWER = 4, and no nulls

### BEGIN SOLUTION
print(merged_data.describe())
### END SOLUTION

### BEGIN SOLUTION
print(merged_data.describe(include='all'))
### END SOLUTION

### BEGIN SOLUTION
days = merged_data[['weekday', 'order_id']].groupby(['weekday']).nunique()
print(days)
print(f"Monday: {days.loc['Monday']['order_id']} orders.")
print(f"Tuesday: {days.loc['Tuesday']['order_id']} orders.")
print(f"Wednesday: {days.loc['Wednesday']['order_id']} orders.")
print(f"Thursday: {days.loc['Thursday']['order_id']} orders.")
print(f"Friday: {days.loc['Friday']['order_id']} orders.")
print(f"Saturday: {days.loc['Saturday']['order_id']} orders.")
print(f"Sunday: {days.loc['Sunday']['order_id']} orders.")
### END SOLUTION

### BEGIN SOLUTION
hours = pd.DataFrame(merged_data['datetime'].dt.hour)
hours['order_id'] = merged_data['order_id']
print(hours.groupby(['datetime']).nunique())
### END SOLUTION


### BEGIN SOLUTION
print(merged_data[['date', 'order_id']].groupby(['date']).nunique().mean())
### END SOLUTION


### BEGIN SOLUTION
sold = merged_data[['pizza_type_id', 'quantity']].groupby(['pizza_type_id']).sum()
sold = sold.sort_values(by='quantity', ascending=False)
print(sold)
print(sold.head())
print(sold.tail())

sold_price = merged_data[['pizza_type_id', 'quantity', 'price']]
sold_price['quantity x price'] = sold_price['quantity'] * sold_price['price']
sold_price = sold_price[['pizza_type_id', 'quantity x price']].groupby(['pizza_type_id']).sum()
sold_price = sold_price.sort_values(by='quantity x price', ascending=False)
print(sold_price)
print(sold_price.head())
print(sold_price.tail())
### END SOLUTION

### BEGIN SOLUTION
print(sold_price['quantity x price'].sum())
### END SOLUTION


### BEGIN SOLUTION
print(merged_data['date'].value_counts().head())
print(merged_data['date'].value_counts().tail())
### END SOLUTION


### BEGIN SOLUTION
print(merged_data['date'].dt.month.value_counts())
### END SOLUTION