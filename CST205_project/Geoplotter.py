
"""
Joshua Trup
Zeke Tuszynksi
Jose Alfaro 
CST 205
4/24/19
"""

# import the neccessary modules: 
import geopandas
import numpy as np
import pandas as pd
from shapely.geometry import Point

import missingno as msn

import seaborn as sns
import matplotlib.pyplot as plt

import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.my_line = QLineEdit()

        # adding a label to give instruction to the user
        self.label1 = QLabel('Enter file name below of the animal you wish to track: ', self)
       
        # our button
        self.my_button = QPushButton("Graph Data")
        
        vbox = QVBoxLayout()
       
        
        vbox.addWidget(self.label1) 
       
        vbox.addWidget(self.my_line)
        vbox.addWidget(self.my_button)
         
         # adding a background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(85, 50, 230))
        self.setPalette(p)
        
        
        self.setLayout(vbox)
        self.my_button.clicked.connect(self.editpic) 

        
        # Setting the window size
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle("GeoPlotter")
    
    




    def editpic(self):
        print("Hello")
        filename = "Tag_data/" + self.my_line.text()
        self.mapmaker(filename)
     
 
    def mapmaker(self, filename):
        
        world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

        animal = pd.read_csv(filename)
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
        plt.savefig(str(filename).replace(".csv", ".png"), bbox_inches='tight');
      
      
      
  
  
        
app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
