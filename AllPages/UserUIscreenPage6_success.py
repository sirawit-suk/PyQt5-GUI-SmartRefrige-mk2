# Page 6 By Pop  
        # waiting for comment in future
        # waiting for more clean code

from PyQt5 import QtCore, QtGui, QtWidgets


class Page6_Success(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.bg_label = QtWidgets.QLabel(self)
        self.bg_label.setEnabled(True)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bg_label.setMinimumSize(QtCore.QSize(800, 480))
        self.bg_label.setMaximumSize(QtCore.QSize(800, 480))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("QT_resource/bgsky.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setObjectName("bg_label")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.version_label = QtWidgets.QLabel(self)
        self.version_label.setGeometry(QtCore.QRect(707, 440, 91, 41))
        self.version_label.setFont(font)
        self.version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")

        self.bgblack_label = QtWidgets.QLabel(self)
        self.bgblack_label.setEnabled(True)
        self.bgblack_label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgblack_label.setMinimumSize(QtCore.QSize(800, 480))
        self.bgblack_label.setMaximumSize(QtCore.QSize(800, 480))
        self.bgblack_label.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        self.bgblack_label.setText("")
        self.bgblack_label.setScaledContents(True)
        self.bgblack_label.setObjectName("bgblack_label")

        self.subbg_label = QtWidgets.QLabel(self)
        self.subbg_label.setGeometry(QtCore.QRect(120, 30, 541, 411))
        self.subbg_label.setStyleSheet("background-color: rgb(166, 214, 255)")
        self.subbg_label.setText("")
        self.subbg_label.setObjectName("subbg_label")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AddStuff_Label_3 = QtWidgets.QLabel(self)
        self.AddStuff_Label_3.setGeometry(QtCore.QRect(90, 50, 618, 47))
        self.AddStuff_Label_3.setFont(font)
        self.AddStuff_Label_3.setAutoFillBackground(False)
        self.AddStuff_Label_3.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.AddStuff_Label_3.setScaledContents(False)
        self.AddStuff_Label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.AddStuff_Label_3.setObjectName("AddStuff_Label_3")

        self.gridFrame = QtWidgets.QFrame(self)
        self.gridFrame.setGeometry(QtCore.QRect(180, 120, 421, 201))
        self.gridFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridFrame.setObjectName("gridFrame")

        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(30, 0, 30, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2 = QtWidgets.QLabel(self.gridFrame)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5 = QtWidgets.QLabel(self.gridFrame)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4 = QtWidgets.QLabel(self.gridFrame)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6 = QtWidgets.QLabel(self.gridFrame)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label = QtWidgets.QLabel(self.gridFrame)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3 = QtWidgets.QLabel(self.gridFrame)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_7 = QtWidgets.QLabel(self.gridFrame)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_8 = QtWidgets.QLabel(self.gridFrame)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_9 = QtWidgets.QLabel(self.gridFrame)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.line = QtWidgets.QFrame(self.gridFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.gridFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.gridFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 20)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 10)
        self.gridLayout.setRowStretch(3, 8)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.nextpagebutton = QtWidgets.QPushButton(self)
        self.nextpagebutton.setGeometry(QtCore.QRect(320, 350, 150, 60))
        self.nextpagebutton.setFont(font)
        self.nextpagebutton.setStyleSheet("background-color: rgb(9, 115, 227); color: rgb(255, 255, 255);")
        self.nextpagebutton.setObjectName("nextpagebutton")

        self.bg_label.raise_()
        self.bgblack_label.raise_()
        self.version_label.raise_()
        self.subbg_label.raise_()
        self.AddStuff_Label_3.raise_()
        self.gridFrame.raise_()
        self.nextpagebutton.raise_()

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def loadData(self, totalPrice=0.0, users=[], username=''):
        
        userCredit = 0.0
        changeCredit = 0.0

        for user in users:
            if user['username'] == username:
                userCredit = user['credit']
        
        ### Wait to do for checking if it can't pay if has lower than or negative(-)
        changeCredit = userCredit - totalPrice

        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", str("{:.2f}".format(userCredit))))
        self.label_4.setText(_translate("MainWindow", str("{:.2f}".format(totalPrice))))
        self.label_6.setText(_translate("MainWindow", str("{:.2f}".format(changeCredit))))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))
        self.AddStuff_Label_3.setText(_translate("MainWindow", "ทำรายการสำเร็จ"))
        self.label_2.setText(_translate("MainWindow", "ชำระเงิน"))
        self.label_5.setText(_translate("MainWindow", "ยอดเงินคงเหลือ      "))
        self.label.setText(_translate("MainWindow", "เงินในบัญชี"))
        self.label_7.setText(_translate("MainWindow", "บาท"))
        self.label_8.setText(_translate("MainWindow", "บาท"))
        self.label_9.setText(_translate("MainWindow", "บาท"))
        self.nextpagebutton.setText(_translate("MainWindow", "ยืนยัน"))
