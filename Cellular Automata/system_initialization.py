# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:55:56 2022

@author: ADMIN
"""
import numpy as np

def initial_state(system_size):
    system = np.zeros(system_size)
    for i in range(system_size):
        if np.random.random() > 0.5:
            system[i] = 1
    return system
    