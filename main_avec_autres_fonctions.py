# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:25:55 2024

@author: Thibault LAUILHE
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from pysr import PySRRegressor

file_name = './Test_shue_nose_with_density.pkl'
df = pd.read_pickle(file_name)
data = np.array(df)

print(df)

#%%

# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(projection='3d')

# nb_valeurs_aff = 10000

# ax.scatter(Pd[:nb_valeurs_aff], Bz[:nb_valeurs_aff], r0_98[:nb_valeurs_aff])

# ax.set_xlabel('Pd')
# ax.set_ylabel('Bz')
# ax.set_zlabel('r0_98')

# plt.show()

#%%

df.sort_values('density_r0_98', ascending=True, inplace=True)

# Pourcentage de valeurs que l'on veut qualifier de faible densité.
# Par exemple, 0.1 -> on va forcer un ceratin nombre de points à être dans les 10% les plus faible de densité
pourcentage = 0.025

def plot_density(df) :
    plt.figure()
    plt.scatter(df["Pd"],df["Bz"],c=np.log(df["density_r0_98"]),cmap=cm.plasma,marker='x')
    plt.show()

#plot_density(df)

nb_faible_densite = int(pourcentage*len(df))

df_faible_densite = df[:nb_faible_densite] #data frame qui contient les points les moins denses
df_forte_densite = df[nb_faible_densite:] #les points les plus denses

nb_selected_point = 5000
taux_train_set = 4/5

taux_point_faible_densite = 0.5

df_selected_point = pd.concat([df_faible_densite.sample(frac=1)[:int(nb_selected_point*taux_point_faible_densite)],
                               df_forte_densite.sample(frac=1)[:int(nb_selected_point*taux_point_faible_densite)]])

nb_point_train = int(taux_train_set*nb_selected_point)

df_selected_point = df_selected_point.sample(frac=1)

training_set = df_selected_point[:nb_point_train]
test_set = df_selected_point[nb_point_train:]

print(training_set)
print(test_set)

#%%

X = training_set[["Pd","Bz"]]
y = training_set["r0_shue_1998"]


model = PySRRegressor(
    binary_operators=["+", "*","-","/","^"],
    unary_operators=["exp","sin"]
    )

model.set_params(
    population_size=75,  # default 33
    tournament_selection_n=23,  # default 10
    tournament_selection_p=0.8,  # default 0.86
    ncyclesperiteration=100,  # default 550
    parsimony=1e-3,  # default 0.0032
    fraction_replaced_hof=0.08,  # default 0.035
    optimizer_iterations=25,  # default 8
    crossover_probability=0.12,  # default 0.066
    weight_optimize=0.06,  # default 0.0
    populations=50,  # default 15
    adaptive_parsimony_scaling=100.0,  # default 20
    warmup_maxsize_by=0.005
)

model.fit(X,y,weights=training_set["weight_98"])