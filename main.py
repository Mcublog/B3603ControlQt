#!/usr/bin/python -u
import sys, os
import serial, time
from serial.tools import list_ports
import json
import threading

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
        self.lock = threading.Lock()

        self.__cmdr = Control('COM1') # Init B3603 control class
        if self.__cmdr .get_status() != 0: # If the connection is sucsessfully
            self.__cmdr.close_connect()

        menubar = self.menuBar
        self.connMenu = menubar.addMenu('&Connection') # Add menu to menu bar

        t = threading.Thread(target=self.port_scan)
        t.start()

        # ports = list(list_ports.comports()) # return ListPortInfo
        # for port in ports:
        #     extractAction = QAction(port.device, self)
        #     extractAction.triggered.connect(self.on_connect_clicked)
        #     self.connMenu.addAction(extractAction)
        #     print(port.device)

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

    def exuite_cmd(self, func, param = None):
        ret = None
        self.lock.acquire()
        try:

            if param != None:
                ret = func(param)
            else:
                ret = func()
        finally:
            self.lock.release()
        return ret

    def dispay_disable(self):
        self.exuite_cmd(self.__cmdr.close_connect)
        self.centralWidget().setEnabled(False)

    def port_scan(self):
        ports = []
        last_posts = []
        while True:
            ports = list(list_ports.comports()) # return ListPortInfo
            if (ports != last_posts):
                self.connMenu.clear()
                for port in ports:
                    extractAction = QAction(port.device, self)
                    extractAction.triggered.connect(self.on_connect_clicked)
                    self.connMenu.addAction(extractAction)
                    print(port.device)
                status = 0

                status = self.exuite_cmd(self.__cmdr.get_status)

                # self.lock.acquire()
                # try:
                #     status = self.__cmdr.get_status()
                # finally:
                #     self.lock.release()

                if (status == 1):
                    port = self.exuite_cmd(self.__cmdr.get_port)
                    # self.lock.acquire()
                    # try:
                    #     port = self.__cmdr.get_port()
                    # finally:
                    #     self.lock.release()
                    ports_num = []
                    for dev in ports:
                        ports_num.append(dev.device)
                    if not (port in ports_num):
                        self.dispay_disable()
            last_posts = ports
            time.sleep(0.5)

    def on_connect_clicked(self):
        action = self.sender()
        print('Action: ' + action.text())

        self.lock.acquire()
        try:
            if (self.__cmdr != None):
                del self.__cmdr
            self.__cmdr = Control(action.text())  # /dev/ttyUSB0 for Linux
        finally:
            self.lock.release()

        status = self.exuite_cmd(self.__cmdr.get_status)
        if (status == 0):
            self.dispay_disable()
        else:
            self.centralWidget().setEnabled(True)

    def set_off(self):
        status = self.exuite_cmd(self.__cmdr.send_cmd, "OUTPUT 0")
        if (status == 0):
            self.dispay_disable()

    def set_on(self):
        v = self.leVoltage.text()
        ofst = self.leVoltageOfst.text()
        self.update_config(int(v), int(ofst))
        volt = int(v) - int(ofst)

        status = self.exuite_cmd(self.__cmdr.get_status)
        if (status == 0):
            self.dispay_disable()
            return

        print('Voltage: ' + str(volt))
        status = self.exuite_cmd(self.__cmdr.send_cmd, "VOLTAGE " + str(volt))
        status = self.exuite_cmd(self.__cmdr.send_cmd, "CURRENT 1000")
        status = self.exuite_cmd(self.__cmdr.send_cmd, "OUTPUT 1")

        if (status == 0):
            self.dispay_disable()


    def update_config(self, voltage, ofst):
        config = {
            "voltage": voltage,
            "voltage offset": ofst
        }
        cfg = json.dumps(config, indent = 4, sort_keys = True)
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
