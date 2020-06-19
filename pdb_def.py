# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:30:23 2019

@author: Rishab
"""
import numpy as np
import itertools
# assuming a case where number of disks = 7 
ll = [[0,5,6,7]] # Lets simplify the problem and take a subset of variables
all_states = ([list(itertools.permutations(item,len(item))) for item in ll]) # getting all possible combinations as states for an individual peg
all_states_sorted= sorted(all_states) 
all_states = [list(all_states_sorted for all_states_sorted,_ in itertools.groupby(all_states_sorted))] # removing duplicate states
#all_states = [list(tupl) for tupl in {tuple(item) for item in all_states}]
#d1_arr = np.zeros((10000,100000))
#for i in range(0,20):
#   for j in range(0,20):
#        for k in range(0,20):
#            for l in range(0,20):
#                d1_arr[i,j,k,l] = np.sum(abs(abs(abs((np.asarray(all_states[0][0][i])) - np.asarray(all_states[0][0][i])) - np.asarray(all_states[0][0][i])) - np.asarray(all_states[0][0][i])))         
class A(object):# calculating cost function 
    def cost_distance(state):
        d1_arr = abs(abs(abs((state[0]) - (state[1])) - (state[2])) - (state[3]))
        d1 = np.sum(d1_arr)
        print(d1)
        d2 = 0 
        for i in state[:,3]:
            get_index = np.where(state[:,(0,1,2)] == i)
            n = get_index[1][0]
            print(n)
            d2 = d2 +n
            print(d2)
        d = d1 +d2
        

