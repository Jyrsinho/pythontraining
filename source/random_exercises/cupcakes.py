from gettext import npgettext
from time import perf_counter

import numpy as np


data = np.array([[174, 94], [189, 87], [185, 110],
                 [195, 104], [149, 61], [189, 104],
                 [147, 92], [154, 111], [167, 67], [175, 79]])

A = np.array([[-4,2,1], [0,2,6], [5,12,9]])
print(A)
rivisummat =  np.sum(A[:,0] + np.sum(A[:,1]) + np.sum(A[:,2]))
print(rivisummat)


