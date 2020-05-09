import numpy as np
import os
import matplotlib.pyplot as plt

curdir = os.path.dirname(__file__)
pardir = os.path.dirname(os.path.dirname(curdir))

score = np.loadtxt(pardir + '/GeneticAlgorithm/evolve_process.txt')

gen, ind = score.shape

plt.rcParams['figure.dpi'] = 200
plt.figure()
line = plt.gca()

plt.fill_between(range(0, gen), score[:, 0], score[:, -1], facecolor='g', alpha=0.1)
line.plot(range(0, gen), score[:, 0], color='g')
# for i in range(ind):
#     line.plot(range(0, gen), score[:, i], color='g')

font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 13}
plt.xlabel('generation', font)
plt.ylabel('fitness score', font)
plt.grid()
plt.savefig('evolve.png')
plt.show()
