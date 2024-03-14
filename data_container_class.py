# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:17 2024

@author: romas
"""


import matplotlib.pyplot as plt

import numpy as np
    
    

class DataContainer:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def plot(self, fig=None, ax=None, title = "My preferred title", text="ОВ", **kwargs):
        
        if fig is None:
            
            fig = plt.gcf()
            
        if ax is None:
            
            ax = plt.gca()
            
        # при передачі **kwargs в функцію plot відбувається розпакування key, value зі словника
        print('Надрукуємо словник kwargs', kwargs)
        
        print()

        ax.plot(self.x, self.y, **kwargs)
        
        ax.set_xlabel('x', fontsize=12)
        
        ax.set_ylabel('y', fontsize=12)
        
        ax.set_title(title)
        
        x_i = -1
        
        a = self.x[x_i]/2
        
        while np.isnan(a):
            
            a = self.x[x_i]/2
            
            x_i -= 1
            
            
        y_i = 1
        
        b = self.y[y_i]
        
        while np.isnan(b):
            
            b = self.y[y_i]
            
            y_i += 1
        
        ax.text(a, b, text, fontsize = 14)
        
        ax.legend()
        
        ax.grid(True)
        
        return ax
 
 