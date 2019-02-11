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
import run

class Launcher(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # login or register (0)
        self.btnRegister.clicked.connect(self.register_user)
        self.btnLogin.clicked.connect(self.login_user)
        
        # main menu (1)
        self.btnLoadNewSingle.clicked.connect(self.load_new_single)
        self.btnLoadContSingle.clicked.connect(self.load_cont_single)
        self.btnLoadJoinMulti.clicked.connect(self.load_join_multi)
        self.btnLoadHostMulti.clicked.connect(self.load_host_multi)
        self.btnLoadContMulti.clicked.connect(self.load_cont_multi)
        
        # all the back buttons
        self.btnBackNewSingle.clicked.connect(self.load_main_menu)
        self.btnBackContMulti.clicked.connect(self.load_main_menu)
        self.btnBackContSingle.clicked.connect(self.load_main_menu)
        self.btnBackJoinMulti.clicked.connect(self.load_main_menu)
        self.btnBackNewMulti.clicked.connect(self.load_main_menu)
        
        # main action buttons
        self.btnNewSingle.clicked.connect(self.start_new_single_game)
        self.btnContSingle.clicked.connect(self.cont_single_game)
        self.btnJoinMulti.clicked.connect(self.join_multi_game)
        self.btnStartNewMulti.clicked.connect(self.start_new_multi_game)
        self.btnContMulti.clicked.connect(self.cont_multi_game)
        
        self.id = 0
        self.email = ''
        self.nickname = ''

    def load_main_menu(self):
        self.mainMenu.setCurrentIndex(1)

    def load_new_single(self):
        self.mainMenu.setCurrentIndex(2)
    
    def start_new_single_game(self):
        runner = run.COSMICARunner(galaxy='COSMICA2', serverPort=None, mapfile="quickstart-4man.map", 
                                   remoteServer='http://localhost:8000', password='singleplayer')
        runner.start()
        self.exit_launcher()
    
    def load_cont_single(self):
        self.mainMenu.setCurrentIndex(3)
        
    def cont_single_game(self):
        runner = run.COSMICARunner(galaxy='COSMICA2', serverPort=None, mapfile="quickstart-4man.map", 
                                   remoteServer='http://localhost:8000', password='singleplayer')
        runner.start()
        self.exit_launcher()
    
    def load_join_multi(self):
        self.mainMenu.setCurrentIndex(4)

    def join_multi_game(self):
        runner = run.COSMICARunner(galaxy='COSMICA6', serverPort=None, empire=5, password='fvuu7ojm',
                                   remoteServer='http://192.168.1.69:8006', startSinglePlayerServer=False)
        runner.start()
        self.exit_launcher()

    def load_host_multi(self):
        self.mainMenu.setCurrentIndex(5)
        
    def start_new_multi_game(self):
        # insert player list into startup code, change arguments to include player list, instead of txt file.
        runner = run.COSMICARunner(galaxy='COSMICA3', serverPort=8003, mapfile="quickstart-4man.map", 
                                   singlePlayer=False, playerList='colshag@gmail.com,email2@email.ca')
        runner.start()
        self.exit_launcher()      

    def load_cont_multi(self):
        self.mainMenu.setCurrentIndex(6)
        
    def cont_multi_game(self):
        runner = run.COSMICARunner(galaxy='COSMICA3', serverPort=8003, singlePlayer=False)
        runner.start()
        self.exit_launcher()
        
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
    
    def exit_launcher(self):
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = Launcher()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main() 