# Page 5 By Pop  
        # waiting for comment in future
        # waiting for more clean code

from PyQt5 import QtCore, QtGui, QtWidgets


class Page5_Ensure(QtWidgets.QWidget):

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
        self.version_label.setGeometry(QtCore.QRect(717, 440, 81, 41))
        self.version_label.setFont(font)
        self.version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")

        self.table_frame = QtWidgets.QFrame(self)
        self.table_frame.setGeometry(QtCore.QRect(100, 110, 601, 241))
        self.table_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_frame.setObjectName("table_frame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.table_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableGoods = QtWidgets.QTableWidget(self.table_frame)
        self.tableGoods.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableGoods.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableGoods.setGridStyle(QtCore.Qt.SolidLine)
        self.tableGoods.setObjectName("tableGoods")
        self.tableGoods.setColumnCount(3)
        self.tableGoods.setRowCount(0)

        # Customize Table property
        self.tableGoods.setColumnWidth(0,350)
        self.tableGoods.setColumnWidth(1,110)
        self.tableGoods.setColumnWidth(2,120)
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
        self.verticalLayout.setStretch(1, 20)

        self.bgblack_label = QtWidgets.QLabel(self)
        self.bgblack_label.setEnabled(True)
        self.bgblack_label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bgblack_label.setMinimumSize(QtCore.QSize(800, 480))
        self.bgblack_label.setMaximumSize(QtCore.QSize(800, 480))
        self.bgblack_label.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
        self.bgblack_label.setText("")
        self.bgblack_label.setScaledContents(True)
        self.bgblack_label.setObjectName("bgblack_label")

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

        self.subbg_label = QtWidgets.QLabel(self)
        self.subbg_label.setGeometry(QtCore.QRect(70, 30, 661, 411))
        self.subbg_label.setStyleSheet("background-color: rgb(166, 214, 255)")
        self.subbg_label.setText("")
        self.subbg_label.setObjectName("subbg_label")

        self.cancelaccept_widget = QtWidgets.QWidget(self)
        self.cancelaccept_widget.setGeometry(QtCore.QRect(240, 370, 301, 55))
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

        self.bg_label.raise_()
        self.bgblack_label.raise_()
        self.subbg_label.raise_()
        self.version_label.raise_()
        self.table_frame.raise_()
        self.AddStuff_Label_3.raise_()
        self.cancelaccept_widget.raise_()

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)


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
        

        _translate = QtCore.QCoreApplication.translate
        self.totalmoney_label.setText(_translate("MainWindow", str("{:.2f}".format(totalPrice))))

        return totalPrice


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))
        item = self.tableGoods.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "รายการสินค้า"))
        item = self.tableGoods.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "จำนวน"))
        item = self.tableGoods.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ราคา"))
        self.total_label.setText(_translate("MainWindow", "รวม"))
        self.totalmoney_label.setText(_translate("MainWindow", "10.00"))
        self.AddStuff_Label_3.setText(_translate("MainWindow", "คุณต้องการทำรายการสั่งซื้อหรือไม่"))
        self.cancelbutton.setText(_translate("MainWindow", "ยกเลิก"))
        self.nextpagebutton.setText(_translate("MainWindow", "ยืนยัน"))
        self.totalmoneyฺbaht_label.setText(_translate("MainWindow", "฿"))
        

