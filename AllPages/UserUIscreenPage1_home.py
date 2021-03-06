# Page 1 By Pop  


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Page1_WelcomeScreen(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # backgroundFrame
        self.bgFRAME = QtWidgets.QFrame(self)
        self.bgFRAME.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.bgFRAME.setAutoFillBackground(False)
        self.bgFRAME.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.bgFRAME.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgFRAME.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgFRAME.setObjectName("bgFRAME")

        # version label
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.version_label = QtWidgets.QLabel(self.bgFRAME)
        self.version_label.setGeometry(QtCore.QRect(717, 440, 81, 41))
        self.version_label.setFont(font)
        self.version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")

        # background skyblue
        self.bg_label = QtWidgets.QLabel(self.bgFRAME)
        self.bg_label.setEnabled(True)
        self.bg_label.setGeometry(QtCore.QRect(0, 1, 800, 480))
        self.bg_label.setMinimumSize(QtCore.QSize(800, 480))
        self.bg_label.setMaximumSize(QtCore.QSize(800, 480))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("QT_resource/bgsky.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setObjectName("bg_label")

        # touch here label
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.touchhere_label = QtWidgets.QLabel(self.bgFRAME)
        self.touchhere_label.setGeometry(QtCore.QRect(220, 320, 370, 41))
        self.touchhere_label.setFont(font)
        self.touchhere_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.touchhere_label.setStyleSheet("QLabel{color: rgb(0, 0, 83)}")
        self.touchhere_label.setAlignment(QtCore.Qt.AlignCenter)
        self.touchhere_label.setObjectName("touchhere_label")

        # white background (behide welcome label)
        self.whitebg_label = QtWidgets.QLabel(self.bgFRAME)
        self.whitebg_label.setGeometry(QtCore.QRect(-10, 90, 821, 171))
        self.whitebg_label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255);}")
        self.whitebg_label.setText("")
        self.whitebg_label.setObjectName("whitebg_label")

        # welcome label
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_label = QtWidgets.QLabel(self.bgFRAME)
        self.Welcome_label.setGeometry(QtCore.QRect(20, 150, 753, 59))
        self.Welcome_label.setFont(font)
        self.Welcome_label.setAutoFillBackground(False)
        self.Welcome_label.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.Welcome_label.setScaledContents(False)
        self.Welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_label.setObjectName("Welcome_label")

        # button press to next page
        self.button1 = QtWidgets.QPushButton(self.bgFRAME)
        self.button1.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.button1.setObjectName("button1")

        # order arrangement 
        self.bg_label.raise_()
        self.version_label.raise_()
        self.whitebg_label.raise_()
        self.touchhere_label.raise_()
        self.Welcome_label.raise_()
        self.button1.raise_()

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Refrigerator MK II V.1.0.0"))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))
        self.touchhere_label.setText(_translate("MainWindow", "แตะที่นี่เพื่อไปหน้าถัดไป"))
        self.Welcome_label.setText(_translate("MainWindow", "Welcome to Smart Refrigerator MK II"))
