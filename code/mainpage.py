import sys
import os
from gui.ui_T_Rex_GUI import Ui_MainWindow
from gui import qrc_ico_rc
from PyQt5 import QtCore,QtGui,QtWidgets,QtWebEngineWidgets
from PyQt5.QtGui import QIcon
import time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.tabs = self.ui.tabWidget
        self.setWindowTitle('主窗口')
        self.setWindowIcon(QIcon(':/ico/trex.png'))
        self.settings = QtCore.QSettings("miner_config.ini", QtCore.QSettings.IniFormat)

        # self.ui.coinkind_comboBox.setCurrentIndex(7) #设置以太币为默认值
        self.ui.startmine_pushButton.setEnabled(False)
        self.ui.findprogram_pushButton.clicked.connect(self.findProgram)
        self.ui.startmine_pushButton.clicked.connect(self.startRun)

        self.ui.coinkind_comboBox.currentTextChanged.connect(self.getCoin)
        self.ui.link_comboBox.currentTextChanged.connect(self.getLink)
        self.ui.server_lineEdit.textEdited.connect(self.getServerIp)
        self.ui.port_lineEdit.textEdited.connect(self.getPort)
        self.ui.wallet_lineEdit.textChanged.connect(self.getWallet)

        self.refill() #还原记录的数据到GUI界面

        self.process = QtCore.QProcess()
        self.process.readyReadStandardOutput.connect(self.addStdOut)


    def refill(self):
        self.ui.coinkind_comboBox.setCurrentText(self.settings.value("Coinkind"))
        self.ui.server_lineEdit.setText(self.settings.value("SERVER/server_ip"))
        self.ui.port_lineEdit.setText(self.settings.value("SERVER/port"))
        self.ui.link_comboBox.setCurrentText(self.settings.value("SERVER/link"))
        self.ui.wallet_lineEdit.setText(self.settings.value("Wallet"))
        self.ui.miner_lineEdit.setText(self.settings.value("Progroam"))
        coinkind = self.ui.coinkind_comboBox.currentText()
        server_ip = self.ui.server_lineEdit.text()
        server_port = self.ui.port_lineEdit.text()
        link = self.ui.link_comboBox.currentText()
        wallet = self.ui.wallet_lineEdit.text()
        progroam = self.ui.miner_lineEdit.text()
        if coinkind and server_ip and server_port and link and wallet and progroam:
            self.ui.startmine_pushButton.setEnabled(True)

    def getCoin(self):
        coin = self.ui.coinkind_comboBox.currentText()
        self.settings.setValue("Coinkind",coin)
        self.refill()

    def getServerIp(self):
        server_ip = self.ui.server_lineEdit.text()
        self.settings.setValue("SERVER/server_ip", server_ip)
        self.refill()

    def getPort(self):
        port = self.ui.port_lineEdit.text()
        self.settings.setValue("SERVER/port",port)
        self.refill()

    def getLink(self):
        link = self.ui.link_comboBox.currentText()
        self.settings.setValue("SERVER/link",link)
        self.refill()

    def getWallet(self):
        wallet = self.ui.wallet_lineEdit.text()
        self.settings.setValue("Wallet",wallet)
        self.refill()

    def findProgram(self):
        program = QtWidgets.QFileDialog.getOpenFileName(self,"选取文件夹","./","程序(*.exe)")
        self.ui.miner_lineEdit.setText(program[0])
        self.settings.setValue("Progroam",program[0])
        self.refill()

    def startRun(self):
        program = self.ui.miner_lineEdit.text()
        coin = self.ui.coinkind_comboBox.currentText()
        stratum = "stratum"+self.ui.link_comboBox.currentText()+"://"+self.ui.server_lineEdit.text()+":"+self.ui.port_lineEdit.text()
        wallet = self.ui.wallet_lineEdit.text()
        name = 'rig0'
        self.process.setProgram(program)
        self.process.setArguments(['-a',coin,'-o',stratum,'-u',wallet,'-p','x','-w',name])
        self.process.start()
        time.sleep(5)
        self.showInformation()

    def addStdOut(self):
        output = bytes(self.process.readAllStandardOutput()).decode()
        self.ui.textEdit.append(output)

    def showInformation(self):
        url = QtCore.QUrl("http://127.0.0.1:4067/trex")
        webview = QtWebEngineWidgets.QWebEngineView()
        webview.load(url)
        webview.show()
        self.tabs.addTab(webview, "监控界面")
        self.tabs.setCurrentIndex(1)


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(APP.exec_())