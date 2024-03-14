#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

df["weight_98"] = 1/df["r0_shue_1998"]

name_input = ["Pd","Bz"]

X = df[name_input]

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
df["density_pd_bz"] = np.exp(kde.score_samples(df[name_input]))

print("densite pd bz ok")

name_input = ["r0_shue_1998"]
X = df[name_input]

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
df["density_r0_98"] = np.exp(kde.score_samples(df[name_input]))

print("densite r0 ok")

df.to_pickle('Test_shue_nose_with_density.pkl')