# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:31:31 2022

@author: ADMIN
"""
import numpy as np

def density(array):
    p = np.sum(array)/array.size
    return p