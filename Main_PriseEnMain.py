import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from pysr import PySRRegressor

file_name = './Test_shue_nose.pkl'
data = pd.read_pickle(file_name)

Pd = data['Pd']
Bz = data['Bz']
r0_98 = data['r0_shue_1998']
r0_97 = data['r0_shue_1997']

data = np.array(data)

#%%

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

nb_valeurs_aff = 10000

ax.scatter(Pd[:nb_valeurs_aff], Bz[:nb_valeurs_aff], r0_98[:nb_valeurs_aff])

ax.set_xlabel('Pd')
ax.set_ylabel('Bz')
ax.set_zlabel('r0_98')

plt.show()

#%%
nb_observations = len(data[:,0])
nb_points_select = 5000
nb_points_training = int(4/5*nb_points_select)
nb_points_test = int(1/5*nb_points_select)

pts_retenus = np.arange(nb_observations)
rd.shuffle(pts_retenus)
pts_retenus = pts_retenus[:nb_points_select]
print(pts_retenus,len(pts_retenus))

selected_data = data[pts_retenus,:]
print(selected_data)

test_set = selected_data[:nb_points_test,:]
print(len(test_set),'=',nb_points_test)
training_set = selected_data[nb_points_test:,:]
print(len(training_set),'=',nb_points_training)

#%%
X = training_set[:,0:2]
y = training_set[:,2]


model = PySRRegressor()

model.fit(X,y)