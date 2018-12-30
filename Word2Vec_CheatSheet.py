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

# subtracting vectors
def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]
subtractv([10, 1], [5, 2])

# adding vectors
def addv(coord1, coord2):
    return [c1 + c2 for c1, c2 in zip(coord1, coord2)]
addv([10, 1], [5, 2])
    
# get the mean
def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0]) # creating list of zeros 
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean

meanv([[0, 1], [2, 2], [4, 3]])

# testing
# ==================================================================================
# # distance from "red" to "green" is greater than the distance from "red" to "pink"
# distance(colors['red'], colors['green']) > distance(colors['red'], colors['pink']) 
# ==================================================================================

# Calculating "closest neighbors"
def closest(space, coord, n=10):
    closest = []
    for key in sorted(space.keys(),
                        key=lambda x: distance(coord, space[x]))[:n]:
        closest.append(key)
    return closest

# test
# =============================================================================
# closest(colors, colors['red'])
# closest(colors, [150, 60, 150])

# closest match for two colors subtracted with each other    
# closest(colors, subtractv(colors['purple'], colors['red']))
  
# closest match for two colors added together    
# closest(colors, addv(colors['blue'], colors['green']))
    
# the average of black and white: medium grey
# closest(colors, meanv([colors['black'], colors['white']]))
    
# an analogy: pink is to red as X is to blue
# pink_to_red = subtractv(colors['pink'], colors['red'])
# closest(colors, addv(pink_to_red, colors['blue']))
    
# another example: 
# navy_to_blue = subtractv(colors['navy'], colors['blue'])
# closest(colors, addv(navy_to_blue, colors['green']))
# =============================================================================
    

    

    
    






