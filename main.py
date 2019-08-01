#!/usr/bin/python -u
import sys, os
import serial, time
from serial.tools import list_ports
import json

sys.path.insert(0, os.getcwd() + '\\ui')
sys.path.insert(0, os.getcwd() + '\\ControlB3603')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction

import main_ui

from b3603_control import Control

def close_connect(cmdr):
    del cmdr      


class ExampleApp(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design

        self.__cmdr = Control('COM1') # Init B3603 control class
        if self.__cmdr .get_status() != 0: # If the connection is sucsessfully
            self.__cmdr.close_connect()

        menubar = self.menuBar 
        connMenu = menubar.addMenu('&Connection') # Add menu to menu bar 
        
        ports = list(list_ports.comports()) # return ListPortInfo
        for port in ports:
            extractAction = QAction(port.device, self)
            extractAction.triggered.connect(self.on_connect_clicked)
            connMenu.addAction(extractAction)
            print(port.device)

        try:
            config = ""
            with open("config.json", "r") as config_file:
                config = json.load(config_file)
            print("Config found...")
        except:
            print("Config not found")
            self.update_config(5000, 0)
            with open("config.json", "r") as config_file:
                config = json.load(config_file)            

        self.leVoltage.setText(str(config['voltage']))
        self.leVoltageOfst.setText(str(config['voltage offset']))
        
        # Slot connecting
        self.pbOff.clicked.connect(self.set_off)
        self.pbSet.clicked.connect(self.set_on)

    def on_connect_clicked(self):
        action = self.sender()
        print('Action: ' + action.text())
        self.__cmdr = Control(action.text())  # /dev/ttyUSB0 for Linux
        print(self.__cmdr.get_status())
        if self.__cmdr.get_status() == False:
            self.__cmdr.close_connect()
            self.centralWidget().setEnabled(False)
        else:        
            self.centralWidget().setEnabled(True)

    def set_off(self):
        self.leVoltage.setText('0')
        self.__cmdr.send_cmd("OUTPUT 0")    
        # close_connect(cmdr)

    def set_on(self):
        v = self.leVoltage.text()
        ofst = self.leVoltageOfst.text()
        self.update_config(int(v), int(ofst))
        volt = int(v) - int(ofst)

        if self.__cmdr.get_status() == 0:
            # close_connect(cmdr) 
            self.__cmdr.close_connect()
            self.centralWidget.setEnabled(False)
            return

        print('Voltage: ' + str(volt))
        self.__cmdr.send_cmd("VOLTAGE " + str(volt))
        self.__cmdr.send_cmd("CURRENT 1000")
        self.__cmdr.send_cmd("OUTPUT 1")
        # close_connect(cmdr)        

    def update_config(self, voltage, ofst):
        config = {
            "voltage": voltage,
            "voltage offset": ofst
        }
        cfg = json.dumps(config, indent=4, sort_keys=True)
        print(cfg)
        f = open("config.json", 'w')
        f.write(cfg)
        f.close()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
