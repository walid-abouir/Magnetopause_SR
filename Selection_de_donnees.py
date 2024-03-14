#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:27:55 2024

@author: cargnell
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

file_name = 'Test_shue_nose_with_density.csv'
df = pd.read_csv(file_name)

def plot_density(df) :
    plt.figure()
    plt.scatter(df["Pd"],df["Bz"],c=np.log(df["density"]),cmap=cm.plasma,marker='x')
    plt.show()

#plot_density(df)

# On trie le df par ordre croissant de densité des points
df.sort_values('density', ascending=True, inplace=True)

print(df)

# Pourcentage de valeurs que l'on veut qualifier de faible densité.
# Par exemple, 0.1 -> on va forcer un ceratin nombre de points à être dans les 10% les plus faible de densité
pourcentage = 0.025

nb_faible_densite = int(pourcentage*len(df))

df_faible_densite = df[:nb_faible_densite]
df_forte_densite = df[nb_faible_densite:] 

print(df_faible_densite)

#plot_density(df_faible_densite)

nb_selected_point = 5000
taux_train_set = 4/5

taux_point_faible_densite = 0.5

df_selected_point = pd.concat([df_faible_densite.sample(frac=1)[:int(nb_selected_point*taux_point_faible_densite)],
                               df_forte_densite.sample(frac=1)[:int(nb_selected_point*taux_point_faible_densite)]])

plot_density(df_selected_point)

nb_point_train = int(taux_train_set*nb_selected_point)
nb_point_test = nb_selected_point - nb_point_train