# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:17 2024

@author: romas
"""


import matplotlib.pyplot as plt


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
        
        ax.text(self.x[-1]/2, self.y[1], text, fontsize = 14)
        
        ax.legend()
        
        ax.grid(True)
        
        return ax
 
 