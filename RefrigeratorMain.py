import sys

#For PyQt5 :
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from PyQt5 import QtCore, QtGui

from AllPages.UserUIscreenPage1_home import Page1_WelcomeScreen 
from AllPages.UserUIscreenPage2_choosebottles import Page2_ChooseBottles
from AllPages.UserUIscreenPage3_facereg import Page3_FaceReg
from AllPages.UserUIscreenPage4_inforeceipt import Page4_InfoReceipt
from AllPages.UserUIscreenPage5_ensure import Page5_Ensure
from AllPages.UserUIscreenPage6_success import Page6_Success



class mainWin(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        #self.setGeometry(50, 50, 400, 450)
        #self.setObjectName("MainWindow") # big MainWindow
        self.setFixedSize(800, 480)
        
        self.name = 'น้ำดื่ม ฿5'
        self.bottle_value = 1
        self.price = 5
        self.totalPrice = 0

        # data goods here
        self.goods = [
            {
                "name": self.name,
                "value": self.bottle_value,
                "price": self.price
            },
        ]

        # data user here
        self.users = [
            {
                "username": "sirawit",
                "first_name": "สิรวิชญ์",
                "last_name": "สุขวัฒนาวิทย์", 
                "credit": 200 
            },
            {
                "username": "watcharaporn",
                "first_name": "วัชราภรณ์",
                "last_name": "ชาแท่น", 
                "credit": 150 
            },

            
        ]

        # start what page ?
        self.startFirst()
        #self.startFouth()
        #self.startSixth()


    def startFirst(self):
        self.firstPage = Page1_WelcomeScreen(self)
        self.setWindowTitle("Welcome Screen")

        # CentralWidget
        self.setCentralWidget(self.firstPage)

        # Go to next page if click
        self.firstPage.button1.clicked.connect(self.startSecond)
        self.show()

    def startSecond(self):
        self.secondPage = Page2_ChooseBottles(self)
        self.setWindowTitle("Choose Bottles")
        
        # CentralWidget
        self.setCentralWidget(self.secondPage)

        # Change value
        self.updateSecondPage()
        self.secondPage.plusbutton.clicked.connect(self.plus)
        self.secondPage.minusbutton.clicked.connect(self.minus)

        # Go to next page if click
        self.secondPage.nextpagebutton.clicked.connect(self.checkIfEmpty)
        
        self.show()
    
    def checkIfEmpty(self):
        if self.bottle_value != 0:  
            self.startThird()

    # PlusData Function
    def plus(self):
        if self.bottle_value < 4: # old: 98 new: 4 because user can't carry more than 4 bottles 
            self.bottle_value += 1
        self.updateSecondPage()

    # MinusData Function
    def minus(self):
        if self.bottle_value > 1: # old: 0 new: 1 because comfortable to use
            self.bottle_value -= 1
        self.updateSecondPage()
    
    def updateSecondPage(self):
        self.updateGoods()
        self.secondPage.lcdNumber.display(self.bottle_value)
        if self.bottle_value != 0:
            self.secondPage.nextpagebutton.setStyleSheet("background-color: rgb(9, 115, 227); color: rgb(255, 255, 255);")
        else:
            self.secondPage.nextpagebutton.setStyleSheet("background-color: rgb(232, 232, 232); color: rgb(60, 60, 60);")

    def updateGoods(self):
        for good in self.goods:
            good['value'] = self.bottle_value
            good['price'] = self.bottle_value*self.price


    def startThird(self):
        self.thirdPage = Page3_FaceReg(self)
        self.setWindowTitle("Face Recognition")

        # CentralWidget
        self.setCentralWidget(self.thirdPage)

        # Go to previous page if click
        #self.thirdPage.cancelbutton.clicked.connect(self.startSecond)
        
        # Go to next page if face detection is valid  
        pass # working on it..
        
        #test go to page 4
        self.thirdPage.cancelbutton.clicked.connect(self.startFourth)
        
        self.show()

    def startFourth(self):
        self.fourthPage = Page4_InfoReceipt(self)
        self.setWindowTitle("Infomation Receipt")
        
        # CentralWidget
        self.setCentralWidget(self.fourthPage)

        # Load data from server
        self.fourthPage.loadData(self.goods, self.users, "sirawit") # select username

        # Go to previous page if click
        self.fourthPage.cancelbutton.clicked.connect(self.startThird)
        # Go to next page if click
        self.fourthPage.nextpagebutton.clicked.connect(self.startFifth)
        self.show()

        

    def startFifth(self):
        self.fifthPage = Page5_Ensure(self)
        self.setWindowTitle("Infomation Receipt")
        
        # CentralWidget
        self.setCentralWidget(self.fifthPage)

        # Load data from server
        self.totalPrice = self.fifthPage.loadData(self.goods, self.users, "sirawit") # select username

        # Go to previous page if click
        self.fifthPage.cancelbutton.clicked.connect(self.startFourth)
        # Go to next page if click
        self.fifthPage.nextpagebutton.clicked.connect(self.startSixth)
        self.show()

    def startSixth(self):
        self.sixthPage = Page6_Success(self)
        self.setWindowTitle("Success")
        
        # CentralWidget
        self.setCentralWidget(self.sixthPage)

        # Load data from server
        self.sixthPage.loadData(self.totalPrice, self.users, "sirawit") # select username

        # Go to next page if click
        self.sixthPage.nextpagebutton.clicked.connect(self.startFirst)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWin()
    sys.exit(app.exec_())