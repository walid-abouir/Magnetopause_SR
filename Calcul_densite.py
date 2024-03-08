"""
Created on Fri Mar  8 13:41:16 2024

@author: cargnell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.neighbors import KernelDensity

file_name = 'Test_shue_nose.pkl'
df = pd.read_pickle(file_name)

#df = df[:365*24]

df["weight_98"] = 1/df["r0_shue_1998"]

name_input = ["Pd","Bz"]
print(df[name_input])

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(df[name_input])
df["density"] = np.exp(kde.score_samples(df[name_input]))

df.to_csv('Test_shue_nose_with_density.csv')

"""
plt.figure()
plt.scatter(df["Pd"],df["Bz"],c=df["density"],cmap=cm.plasma)
plt.show()"""
