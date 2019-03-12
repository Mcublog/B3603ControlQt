#!/usr/bin/python -u
import sys, os
sys.path.insert(0, os.getcwd() + '\\ui')
sys.path.insert(0, os.getcwd() + '\\control')

from PyQt5 import QtWidgets

import main_ui

from b3603_out_off import main as off
from b3603_set import main as set

class ExampleApp(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design
        # Slot connecting
        self.pbOff.clicked.connect(self.set_off)
        self.pbSet.clicked.connect(self.set_on)

    def set_off(self):
        self.leVoltage.setText('0')
        off()

    def set_on(self):
        self.leVoltage.setText('4200')
        set()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()