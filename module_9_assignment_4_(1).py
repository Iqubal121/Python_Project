# -*- coding: utf-8 -*-
"""module 9 assignment 4 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1puy1FvLuQtFnyzCKWiMtnutd9h0DJWNE
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

data=np.array([[5,3],
[10,15],
[15,12],
[24,10],
[30,30],
[85,70],
[71,80],
[60,78],
[70,55],
[80,91]])

data

import pandas as pd
data=pd.DataFrame(data)

data.columns=["x",'y']

data

plt.scatter(data['x'],data['y'])

import scipy.cluster.hierarchy as sch
plt.figure(figsize=(7,5))
plt.title('Dendrogram')
dendo=sch.dendrogram(sch.linkage(data,method='ward'))

from statsmodels.api import add_constant
import statsmodels.api as sm
x2 = add_constant(x_train)
lm = sm.OLS(y_train,x2)
lm2 = lm.fit()

