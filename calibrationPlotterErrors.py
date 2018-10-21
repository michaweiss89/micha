import os
import numpy as np
import matplotlib.pyplot as plt
import math as mt
import scipy.signal
import pandas as pd
from itertools import compress


def read_data(path, Hlength = 1):
    filecontents = np.ndfromtxt(path, dtype = float, unpack = True, skip_header = Hlength, delimiter=" ")
    return(filecontents)

a = np.array([])
Er = np.array([])
plt.close('all')
Mydir = "/home/micha/workdir/60Co/Calibration/Calibr/Carea/"
Mydir = "/home/micha/workdir/252CfMeasurments/after/calibration/Carea/"
for line in sorted(os.listdir(Mydir)):
    M=read_data(Mydir+"/"+line)
    a = np.hstack((a, M[1]))
#    Er = np.hstack((Er, M[2]))
print(M)
a = a.reshape(len(os.listdir(Mydir)),len(M[0]))
#Er = Er.reshape(len(os.listdir(Mydir)),len(M[0]))
All = pd.DataFrame(a, index = range(1,len(os.listdir(Mydir))+1), columns= M[0])
#Err = pd.DataFrame(Er, index = range(1,len(os.listdir(Mydir))+1), columns= M[0])

All.T.plot()
plt.show()
