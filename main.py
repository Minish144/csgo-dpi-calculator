import sys
from GUI import *
from PyQt5 import QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.MyFunction)


    def MyFunction(self):
        dpi_old  = str ( self.ui.textEdit.toPlainText() )
        sens_old = str ( self.ui.textEdit_2.toPlainText() )
        dpi_new  = str ( self.ui.textEdit_3.toPlainText() )

        if dpi_old == '' or sens_old == '' or dpi_new == '':
            self.ui.label_4.setText('Enter correct values')
        else:
            sens_new = int(dpi_old)/int(dpi_new)*int(sens_old)
            self.ui.label_4.setText('Your new sensetivity is: ' + str(sens_new))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
