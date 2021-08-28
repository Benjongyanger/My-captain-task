# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:13:06 2021

@author: Ben
"""

# each occurrence frequency using
# naive method

# initializing string
test_str = "Mississippi"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print ("Count of all characters in Mississippi is :\n "
										+ str(all_freq))
