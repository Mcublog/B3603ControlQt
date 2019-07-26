#!/usr/bin/python -u
import sys, os
import serial, time
import json

sys.path.insert(0, os.getcwd() + '\\ui')
sys.path.insert(0, os.getcwd() + '\\ControlB3603')

from PyQt5 import QtWidgets

import main_ui

from b3603_control import Control

def close_connect(cmdr):
    del cmdr      


class ExampleApp(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Init design

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
          
    def set_off(self):
        self.leVoltage.setText('0')
        cmdr = Control('COM9')  # /dev/ttyUSB0 for Linux
        if cmdr.get_status() == 0:
            return close_connect(cmdr)
        cmdr.send_cmd("OUTPUT 0")    
        close_connect(cmdr)

    def set_on(self):
        v = self.leVoltage.text()
        ofst = self.leVoltageOfst.text()
        self.update_config(int(v), int(ofst))
        volt = int(v) - int(ofst)

        cmdr = Control('COM9')  # /dev/ttyUSB0 for Linux
        if cmdr.get_status() == 0:
            return close_connect(cmdr)

        print('Voltage: ' + str(volt))
        cmdr.send_cmd("VOLTAGE " + str(volt))
        cmdr.send_cmd("CURRENT 1000")
        cmdr.send_cmd("OUTPUT 1")
        close_connect(cmdr)

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
