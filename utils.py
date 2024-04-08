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


def cylinder_volume(radius, height, pi = 3.14):
    '''This function calculates the volume of a cylinder.'''
    V = radius ** 2 * height * pi
    print("cylinder_volume =", V)
    return V

radius = r
height = 18
print(cylinder_volume (r, height))

def ms2kmh (ms): 
    '''This function converts speed from meters per second to kilometers per hour.'''
    return ms*3.6

velocity = (1,5,10,15,30)

for i in velocity:
    print(ms2kmh(i))
