# TestProgramWithGUI.py
# This is a program for testing Qt GUI and PySide

import sys

# Import Qt GUI component
from PySide import QtGui

from PySide.QtGui import *

# Import GUI File


from Gui import Ui_Data
import griphf
import QueryConverter
from tkinter import *
# Self Function





# Make main window class
class MainWindow(QMainWindow,Ui_Data):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        # Connect button click event to PrintHello function
        self.data=[]

        def PrintHello():
            print("Hello")
            p = QtGui.QFileDialog.getOpenFileName()
            datatxt=[]
            dataT=[]
            f = open(p[0], "r")
            lines = f.readlines()  # 读取全部内容
            for line in lines:
                datatxt.append(list(map(tuple,line.split(','))))
            for d in datatxt:
                dataT.extend(d)
            for da in dataT:
                self.data.append((da[0],da[2],da[4]))

        data1=[(1,2,"a"),(2,3,"b"),(2,6,"g"),(3,5,"c"),(1,4,"f"),(3,7,"c"),(4,8,"b"),(8,9,"c")]
        self.AddDiagram.clicked.connect(PrintHello)
        

        def PrintPath():
            query = self.lineEdit.text()
            if "+" in query or "[" in query:
                print(query)
                for q in QueryConverter.QueryToWords(query):
                    print(q,griphf.GetVertextParh(self.data,q))
            else:
                print(query, griphf.GetVertextParh(self.data, query))
            # print(query)
        self.CheckPath.clicked.connect(PrintPath)

# End of main window class


# Main Function
if __name__=='__main__':
    Program = QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    Program.exec_()