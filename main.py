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

        dpi_new=0;sens_old=0;dpi_old=0

        dpi_old  = int ( self.ui.textEdit.toPlainText() )
        sens_old = int ( self.ui.textEdit_2.toPlainText() )
        dpi_new  = int ( self.ui.textEdit_3.toPlainText() )


        if dpi_old != ' ' and sens_old != ' ' and dpi_new != ' ':
            sens_new = dpi_old/dpi_new*sens_old
            self.ui.label_4.setText('Your new sensetivity is: ' + str(sens_new))
        else:
            self.ui.label_4.setText('Enter correct values!')
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
