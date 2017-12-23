# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_speedLimit_connector.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_speedLimit_connector(object):
    def setupUi(self, speedLimit_connector):
        speedLimit_connector.setObjectName("speedLimit_connector")
        speedLimit_connector.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(speedLimit_connector)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(speedLimit_connector)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), speedLimit_connector.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), speedLimit_connector.reject)
        QtCore.QMetaObject.connectSlotsByName(speedLimit_connector)

    def retranslateUi(self, speedLimit_connector):
        speedLimit_connector.setWindowTitle(QtGui.QApplication.translate("speedLimit_connector", "speedLimit_connector", None, QtGui.QApplication.UnicodeUTF8))
