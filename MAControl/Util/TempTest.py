import numpy as np
import operator
import argparse
import random
import math
import os
import matplotlib.pyplot as plt
import MAControl.Util.SignIsSame as sis
import MAEnv.scenarios.TargetProfile as T
import MAControl.Util.get_random_state as rs

# --evolve --test

# plt.rcParams['figure.dpi'] = 800
# curdir = os.path.dirname(__file__)
# pardir = os.path.dirname(os.path.dirname(curdir))
# data = np.loadtxt(pardir + '/cost.txt')
# plt.figure()
# line = plt.gca()
# line.plot(data[:, 0], data[:, 1], 'c--')
# # plt.xlim(0, 4000)
# plt.show()

# uav_pos = np.array([1, 1])
# tar_pos = np.array([1, 2])

# curdir = os.path.dirname(__file__)
# pardir = os.path.dirname(os.path.dirname(curdir))
# target = np.loadtxt(pardir + '/track/target_attacking.txt')

gen = 2
ind = 5
collect = 3
uav_num = 5

r_state = rs.RandomState(collect, uav_num)

for g in range(gen):
    for i in range(ind):
        for c in range(collect):
            for u in range(uav_num):
                pos, vel = r_state.get_state(c, u)
                print('gen ', g, 'ind ', i, 'coll ', c, 'uav ', u, pos, vel)
            print('\n')
        print('\n\n')
    print('\n\n\n')




pass
