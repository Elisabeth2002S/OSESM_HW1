# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:55:34 2024

@author: Elisabeth Seifried
"""

def triangular_surface_area (s, h):  
    '''This function calculates the surface area of a triangle.'''
    A = s * h /2
    print("triangular_surface_area =", A)
    return A

s = 2.8
h = 4

triangular_surface_area (s,h)

def circular_surface_area (radius, pi = 3.14):
    '''This function calculates the surface area of a circle.'''
    A = radius **2 *pi
    print("circular_surface_area =", A)
    return A

r = 18

circular_surface_area (r)

#def mean(numbers): 
#    '''This function calculates the mean of a list of numbers.
#    Parameters:
#        numbers (list): A list of numeric values.
#    Returns:
#        float: The mean (average) of the input numbers.'''
#    return print("mean =", sum(numbers)/len(numbers))


#a = (1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,19,18)

#mean(a)

def ms2kmh (ms): 
    '''This function converts speed from meters per second to kilometers per hour.'''
    return ms*3.6

velocity = (1,5,10,15,30)

for i in velocity:
    print(ms2kmh(i))





