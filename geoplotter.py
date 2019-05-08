import geopandas
import numpy as np
import pandas as pd
from shapely.geometry import Point

import missingno as msn

import seaborn as sns
import matplotlib.pyplot as plt

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))




animal = pd.read_csv('blackmarlin.csv')
print(animal.describe())

animal['coordinates'] = animal[['longitude', 'latitude']].values.tolist()
animal['coordinates'] = animal['coordinates'].apply(Point)

animal = geopandas.GeoDataFrame(animal, geometry='coordinates')

animal.plot(figsize=(20,10));


fig, ax = plt.subplots(1, figsize=(20,20))
base = world.plot(figsize=(30,20))
animal.plot(ax=base, column='month', marker="<", markersize=10, cmap='rainbow', label="Transmisson Time")
_ = ax.axis('off')
ax.legend(loc='lower left')
plt.legend()
ax.set_title("PSTAT-tagged Animal", fontsize=25)
plt.savefig('animaltag.png',bbox_inches='tight');

