# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Python\B3603Control\ui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(238, 175)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leVoltage = QtWidgets.QLineEdit(self.centralwidget)
        self.leVoltage.setText("0")
        self.leVoltage.setMaxLength(5)
        self.leVoltage.setFrame(True)
        self.leVoltage.setObjectName("leVoltage")
        self.horizontalLayout_2.addWidget(self.leVoltage)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbSet = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbSet.setObjectName("pbSet")
        self.horizontalLayout.addWidget(self.pbSet)
        self.pbOff = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pbOff.setObjectName("pbOff")
        self.horizontalLayout.addWidget(self.pbOff)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "B3603"))
        self.leVoltage.setInputMask(_translate("MainWindow", "99999"))
        self.label.setText(_translate("MainWindow", "mV"))
        self.groupBox.setTitle(_translate("MainWindow", "Control"))
        self.pbSet.setText(_translate("MainWindow", "Set"))
        self.pbOff.setText(_translate("MainWindow", "OFF"))


import res_rc
