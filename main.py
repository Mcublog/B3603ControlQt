#!/usr/bin/python -u
import sys, os
import serial, time

sys.path.insert(0, os.getcwd() + '\\ui')
sys.path.insert(0, os.getcwd() + '\\control')

from PyQt5 import QtWidgets

import main_ui

from b3603_control import Control

def close_connect(cmdr):
    del cmdr      


class ExampleApp(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design
        # Slot connecting
        self.pbOff.clicked.connect(self.set_off)
        self.pbSet.clicked.connect(self.set_on)
          
    def set_off(self):
        self.leVoltage.setText('0')
        cmdr = Control('COM9')  # /dev/ttyUSB0 for Linux
        if cmdr.get_status() == 0:
            return close_connect(cmdr)
        cmdr.send_cmd("OUTPUT 0")    
        close_connect(cmdr)

    def set_on(self):
        v = self.leVoltage.text()
        print(v)
        cmdr = Control('COM9')  # /dev/ttyUSB0 for Linux
        if cmdr.get_status() == 0:
            return close_connect(cmdr)
        cmdr.send_cmd("OUTPUT 0")
        cmdr.send_cmd("VOLTAGE " + v)
        cmdr.send_cmd("CURRENT 800")
        cmdr.send_cmd("OUTPUT 1")
        close_connect(cmdr)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()