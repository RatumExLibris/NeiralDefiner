import sys
from PyQt5 import QtWidgets
import mydesign2

class Main(QtWidgets.QMainWindow, mydesign2.Ui_Neiralink):
    def __init__(self):
        super().__init__()
        self.ui = mydesign2.Ui_Neiralink()
        self.setupUi(self)

        #self.label.setText("еееееее")

def start():
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
 
    sys.exit(app.exec())

start()
