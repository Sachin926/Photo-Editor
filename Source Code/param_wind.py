

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import *

global img
class Ui_param_dialog(object):
    img_file = ""
    def setupUi(self, param_dialog):
        img = self.img_file
        with open ("file.txt", "wt") as f:
            f.write(img)
        param_dialog.setObjectName("param_dialog")
        param_dialog.resize(400, 466)
        self.bright = QtWidgets.QSlider(param_dialog)
        self.bright.setMinimum(0)
        self.bright.setMaximum(255)
        self.bright.setGeometry(QtCore.QRect(150, 60, 231, 22))
        self.bright.setOrientation(QtCore.Qt.Horizontal)
        self.bright.setObjectName("bright")
        self.bright.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.bright.setTickInterval(20)
        self.bright.setValue(0)
        self.dark = QtWidgets.QSlider(param_dialog)
        self.dark.setGeometry(QtCore.QRect(150, 110, 231, 22))
        self.dark.setOrientation(QtCore.Qt.Horizontal)
        self.dark.setObjectName("dark")
        self.dark.setMinimum(0)
        self.dark.setMaximum(255)
        self.dark.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.dark.setTickInterval(20)
        self.dark.setValue(0)
        self.blur = QtWidgets.QSlider(param_dialog)
        self.blur.setGeometry(QtCore.QRect(150, 160, 231, 22))
        self.blur.setOrientation(QtCore.Qt.Horizontal)
        self.blur.setObjectName("blur")
        self.blur.setMinimum(3)
        self.blur.setMaximum(15)
        self.blur.setSingleStep(2)
        self.blur.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.blur.setTickInterval(2)
        self.blur.setValue(0)
        self.label = QtWidgets.QLabel(param_dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(param_dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(param_dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.scale_x = QtWidgets.QDoubleSpinBox(param_dialog, value = 1, maximum = 5, minimum = 0, singleStep = 0.1)
        self.scale_x.setGeometry(QtCore.QRect(150, 210, 62, 22))
        self.scale_x.setObjectName("scale_x")
        self.scale_x.setValue(1)
        self.scale_y = QtWidgets.QDoubleSpinBox(param_dialog, value = 1, maximum = 5, minimum = 0, singleStep = 0.1)
        self.scale_y.setGeometry(QtCore.QRect(150, 260, 62, 22))
        self.scale_y.setObjectName("scale_y")
        self.scale_y.setValue(1)
        self.label_4 = QtWidgets.QLabel(param_dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(param_dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.color = QtWidgets.QComboBox(param_dialog, editable = False)
        self.color.addItems(["NONE", "Grey Scale", "HSV", "Black & White", "EDGE"])
        self.color.setGeometry(QtCore.QRect(150, 310, 121, 22))
        self.color.setObjectName("color")
        self.label_6 = QtWidgets.QLabel(param_dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 310, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.save = QtWidgets.QPushButton(param_dialog, clicked = lambda : self.save_file())
        self.save.setGeometry(QtCore.QRect(230, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.preview = QtWidgets.QPushButton(param_dialog, clicked = lambda : self.write_file())
        self.preview.setGeometry(QtCore.QRect(50, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.preview.setFont(font)
        self.preview.setObjectName("preview")

        self.retranslateUi(param_dialog)
        QtCore.QMetaObject.connectSlotsByName(param_dialog)

    def write_file(self):
        l = [str(self.bright.value()), str(self.dark.value()), 
                    str(self.blur.value()), str(self.scale_x.value()), 
                            str(self.scale_y.value()), str(self.color.currentText())]

        with open("params.txt", "wt") as file:
            for i in l:
                file.write(i)
                file.write("\n")

        thread = open_cv()
        thread.start()

    def save_file(self):
        l = [str(self.bright.value()), str(self.dark.value()), 
                    str(self.blur.value()), str(self.scale_x.value()), 
                            str(self.scale_y.value()), str(self.color.currentText())]

        with open("params.txt", "wt") as file:
            for i in l:
                file.write(i)
                file.write("\n")

        obj = open_cv()
        obj.run()
        obj.save()



    def retranslateUi(self, param_dialog):
        _translate = QtCore.QCoreApplication.translate
        param_dialog.setWindowTitle(_translate("param_dialog", "Set Parameters"))
        self.label.setText(_translate("param_dialog", "Brightness"))
        self.label_2.setText(_translate("param_dialog", "Darkness"))
        self.label_3.setText(_translate("param_dialog", "Blur"))
        self.label_4.setText(_translate("param_dialog", "Scale X"))
        self.label_5.setText(_translate("param_dialog", "Scale Y"))
        self.label_6.setText(_translate("param_dialog", "Color Scheme"))
        self.save.setText(_translate("param_dialog", "Save"))
        self.preview.setText(_translate("param_dialog", "Preview"))

import numpy as np
import cv2 as cv

class open_cv(Thread):
    def run(self):

        with open ("params.txt", "rt") as file:
            data = file.readlines()

        self.bright = int(data[0])
        self.dark = int(data[1])
        self.blur = int(data[2])

        if (self.blur % 2 == 0 and self.blur != 0):
            self.blur = self.blur + 1

        self.scale_x = float(data[3])
        self.scale_y = float(data[4])
        self.color = data[5].split("\n")[0]

        with open("file.txt") as f:
            path = f.read()

        self.image = cv.imread(path)

        self.adjust_brightness()


    def adjust_brightness(self):
        #Brightness
        mat1 = np.ones(self.image.shape, dtype = "uint8")
        mat1 = mat1 * self.bright
        self.image = cv.add(src1 = self.image, src2 = mat1)

        #Darkness
        mat2 = np.ones(self.image.shape, dtype = "uint8")
        mat2 = mat2 * self.dark
        self.image = cv.subtract(src1 = self.image, src2 = mat2)

        #Blur
        self.image = cv.GaussianBlur(src = self.image, ksize = (self.blur, self.blur), sigmaX = 0)

        #Resize 
        height, width = self.image.shape[:2]
        height = int(height * self.scale_x)
        width = int(width * self.scale_y)
        self.image = cv.resize(src = self.image, dsize = (width, height),
                         fx = self.scale_x, fy = self.scale_y, interpolation=cv.INTER_CUBIC)

        #Color Scheme
        switch = {"NONE" : self.none, "Grey Scale" : self.grey, "HSV" : self.hsv, "Black & White" : self.bnw, "EDGE" : self.edge}
        switch[self.color]()

        cv.destroyAllWindows()
        cv.imshow("image", self.image)
        cv.waitKey(0)

    def none(self):
        pass

    def grey(self):
        print (self.image.shape)
        self.image = cv.cvtColor(src = self.image, code = cv.COLOR_BGR2GRAY)

    def hsv(self):
        self.image = cv.cvtColor(src = self.image, code = cv.COLOR_BGR2HSV)

    def bnw(self):
        self.image = cv.cvtColor(src = self.image, code = cv.COLOR_BGR2GRAY)
        _, self.image = cv.threshold(src = self.image, thresh = 127, 
                                                maxval = 255, type = cv.THRESH_BINARY)

    def edge(self):
        self.image = cv.Canny(image = self.image, threshold1 = 70, threshold2 = 100)

    def save(self):
        cv.imwrite("edit.png", img = self.image)



