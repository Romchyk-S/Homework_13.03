# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:10:24 2024

@author: romas
"""
import math as m

import numpy as np

def find_x_piecesewise_for_periodic_functions(a: float|int, b: float|int, period: float|int,
                                              zero_left: float|int, zero_right: float|int, x: np.ndarray):

    
    x_pieces = []
    
    if a < 0:
        
        n_range = range(m.ceil((a)/period), m.ceil((b)/period)+1)
        
    else:
        
        n_range = range(m.ceil((b)/period)+1)
        
     
    if a > zero_left:
        
        iterations = m.ceil(a/zero_left)
        
        zero_left *= iterations
        
        zero_right *= iterations
    
    for n_1 in n_range:
        
        zero_multiply = n_1/abs(n_1) if n_1 != 0 else 0
        
        period_multiply = (n_1-1) if n_1 > 1 else 0
        
        try:
            
            x_pieces[0] = np.logical_or(x_pieces[0], ((x >= zero_multiply*zero_left+period_multiply*period) & 
                                                      (x <= zero_multiply*zero_right+period_multiply*period)))

        except IndexError:
           
           x_pieces.append((x >= zero_multiply*zero_left+period_multiply*period) & 
                           (x <= zero_multiply*zero_right+period_multiply*period))
    
    x_pieces.append(np.logical_not(x_pieces[0]))
    
    return x_pieces
