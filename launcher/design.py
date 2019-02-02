# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Fri Feb 01 19:46:13 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1064, 851)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(_fromUtf8("#login_register {\n"
"    background-color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-image: url(:/images/background.png);\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.login_register = QtGui.QWidget()
        self.login_register.setObjectName(_fromUtf8("login_register"))
        self.formLayout_2 = QtGui.QFormLayout(self.login_register)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminator Two"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_4)
        self.label = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.txtEmail = QtGui.QLineEdit(self.login_register)
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtEmail)
        self.label_2 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtPassword = QtGui.QLineEdit(self.login_register)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtPassword)
        self.btnLogin = QtGui.QPushButton(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.btnLogin)
        self.label_7 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtNewEmail = QtGui.QLineEdit(self.login_register)
        self.txtNewEmail.setObjectName(_fromUtf8("txtNewEmail"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtNewEmail)
        self.label_8 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txtNickname = QtGui.QLineEdit(self.login_register)
        self.txtNickname.setObjectName(_fromUtf8("txtNickname"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtNickname)
        self.label_9 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.txtNewPassword = QtGui.QLineEdit(self.login_register)
        self.txtNewPassword.setObjectName(_fromUtf8("txtNewPassword"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.txtNewPassword)
        self.btnRegister = QtGui.QPushButton(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName(_fromUtf8("btnRegister"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.btnRegister)
        self.label_6 = QtGui.QLabel(self.login_register)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminator Two"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_6)
        self.stackedWidget.addWidget(self.login_register)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.stackedWidget)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminator Two"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Cosmica Launcher", None))
        self.label_4.setText(_translate("MainWindow", "Login:", None))
        self.label.setText(_translate("MainWindow", "Enter Email Address:", None))
        self.label_2.setText(_translate("MainWindow", "Enter Password:", None))
        self.btnLogin.setText(_translate("MainWindow", "Login", None))
        self.label_7.setText(_translate("MainWindow", "Enter Email Address:", None))
        self.label_8.setText(_translate("MainWindow", "Enter Nickname:", None))
        self.label_9.setText(_translate("MainWindow", "Enter Password:", None))
        self.btnRegister.setText(_translate("MainWindow", "Register to NeuroJump", None))
        self.label_6.setText(_translate("MainWindow", "Register:", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#ffaa00;\">C O S M I C A</span></p></body></html>", None))

import resources_rc
