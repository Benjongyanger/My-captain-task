# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:50:38 2021

@author: Ben
"""

# Python program to print positive Numbers in a List
 
# list of numbers
list1 = [12, -7, 5, 64, -14]
 
# iterating each number in list
for num in list1:
     
    # checking condition
    if num >= 0:
       print(num, end = " ")
       
       
       
       
       # Python program to print positive Numbers in a List
 
# list of numbers
list1 = [12, 14, -95, 3]
num = 0
 
# using while loop     
while(num < len(list1)):
     
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = " ")
     
    # increment num 
    num += 1