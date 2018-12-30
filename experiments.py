# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:49:36 2018

@author: Rohit
"""

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