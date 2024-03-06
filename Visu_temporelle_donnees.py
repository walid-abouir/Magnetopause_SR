import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

filepath =  "C:/Users/romai/Desktop/INSA/4A/Projet_Recherche/Test_shue_nose.pkl"

df = pd.read_pickle(filepath)

starting_year = 2003
ending_year = 2004

# Paramètres de l'animation
frames = (ending_year+1-starting_year)*12  # Nombre de trames dans l'animation
sigma = 0.1  # Paramètre de lissage pour le noyau gaussien

# Mise en place du tracé
fig, (ax1, ax2) = plt.subplots(2,1)
sns.set(style="white", palette="muted", color_codes=True)

# Création de toutes les dates de l'animation
range_mois = ['01','02','03','04','05','06','07','08','09','10','11','12']
dates = [str(annee)+'-'+mois for annee in range(starting_year,ending_year+1) for mois in range_mois]

def update(frame):   
    ax1.clear()
    ax1.set_xlim(0,10)
    ax1.set_ylim(-7,7)   
    ax1.set_xlabel('Pd')
    ax1.set_ylabel('Bz') 
    
    ax2.clear()
    ax2.set_xlim(5,18)
    ax2.set_ylim(0,1)
    
    date = dates[frame]
    
    data = df[(df.index.strftime('%Y-%m-%d %H:%M:%S')).str.startswith(date)]

    ax2.hist(data["r0_shue_1998"],density=True,bins=30)
    
    # Ploter les points de données
    sns.scatterplot(x=data["Pd"],y=data["Bz"], ax=ax1, color='b', alpha=0.5)
    
    # Calculer la densité des points avec un noyau gaussien
    sns.kdeplot(x=data["Pd"],y=data["Bz"], cmap="Blues", fill=True, ax=ax1, levels=15, thresh=0, bw_method=sigma)
    
    # Ajouter des informations supplémentaires si nécessaire
    ax1.set_title(dates[frame])

# Créer l'animation
animation = FuncAnimation(fig, update, frames=frames,interval=100)

# Afficher l'animation
plt.show()
