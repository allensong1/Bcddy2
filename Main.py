import sys
from formAutoClick import Ui_formAutoClick
from MainForm import Ui_MainForm
from PyQt5 import QtWidgets


#region 窗口类相关函数
class myMainForm(QtWidgets.QWidget,Ui_MainForm):
    def __init__(self):
        super(myMainForm,self).__init__()
        self.setupUi(self)

    def testButton1(self):
        self.hide()
        self.newform = myformAutoClick()
        self.newform.show()

class myformAutoClick(QtWidgets.QWidget,Ui_formAutoClick):
    def __init__(self):
        super(myformAutoClick,self).__init__()
        self.setupUi(self)

    def closeAndReturn1(self):
        aaa = self.lineEdit.text()
        self.hide()
        self.mai = myMainForm()
        self.mai.lineEdit.setText(aaa)
        self.mai.show()

#endregion


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_form = myMainForm()
    my_form.show()
    sys.exit(app.exec_())