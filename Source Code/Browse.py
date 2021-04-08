


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from threading import *
from param_wind import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 273)
        self.file = QtWidgets.QLineEdit(Dialog)
        self.file.setGeometry(QtCore.QRect(20, 90, 261, 20))
        self.file.setObjectName("file")
        self.browse = QtWidgets.QPushButton(Dialog, clicked = lambda : self.get_file(Dialog))
        self.browse.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.browse.setObjectName("browse")
        self.edit = QtWidgets.QPushButton(Dialog, clicked = lambda : self.next())
        self.edit.setGeometry(QtCore.QRect(150, 150, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def get_file(self, Dialog):
    	self.name = QFileDialog().getOpenFileName(Dialog, "Open image",r"C:")
    	self.file.setText(self.name[0])

    def next(self):
    	self.param_dialog = QtWidgets.QDialog()
    	self.ui = Ui_param_dialog()
    	self.ui.img_file = self.name[0]
    	obj = self.ui.setupUi(self.param_dialog)
    	self.param_dialog.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.browse.setText(_translate("Dialog", "Browse"))
        self.edit.setText(_translate("Dialog", "Edit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
