"""
Created on Fri Oct 21 11:28 2022

@author: ADMIN
"""
import numpy as np
from system_initialization import initial_state
from observables import density

def binary_code(wolfram_number):
    binary = format(wolfram_number, 'b')
    binary = list(binary)
    binary = np.array(binary)
    binary = binary.astype('int')
    
    length = binary.size
    if length < 8:
        insertions = np.zeros(8-length)
        binary = np.insert(binary, 0, insertions)          
    return binary
    
def wolfram_update_rule(system, wolfram_number, i):
    system_size = len(system)
    initial_element = system[i]
    
    if i-1<0:
        left_neighbour = system[system_size-1]
    else:
        left_neighbour = system[i-1]
    if i+1 > system_size-1:
        right_neighbour = system[0]
    else:    
        right_neighbour = system[i+1]
    
    if left_neighbour == 1 and initial_element == 1 and right_neighbour == 1:
        new_element = binary_code(wolfram_number)[0]
    if left_neighbour == 1 and initial_element == 1 and right_neighbour == 0:
        new_element = binary_code(wolfram_number)[1]
    if left_neighbour == 1 and initial_element == 0 and right_neighbour == 1:
        new_element = binary_code(wolfram_number)[2]    
    if left_neighbour == 1 and initial_element == 0 and right_neighbour == 0:
        new_element = binary_code(wolfram_number)[3]
    if left_neighbour == 0 and initial_element == 1 and right_neighbour == 1:
        new_element = binary_code(wolfram_number)[4]
    if left_neighbour == 0 and initial_element == 1 and right_neighbour == 0:
        new_element = binary_code(wolfram_number)[5]  
    if left_neighbour == 0 and initial_element == 0 and right_neighbour == 1:
        new_element = binary_code(wolfram_number)[6]
    if left_neighbour == 0 and initial_element == 0 and right_neighbour == 0:
        new_element = binary_code(wolfram_number)[7]  
    
    return new_element

def system_update(system, wolfram_number):
    system_size = system.size
    new_system = np.array([])
    for i in range(system_size):
        new_element = wolfram_update_rule(system, wolfram_number, i)
        new_system = np.append(new_system, new_element)
    return new_system

# W = 204
# cellular_automaton = initial_state(10000)
# cellular_automaton_new = system_update(cellular_automaton, W)

# print("The update rule is: ", binary_code(W))
# print("Initial state: ", cellular_automaton)
# print("Updated state: ", cellular_automaton_new)
# print("initial density=", density(cellular_automaton), "\n", "final density= ",
#       density(cellular_automaton_new))



