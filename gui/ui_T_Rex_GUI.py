# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\T-Rex-GUI\gui/T_Rex_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.coinkind_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.coinkind_comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.coinkind_comboBox.setObjectName("coinkind_comboBox")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.coinkind_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.coinkind_comboBox)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.link_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.link_comboBox.setObjectName("link_comboBox")
        self.link_comboBox.addItem("")
        self.link_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.link_comboBox)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.server_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.server_lineEdit.setObjectName("server_lineEdit")
        self.horizontalLayout_4.addWidget(self.server_lineEdit)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.port_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.horizontalLayout_5.addWidget(self.port_lineEdit)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wallet_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.wallet_lineEdit.setFont(font)
        self.wallet_lineEdit.setObjectName("wallet_lineEdit")
        self.verticalLayout_5.addWidget(self.wallet_lineEdit)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.miner_lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.miner_lineEdit.setObjectName("miner_lineEdit")
        self.verticalLayout_4.addWidget(self.miner_lineEdit)
        self.findprogram_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.findprogram_pushButton.setObjectName("findprogram_pushButton")
        self.verticalLayout_4.addWidget(self.findprogram_pushButton)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_9.addWidget(self.textEdit)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addWidget(self.groupBox_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.startmine_pushButton = QtWidgets.QPushButton(self.tab)
        self.startmine_pushButton.setMinimumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.startmine_pushButton.setFont(font)
        self.startmine_pushButton.setObjectName("startmine_pushButton")
        self.horizontalLayout_10.addWidget(self.startmine_pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout_11.setStretch(0, 5)
        self.horizontalLayout_11.setStretch(1, 5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.setStretch(0, 3)
        self.verticalLayout_8.setStretch(1, 5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "币种"))
        self.coinkind_comboBox.setItemText(0, _translate("MainWindow", "etchash"))
        self.coinkind_comboBox.setItemText(1, _translate("MainWindow", "astralhash"))
        self.coinkind_comboBox.setItemText(2, _translate("MainWindow", "balloon"))
        self.coinkind_comboBox.setItemText(3, _translate("MainWindow", "bcd"))
        self.coinkind_comboBox.setItemText(4, _translate("MainWindow", "bitcore"))
        self.coinkind_comboBox.setItemText(5, _translate("MainWindow", "c11"))
        self.coinkind_comboBox.setItemText(6, _translate("MainWindow", "dedal"))
        self.coinkind_comboBox.setItemText(7, _translate("MainWindow", "ethash"))
        self.coinkind_comboBox.setItemText(8, _translate("MainWindow", "geek"))
        self.coinkind_comboBox.setItemText(9, _translate("MainWindow", "hmq1725"))
        self.coinkind_comboBox.setItemText(10, _translate("MainWindow", "honeycomb"))
        self.coinkind_comboBox.setItemText(11, _translate("MainWindow", "jeonghash"))
        self.coinkind_comboBox.setItemText(12, _translate("MainWindow", "kawpow"))
        self.coinkind_comboBox.setItemText(13, _translate("MainWindow", "lyra2z"))
        self.coinkind_comboBox.setItemText(14, _translate("MainWindow", "megabtx"))
        self.coinkind_comboBox.setItemText(15, _translate("MainWindow", "megamec"))
        self.coinkind_comboBox.setItemText(16, _translate("MainWindow", "mtp"))
        self.coinkind_comboBox.setItemText(17, _translate("MainWindow", "mtp-tcr"))
        self.coinkind_comboBox.setItemText(18, _translate("MainWindow", "multi"))
        self.coinkind_comboBox.setItemText(19, _translate("MainWindow", "octopus"))
        self.coinkind_comboBox.setItemText(20, _translate("MainWindow", "padihash"))
        self.coinkind_comboBox.setItemText(21, _translate("MainWindow", "pawelhash"))
        self.coinkind_comboBox.setItemText(22, _translate("MainWindow", "phi"))
        self.coinkind_comboBox.setItemText(23, _translate("MainWindow", "polytimos"))
        self.coinkind_comboBox.setItemText(24, _translate("MainWindow", "progpow"))
        self.coinkind_comboBox.setItemText(25, _translate("MainWindow", "progpow-veil"))
        self.coinkind_comboBox.setItemText(26, _translate("MainWindow", "progpow-veriblock"))
        self.coinkind_comboBox.setItemText(27, _translate("MainWindow", "progpowz"))
        self.coinkind_comboBox.setItemText(28, _translate("MainWindow", "sha256q"))
        self.coinkind_comboBox.setItemText(29, _translate("MainWindow", "sha256t"))
        self.coinkind_comboBox.setItemText(30, _translate("MainWindow", "skunk"))
        self.coinkind_comboBox.setItemText(31, _translate("MainWindow", "sonoa"))
        self.coinkind_comboBox.setItemText(32, _translate("MainWindow", "tensority"))
        self.coinkind_comboBox.setItemText(33, _translate("MainWindow", "timetravel"))
        self.coinkind_comboBox.setItemText(34, _translate("MainWindow", "tribus"))
        self.coinkind_comboBox.setItemText(35, _translate("MainWindow", "x11r"))
        self.coinkind_comboBox.setItemText(36, _translate("MainWindow", "x16r"))
        self.coinkind_comboBox.setItemText(37, _translate("MainWindow", "x16rt"))
        self.coinkind_comboBox.setItemText(38, _translate("MainWindow", "x16rv2"))
        self.coinkind_comboBox.setItemText(39, _translate("MainWindow", "x16s"))
        self.coinkind_comboBox.setItemText(40, _translate("MainWindow", "x17"))
        self.coinkind_comboBox.setItemText(41, _translate("MainWindow", "x21s"))
        self.coinkind_comboBox.setItemText(42, _translate("MainWindow", "x22i"))
        self.coinkind_comboBox.setItemText(43, _translate("MainWindow", "x25x"))
        self.coinkind_comboBox.setItemText(44, _translate("MainWindow", "x33"))
        self.groupBox_2.setTitle(_translate("MainWindow", "矿池"))
        self.label.setText(_translate("MainWindow", "链接方式"))
        self.link_comboBox.setItemText(0, _translate("MainWindow", "ssl"))
        self.link_comboBox.setItemText(1, _translate("MainWindow", "tcp"))
        self.label_2.setText(_translate("MainWindow", "矿池服务器地址"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.groupBox_3.setTitle(_translate("MainWindow", "钱包地址"))
        self.groupBox_5.setTitle(_translate("MainWindow", "T-Rex程序地址"))
        self.findprogram_pushButton.setText(_translate("MainWindow", "打开程序"))
        self.groupBox_4.setTitle(_translate("MainWindow", "命令行结果显示"))
        self.startmine_pushButton.setText(_translate("MainWindow", "开始挖矿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "配置界面"))
