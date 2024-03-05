import pandas as pd

filepath =  "C:/Users/romai/Desktop/INSA/4A/Projet_Recherche/Test_shue_nose.pkl"

df = pd.read_pickle(filepath)

print(df.head)

df["1/r0_98"] = 1/df["r0_shue_1998"]

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

"""
x = df["Pd"]
y = df["Bz"]
"""

points_regardes = 200000

x = df["Pd"][:points_regardes]
y = df["Bz"][:points_regardes]

# Paramètres de l'animation
frames = 50  # Nombre de trames dans l'animation
sigma = 0.2  # Paramètre de lissage pour le noyau gaussien

# Mise en place du tracé
fig, ax = plt.subplots()
sns.set(style="white", palette="muted", color_codes=True)


taille_intervalle = int(points_regardes/frames)


ax.set_xlim(0,15)
ax.set_ylim(-7,7)

def update(frame):   
    intervalle = np.linspace(frame*taille_intervalle,(frame+1)*taille_intervalle,100,dtype='int64')

    # Ploter les points de données
    sns.scatterplot(x=x[intervalle],y=y[intervalle], ax=ax, color='b', alpha=0.5)
    
    # Calculer la densité des points avec un noyau gaussien
    sns.kdeplot(x=x[intervalle],y=y[intervalle], cmap="Blues", fill=True, ax=ax, levels=15, thresh=0, bw_method=sigma)
    
    # Ajouter des informations supplémentaires si nécessaire
    ax.set_title(f'Frame {frame + 1}/{frames}')
    
    
ax.set_xlabel('Pd')
ax.set_ylabel('Bz') 

# Créer l'animation
animation = FuncAnimation(fig, update, frames=frames)

# Afficher l'animation
plt.show()