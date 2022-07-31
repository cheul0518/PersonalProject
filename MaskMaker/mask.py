import sys
import os
import cv2

import resource
import numpy as np
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def __init__(self):
        super().__init__()
        self.label_dir = None
        self.form = QtWidgets.QWidget()
        self.setupUi(self.form)
        self.SetConnect()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 545)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.bg_2 = QtWidgets.QLabel(Dialog)
        self.bg_2.setGeometry(QtCore.QRect(50, 30, 320, 480))
        self.bg_2.setStyleSheet("border-image:url(:/image/bg.jpg);\n"
"border-radius: 20px;")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(260, 420, 381, 521))
        self.widget_2.setObjectName("widget_2")
        self.bg_3 = QtWidgets.QLabel(self.widget_2)
        self.bg_3.setGeometry(QtCore.QRect(30, 20, 320, 480))
        self.bg_3.setStyleSheet("border-image: url(:/Image/320480_2.jpg);\n"
"border-radius: 20px;")
        self.bg_3.setText("")
        self.bg_3.setObjectName("bg_3")
        self.save_dir_2 = QtWidgets.QLineEdit(self.widget_2)
        self.save_dir_2.setGeometry(QtCore.QRect(60, 210, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.save_dir_2.setFont(font)
        self.save_dir_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,230);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.save_dir_2.setText("")
        self.save_dir_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.save_dir_2.setObjectName("save_dir_2")
        self.load_file_2 = QtWidgets.QLineEdit(self.widget_2)
        self.load_file_2.setGeometry(QtCore.QRect(60, 300, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.load_file_2.setFont(font)
        self.load_file_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,230);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.load_file_2.setText("")
        self.load_file_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.load_file_2.setObjectName("load_file_2")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(110, 80, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgba(255,255,255, 255);")
        self.title.setObjectName("title")
        self.save_dir = QtWidgets.QLineEdit(Dialog)
        self.save_dir.setGeometry(QtCore.QRect(80, 290, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.save_dir.setFont(font)
        self.save_dir.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,230);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.save_dir.setText("")
        self.save_dir.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.save_dir.setReadOnly(True)
        self.save_dir.setPlaceholderText("")
        self.save_dir.setObjectName("save_dir")
        self.bg_filter = QtWidgets.QLabel(Dialog)
        self.bg_filter.setGeometry(QtCore.QRect(60, 60, 301, 441))
        self.bg_filter.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0,x2:0,y2:0.715909, stop:0 rgba(0,0,0,50), stop:0.375 rgba(0,0,0,80),stop:0.835227 rgba(0,0,0,80));\n"
"border-radius: 20px;")
        self.bg_filter.setText("")
        self.bg_filter.setObjectName("bg_filter")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 381, 521))
        self.widget.setObjectName("widget")
        self.bg = QtWidgets.QLabel(self.widget)
        self.bg.setGeometry(QtCore.QRect(10, 40, 320, 480))
        self.bg.setStyleSheet("border-image: url(:/Image/320480_2.jpg);\n"
"border-radius: 20px;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(80, 270, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));    \n"
"    color: rgba(255,255,255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));     \n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.load_btn = QtWidgets.QPushButton(Dialog)
        self.load_btn.setGeometry(QtCore.QRect(80, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.load_btn.setFont(font)
        self.load_btn.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));    \n"
"    color: rgba(255,255,255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));     \n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.load_btn.setObjectName("load_btn")
        self.exit_btn = QtWidgets.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(80, 440, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));    \n"
"    color: rgba(255,255,255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));     \n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}")
        self.exit_btn.setObjectName("exit_btn")
        self.widget.raise_()
        self.bg_2.raise_()
        self.widget_2.raise_()
        self.bg_filter.raise_()
        self.title.raise_()
        self.save_dir.raise_()
        self.save_btn.raise_()
        self.load_btn.raise_()
        self.exit_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.save_dir_2.setPlaceholderText(_translate("Dialog", "Directory"))
        self.load_file_2.setPlaceholderText(_translate("Dialog", "Load"))
        self.title.setText(_translate("Dialog", "Mask maker"))
        self.save_btn.setText(_translate("Dialog", "Label"))
        self.load_btn.setText(_translate("Dialog", "Image"))
        self.exit_btn.setText(_translate("Dialog", "Exit"))

    def SetConnect(self):
        self.save_btn.clicked.connect(self.save_button_clicked)
        self.load_btn.clicked.connect(self.load_button_clicked)
        self.exit_btn.clicked.connect(self.exit_button_clicked)

    def save_button_clicked(self):
        self.label_dir = QFileDialog.getExistingDirectory(QtWidgets.QWidget(), 'Label location', QDir.currentPath())
        if self.label_dir is not None:
            self.save_dir.setText(self.label_dir)

    def load_button_clicked(self):
        if self.label_dir is not None:
            fname = QFileDialog.getOpenFileName(QtWidgets.QWidget(), "Open an image file", QDir.currentPath(),
                                                "Image Files (*.png *.jpg *.bmp)") # "JPG files (*.jpg);;PNG files (*.png)")
            if fname == ('',''):
                return
            else:
                LabelMe(dirname=self.label_dir, fileLocation=fname[0])
        else:
            self.save_dir.setText("Set the label directory first")

    def exit_button_clicked(self):
        sys.exit(0)

class LabelMe:

    global points
    points = []

    def __init__(self, dirname, fileLocation):
        self.dirname = dirname
        self.file_loc = fileLocation
        self.main()

    def click_event(self, event, x, y, flags, param):
        """ Detects mouse left click and drag, and draws lines between the coordinates mouse cursor's passed through
        """
        if flags == cv2.EVENT_FLAG_LBUTTON: # Left mouse click / drag
            points.append((x,y))
        if flags == cv2.EVENT_FLAG_RBUTTON:  # Right mouse click / drag
            del points[-1]

    def main(self):
        img = cv2.imread(self.file_loc)
        cv2.namedWindow('image', flags=cv2.WINDOW_GUI_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while(True):
            cv2.setMouseCallback('image', self.click_event, img)
            img_copy = img.copy()
            if len(points) > 1:
                for i in range(len(points) - 1):
                    cv2.line(img_copy, points[i], points[i + 1], 255, 3, 16)
            cv2.imshow('image', img_copy)

            key = cv2.waitKey(5)
            # Exit
            if key == ord('z'):
                points.clear()
                break
            # Extract the mask and save it
            if key == ord('s'):
                mask = np.zeros_like(img)
                if len(points) != 0:
                    file_name = self.file_loc.split('/')[-1]
                    # cv2.drawContours(image, contours, contour index,color, thickness)
                    cv2.drawContours(mask, np.array([points]), -1, (255,255,255), -1)
                    # contour index > 0, each contour. contour index <0 -> all
                    # thickness > 0, outline. thickness < 0 -> area
                    cv2.imwrite(self.dirname + '/' + file_name[:-4] + '_mask' + file_name[-4:], mask)

        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog()
    window.form.show()
    sys.exit(app.exec_())