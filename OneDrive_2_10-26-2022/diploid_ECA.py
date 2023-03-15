# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:33:08 2022

@author: ADMIN
"""
import numpy as np
from wolfram_classes import wolfram_update_rule, binary_code
from system_initialization import initial_state
from observables import density



def diploid_update_rule(system, wolfram_number, weight):
    system_size = len(system)
    new_system = np.array([])
    for i in range(system_size):
        if np.random.random() < weight:
            new_element = wolfram_update_rule(system, wolfram_number, i)
        else:
            new_element = 0
        new_system = np.append(new_system, new_element)
    return new_system

def diploid_simulation(system, wolfram_number, weight, iterations):
    print("Update rule is: ", binary_code(wolfram_number))
    for i in range(iterations):
        system = diploid_update_rule(system, wolfram_number, weight)
        i = i+1
    return system

# cellular_automaton = initial_state(10000)
# cellular_automaton_new = diploid_simulation(cellular_automaton, 28, 0.8, 5)

# print("Initial state: ", cellular_automaton)
# print("Updated state: ", cellular_automaton_new)
# print("initial density=", density(cellular_automaton), "\n", "final density= ",
#       density(cellular_automaton_new))