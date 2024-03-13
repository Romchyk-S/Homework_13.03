# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:15:11 2024

@author: romas
"""
import functions_to_plot as ftp

import data_container_class as dcc

import inspect as insp

import matplotlib.pyplot as plt

import math as m


def fill_arr(array: list, to_be_plotted: list):
    
    if len(array) < len(to_be_plotted):
        
        elms_to_add_num = abs(len(array)-len(to_be_plotted))
        
        if len(array) < m.floor(len(to_be_plotted)/2):
            
            multiple = (m.floor(len(to_be_plotted)/2*len(array))) 
            
            array = array*multiple
        
        elms_to_add = array[:elms_to_add_num]
        
        new_array = [elm for elm in array + elms_to_add]
        
    else:
        
        new_array = array
        
    return new_array


colors = ['green', 'darkcyan', 'blue', 'magenta', 'red', 'purple', 'orange']

markers = ['o', '^', '.', ',', 'v', '>', '<', '1', '2', '3']

linestyles = ['solid', 'dotted', 'dashed', 'dashdot']

linewidth, marker_size = 1, 0

to_be_plotted = insp.getmembers(ftp, insp.isfunction)

colors = fill_arr(colors, to_be_plotted)

markers = fill_arr(markers, to_be_plotted)

linestyles = fill_arr(linestyles, to_be_plotted)

for func, color, marker, linestyle in zip(to_be_plotted, colors, markers, linestyles):
    
    x, y, text, title = func[1]()
    
    data = dcc.DataContainer(x, y)
    
    fig, axis = plt.subplots(1, 1, layout="constrained", figsize=(10,6))
    
    data.plot(fig=fig, ax=axis, color=color, marker=marker, linestyle=linestyle, linewidth=linewidth, 
              markersize=marker_size, label=title, title=title, text = text)

    plt.show()
    
    linewidth += 0.1
    
    marker_size += 1
     