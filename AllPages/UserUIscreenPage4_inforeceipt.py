# Page 4 By Pop  
        # waiting for comment in future
        # waiting for more clean code

from PyQt5 import QtCore, QtGui, QtWidgets


class Page4_InfoReceipt(QtWidgets.QWidget):
    
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

        self.cancelaccept_widget = QtWidgets.QWidget(self)
        self.cancelaccept_widget.setGeometry(QtCore.QRect(240, 410, 301, 55))
        self.cancelaccept_widget.setObjectName("cancelaccept_widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cancelaccept_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.cancelbutton = QtWidgets.QPushButton(self.cancelaccept_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbutton.sizePolicy().hasHeightForWidth())
        self.cancelbutton.setSizePolicy(sizePolicy)
        self.cancelbutton.setFont(font)
        self.cancelbutton.setStyleSheet("background-color: rgb(232, 232, 232); color: rgb(59, 59, 59)")
        self.cancelbutton.setObjectName("cancelbutton")

        self.horizontalLayout.addWidget(self.cancelbutton)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nextpagebutton = QtWidgets.QPushButton(self.cancelaccept_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextpagebutton.sizePolicy().hasHeightForWidth())
        self.nextpagebutton.setSizePolicy(sizePolicy)
        self.nextpagebutton.setFont(font)
        self.nextpagebutton.setStyleSheet("background-color: rgb(9, 115, 227); color: rgb(255, 255, 255);")
        self.nextpagebutton.setObjectName("nextpagebutton")

        self.horizontalLayout.addWidget(self.nextpagebutton)

        self.pic_label = QtWidgets.QLabel(self)
        self.pic_label.setGeometry(QtCore.QRect(660, 20, 80, 80))
        self.pic_label.setMaximumSize(QtCore.QSize(80, 80))
        self.pic_label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255);}")
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")

        self.tellmoney_frame = QtWidgets.QFrame(self)
        self.tellmoney_frame.setGeometry(QtCore.QRect(410, 50, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tellmoney_frame.sizePolicy().hasHeightForWidth())
        self.tellmoney_frame.setSizePolicy(sizePolicy)
        self.tellmoney_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tellmoney_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tellmoney_frame.setObjectName("tellmoney_frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tellmoney_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.tellmoney_label = QtWidgets.QLabel(self.tellmoney_frame)
        self.tellmoney_label.setMaximumSize(QtCore.QSize(480, 480))
        self.tellmoney_label.setFont(font)
        self.tellmoney_label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255);}")
        self.tellmoney_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tellmoney_label.setObjectName("tellmoney_label")

        self.horizontalLayout_2.addWidget(self.tellmoney_label)

        self.money_frame = QtWidgets.QFrame(self.tellmoney_frame)
        self.money_frame.setStyleSheet("background-color: rgb(43, 61, 127); color: rgb(255, 255, 255);")
        self.money_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.money_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.money_frame.setObjectName("money_frame")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.money_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.moneynumber = QtWidgets.QLCDNumber(self.money_frame)
        self.moneynumber.setStyleSheet("")
        self.moneynumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.moneynumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.moneynumber.setSmallDecimalPoint(False)
        self.moneynumber.setDigitCount(6)
        self.moneynumber.setProperty("value", 0.0)
        self.moneynumber.setProperty("intValue", 0)
        self.moneynumber.setObjectName("moneynumber")

        self.horizontalLayout_3.addWidget(self.moneynumber)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.bath_label = QtWidgets.QLabel(self.money_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bath_label.sizePolicy().hasHeightForWidth())
        self.bath_label.setSizePolicy(sizePolicy)
        self.bath_label.setMaximumSize(QtCore.QSize(480, 480))
        self.bath_label.setFont(font)
        self.bath_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bath_label.setAutoFillBackground(False)
        self.bath_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.bath_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bath_label.setWordWrap(False)
        self.bath_label.setObjectName("bath_label")

        self.horizontalLayout_3.addWidget(self.bath_label)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 5)

        self.horizontalLayout_2.addWidget(self.money_frame)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 6)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.name_label = QtWidgets.QLabel(self)
        self.name_label.setGeometry(QtCore.QRect(60, 50, 331, 41))
        self.name_label.setMaximumSize(QtCore.QSize(480, 480))
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.name_label.setLineWidth(1)
        self.name_label.setObjectName("name_label")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.version_label = QtWidgets.QLabel(self)
        self.version_label.setGeometry(QtCore.QRect(717, 440, 81, 41))
        self.version_label.setFont(font)
        self.version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")

        self.table_frame = QtWidgets.QFrame(self)
        self.table_frame.setGeometry(QtCore.QRect(60, 110, 681, 251))
        self.table_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_frame.setObjectName("table_frame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.table_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Table start 

        self.tableGoods = QtWidgets.QTableWidget(self.table_frame)
        self.tableGoods.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableGoods.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableGoods.setGridStyle(QtCore.Qt.SolidLine)
        self.tableGoods.setObjectName("tableGoods")
        self.tableGoods.setColumnCount(3)
        self.tableGoods.setRowCount(0)

        # Customize Table property
        self.tableGoods.setColumnWidth(0,400)
        self.tableGoods.setColumnWidth(1,110)
        self.tableGoods.setColumnWidth(2,150)
        self.tableGoods.horizontalHeader().setStretchLastSection(True)

        # font for all header (3 header columns )
        header_font = QtGui.QFont()
        header_font.setFamily("Leelawadee UI")
        header_font.setPointSize(13)
        header_font.setBold(True)
        header_font.setWeight(75)

        header_item_1 = QtWidgets.QTableWidgetItem()
        header_item_2 = QtWidgets.QTableWidgetItem()
        header_item_3 = QtWidgets.QTableWidgetItem()
        header_item_1.setFont(header_font)
        header_item_2.setFont(header_font)
        header_item_3.setFont(header_font)

        self.tableGoods.setHorizontalHeaderItem(0, header_item_1)
        self.tableGoods.setHorizontalHeaderItem(1, header_item_2)
        self.tableGoods.setHorizontalHeaderItem(2, header_item_3)

        # font for all data (3 data columns )
        data_font = QtGui.QFont()
        data_font.setFamily("Leelawadee UI")
        data_font.setPointSize(12)
        data_font.setBold(False)
        #data_font.setWeight(75)

        self.tableGoods.setFont(data_font)

        '''
        self.tableGoods.horizontalHeader().setVisible(True)
        self.tableGoods.horizontalHeader().setCascadingSectionResizes(False)
        self.tableGoods.horizontalHeader().setDefaultSectionSize(200)
        self.tableGoods.horizontalHeader().setHighlightSections(True)
        self.tableGoods.horizontalHeader().setMinimumSectionSize(100)
        self.tableGoods.horizontalHeader().setSortIndicatorShown(False)
        self.tableGoods.horizontalHeader().setStretchLastSection(True)
        self.tableGoods.verticalHeader().setStretchLastSection(False)
        '''
        # Table end 

        self.verticalLayout.addWidget(self.tableGoods)

        self.horizontalFrame = QtWidgets.QFrame(self.table_frame)
        self.horizontalFrame.setObjectName("horizontalFrame")

        self.totalamount = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.totalamount.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.totalamount.setContentsMargins(0, 0, 0, 0)
        self.totalamount.setObjectName("totalamount")

        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_label = QtWidgets.QLabel(self.horizontalFrame)
        self.total_label.setFont(font)
        self.total_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_label.setObjectName("total_label")

        self.totalamount.addWidget(self.total_label)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totalmoney_label = QtWidgets.QLabel(self.horizontalFrame)
        self.totalmoney_label.setFont(font)
        self.totalmoney_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.totalmoney_label.setObjectName("totalmoney_label")

        self.totalamount.addWidget(self.totalmoney_label)

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totalmoneyฺbaht_label = QtWidgets.QLabel(self.horizontalFrame)
        self.totalmoneyฺbaht_label.setFont(font)
        self.totalmoneyฺbaht_label.setAlignment(QtCore.Qt.AlignCenter)
        self.totalmoneyฺbaht_label.setObjectName("totalmoneyฺbaht_label")

        self.totalamount.addWidget(self.totalmoneyฺbaht_label)

        # set Stretch

        self.totalamount.setStretch(0, 20)
        self.totalamount.setStretch(1, 3)
        self.totalamount.setStretch(2, 2)

        self.verticalLayout.addWidget(self.horizontalFrame)

        self.verticalLayout.setStretch(0, 90)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

        self.loadData()

    def loadData(self, goods=[], users=[], username=''):
        
        row = 0
        self.tableGoods.setRowCount(len(goods))
        totalPrice = 0.00
        
        for good in goods:
            totalPrice += good["price"]
            col_item_1 = QtWidgets.QTableWidgetItem(good["name"])
            col_item_2 = QtWidgets.QTableWidgetItem(str(good["value"]))
            col_item_3 = QtWidgets.QTableWidgetItem(str("{:.2f}".format(good["price"])))
            col_item_2.setTextAlignment(QtCore.Qt.AlignCenter)
            col_item_3.setTextAlignment(QtCore.Qt.AlignCenter)

            self.tableGoods.setItem(row, 0, col_item_1)
            self.tableGoods.setItem(row, 1, col_item_2)
            self.tableGoods.setItem(row, 2, col_item_3)
            row += 1
        
        fullName = ''
        for user in users:
            if user['username'] == username:
                fullName = 'คุณ'+' '+user['first_name']+' '+user['last_name']
                self.moneynumber.display(user['credit'])


        _translate = QtCore.QCoreApplication.translate
        self.totalmoney_label.setText(_translate("MainWindow", str("{:.2f}".format(totalPrice))))
        self.name_label.setText(_translate("MainWindow", fullName))

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancelbutton.setText(_translate("MainWindow", "ย้อนกลับ"))
        self.nextpagebutton.setText(_translate("MainWindow", "ถัดไป"))
        self.tellmoney_label.setText(_translate("MainWindow", "เงินในบัญชี"))
        self.bath_label.setText(_translate("MainWindow", "บาท"))
        
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))
        item = self.tableGoods.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "รายการสินค้า"))
        item = self.tableGoods.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "จำนวน"))
        item = self.tableGoods.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ราคา (฿)"))
        self.total_label.setText(_translate("MainWindow", "รวม"))
        self.totalmoneyฺbaht_label.setText(_translate("MainWindow", "฿"))