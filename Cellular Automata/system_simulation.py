# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:52:22 2022

@author: ADMIN
"""
from system_initialization import initial_state
from observables import density
import time

import display

N = 200
W = 254
lamb = 0.8
T = 50

start_time = time.time()

cellular_automaton = initial_state(N)

cellular_automaton_new=display.plotting(cellular_automaton, W, lamb, T)
if cellular_automaton_new!="null":
      print("Initial state: ", cellular_automaton)
      print("Updated state: ", cellular_automaton_new)
      print("initial density=", density(cellular_automaton), "\n", "final density= ",
            density(cellular_automaton_new))
print("Time to execute the simulation:", (time.time() - start_time), "seconds")