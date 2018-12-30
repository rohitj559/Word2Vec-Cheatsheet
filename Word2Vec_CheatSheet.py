# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:00:48 2018

@author: Rohit
"""

# Loading the JSON data
import json
color_data = json.loads(open("xkcd.json").read())

# function to convert colors from hex format (#1a2b3c) to a tuple of integers
def hex_to_int(s):
    s = s.lstrip("#")
    return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)

# create a dictionary and populate it with mappings from color names to RGB vectors for each color in the data
colors = dict()
for item in color_data['colors']:
    colors[item["color"]] = hex_to_int(item["hex"])   


# testing   
# =============================================================================
# print(colors['olive'])
# print(colors['red'])
# print(colors['black'])
# =============================================================================
    
# function to get the Euclidean distance between two points
import math
def distance(coord1, coord2):
    # note, this is VERY SLOW, don't use for actual code
    return math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))

# testing
# =============================================================================
# print(distance([10, 1], [5, 2]))
# =============================================================================
    





