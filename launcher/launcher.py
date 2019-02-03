# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# launcher.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This is main cosmica launcher
# ---------------------------------------------------------------------------
from PyQt4 import QtGui
import sys
import design
import os
from xmlrpclib import ServerProxy

class Launcher(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.register_user)
        self.btnLogin.clicked.connect(self.login_user)
        self.id = 0
        self.email = ''
        self.nickname = ''

    #def browse_folder(self):
        #self.listWidget.clear() # In case there are any existing elements in the list
        #directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                           #"Pick a folder")
        ## execute getExistingDirectory dialog and set the directory variable to be equal
        ## to the user selected directory

        #if directory: # if user didn't pick a directory don't continue
            #for file_name in os.listdir(directory): # for all files, if any, in the directory
                #self.listWidget.addItem(file_name)  # add file to the listWidget
    def register_user(self):
        myInfo = {'email':str(self.txtNewEmail.text()), 'nickname':str(self.txtNickname.text()), 'password':str(self.txtNewPassword.text())}
        server = ServerProxy('http://localhost:8090/')
        result = server.register_new_player(myInfo)
        if result == 1:
            self.mainMenu.setCurrentIndex(1)
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Welcome to Cosmica %s" % str(self.txtNickname.text()))
            msg.exec_()
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("Error in Registration: %s" % result)
            msg.exec_()        
            
    def login_user(self):
        myInfo = {'email':str(self.txtEmail.text()), 'password':str(self.txtPassword.text())}
        server = ServerProxy('http://localhost:8090/')
        result = server.login_player(myInfo)
        if len(result) == 4:
            self.id = result[0]
            self.email = result[1]
            self.nickname = result[2]
            self.mainMenu.setCurrentIndex(1)
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText('Welcome to Cosmica %s' % self.nickname)
            msg.exec_()
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText('Login Error:%s' % result)
            msg.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    form = Launcher()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main() 