import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QFileDialog)
from PyQt5.QtCore import pyqtSlot


# list of the animals
animals_list = ["Select an Animal:", "Marlin", "Shark", "Tuna", "Whale", "Turtle"]
dataset_list = []

# window class
class new_window(QWidget):
 def __init__(self, animal_choice):
     super().__init__()
     self.setAutoFillBackground(True)
     p = self.palette()
     
     #if else statements for the animals
     if animal_choice =="Marlin":
         dataset
     elif animal_choice =="Shark":
         dataset
     elif animal_choice =="Tuna":
         dataset
     elif animal_choice =="Whale":
         dataset
     elif animal_choice =="Turtle":
         dataset
     self.setPalette(p)

#main class window
class Window(QWidget):
  def __init__(self):
      super().__init__()

      vbox = QVBoxLayout()
      
      # create label
      self.qt_combo_box = QComboBox()
      self.qt_combo_box.addItems(animals_list)
      self.our_label = QLabel("")


      






      self.our_button = QPushButton("Click here to plot the animals movements.", self)
      self.our_button.clicked.connect(self.button_clicked)


      # create data box
      self.our_button1 = QPushButton("Select the data", self)
      self.our_button.clicked.connect(self.button_clicked)
      
  
      vbox.addWidget(self.qt_combo_box)
      vbox.addWidget(self.our_label)
      vbox.addWidget(self.our_button1)

      """
      def selectFile():
        lineEdit.setText(QFileDialog.getOpenFileName())

      self.our_button.clicked.connect.connect(selectFile)
      """



      
      # create box
      vbox.addWidget(self.qt_combo_box)
      vbox.addWidget(self.our_label)
      vbox.addWidget(self.our_button)

      self.setGeometry(400, 400, 500, 300)
            
      self.setLayout(vbox)
      self.setWindowTitle("Animal Telemetry Plotter")
      self.my_text = self.qt_combo_box.currentText()
     
     


     

   
     
   
  







  @pyqtSlot()
  def button_clicked(self):
      # new window
      self.new_window = new_window(self.my_text)
      self.new_window.show()

# creates object with Qapp.
app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
