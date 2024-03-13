# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

import find_x_for_piecewise as fp

def func_0():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x_1 = 1, x_2 = -1$"
    
    title = "$x^2-1$"
    
    return x, x**2-1, label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x=3$"
    
    title = "$(x^2-5x+6)/(x-2)$"
    
    y = (np.piecewise(x, [(x < 1.99), ((x >= 1.99) & (x <= 2.01)), (x>2.01)],
                          [lambda x: (x**2-5*x+6)/(x-2), np.nan, lambda x: (x**2-5*x+6)/(x-2)]))
    
    return x, y, label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$no \ zeros$"
    
    title = "$2^{3x-1}$"
    
    return x, 2**(3*x-1), label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)
    
    label = "$x=3$"
    
    title = "$log_2 ((2x-1)/(x+2))$"
    
    y = (np.piecewise(x, [(x < -2), ((x >= -2) & (x <= 0.5)), (x>0.5)],
                          [lambda x: np.log2((2*x-1)/(x+2)), np.nan, lambda x: np.log2((2*x-1)/(x+2))]))
    
    return x, y, label, title

# def func_4():
    
#     x = np.arange(-10, 10, 0.1)
    
#     label = "$x_1 = 4 \ \ x_2 = 2$"
    
#     title = "$log_{1/2} (x^2-6x+9)$"
    
#     y = (np.piecewise(x, [(x < 2.99), ((x >= 2.99) & (x <= 3.01)), (x>3.01)],
#                           [lambda x: np.emath.logn(1/2, x**2-6*x+9), np.nan, lambda x: np.emath.logn(1/2, x**2-6*x+9)]))
    
#     return x, y, label, title

# def func_5():
    
#     label = "$x=\pi_n$"
    
#     title = "$sin^2(x)$"
    
#     x = np.arange(-4*np.pi, 4*np.pi, 0.1)
    
#     return x, np.sin(x)**2, label, title

# def func_6():
    
#     # здається, не працює для проміжків із від'ємними значеннями x.
    
#     a = 0
    
#     b = 4*np.pi
    
#     x = np.arange(a, b, 0.01)
    
#     period = np.pi

#     zero_left = (np.pi-0.01)
    
#     zero_right = (np.pi+0.01)
   
#     x_pieces = fp.find_x_piecesewise_for_periodic_functions(a, b, period, zero_left, zero_right, x)
    
#     y_pieces = [np.nan, lambda x: np.sin(x) + (1/np.sin(x))]

#     y = (np.piecewise(x, x_pieces, y_pieces))
    
#     label = "$no \ zeros$"
    
#     title = "$sinx + 1/sinx$"

#     return x, y, label, title

# def func_7():
    
#     # здається, не працює для проміжків із від'ємними значеннями x.
    
#     a = 0
    
#     b = 4*np.pi
    
#     x = np.arange(a, b, 0.01)
    
#     period = np.pi

#     zero_left = (np.pi-0.01)
    
#     zero_right = (np.pi+0.01)
   
#     x_pieces = fp.find_x_piecesewise_for_periodic_functions(a, b, period, zero_left, zero_right, x)
    
#     y_pieces = [np.nan, lambda x: np.sin(x) - (1/np.sin(x))]

#     y = (np.piecewise(x, x_pieces, y_pieces))
    
#     label = "\frac{\pi}{2} + \pi_n$"
    
#     title = "$sinx - 1/sinx$"
  
#     return x, y, label, title