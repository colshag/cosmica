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
import glob
import re
import random
import string

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
        
        # main listbox clicked
        self.lstChooseMapNewSingle.clicked.connect(self.lstChooseMapNewSingle_clicked)
        self.lstChooseGameContSingle.clicked.connect(self.lstChooseGameContSingle_clicked)
        self.lstChooseMapNewMulti.clicked.connect(self.lstChooseMapNewMulti_clicked)
        self.selectedMapName = None
        self.selectedDBOnDisk = None
        
        self.id = 0
        self.email = ''
        self.nickname = ''
        self.myInfo = {}
        self.serverAddress = 'http://localhost:8090/'

    def load_main_menu(self):
        self.mainMenu.setCurrentIndex(1)

    def load_new_single(self):
        self.mainMenu.setCurrentIndex(2)
        self.selectedMapName = None
        entries = self.getAvailableMapNames()
        if entries == []:
            return
        
        model = QtGui.QStandardItemModel()
        self.lstChooseMapNewSingle.setModel(model)
        
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)        
    
    def getAvailableMapNames(self):
        myList = glob.glob('../Data/*.map')
        myNewList = []
        for line in myList:
            line = line[8:]
            myNewList.append(line)   
        return myNewList
    
    def getCurrentGamesOnDisk(self):
        myList = glob.glob('../Database/COSMICA*')
        myNewList = []
        for line in myList:
            line = line[12:]
            myNewList.append(line)
        return myNewList
    
    def getAvailableDatabaseNameOnDisk(self):
        currentNames = self.getCurrentGamesOnDisk()
        for i in range(1,9):
            if 'COSMICA%d' % i not in currentNames:
                return 'COSMICA%d' % i
        return None
    
    def lstChooseMapNewSingle_clicked(self, index):
        self.selectedMapName = str(index.data().toString())
    
    def lstChooseMapNewMulti_clicked(self, index):
        self.selectedMapName = str(index.data().toString())
    
    def lstChooseGameContSingle_clicked(self, index):
        self.selectedDBOnDisk = str(index.data().toString())
    
    def start_new_single_game(self):
        if self.selectedMapName == None:
            self.message('Please select a map')
            return
        dataBaseName = self.getAvailableDatabaseNameOnDisk()
        if dataBaseName == None:
            self.message('Please delete some of your existing games from your Database folder')
            return
        runner = run.COSMICARunner(galaxy=dataBaseName, serverPort=None, mapfile=self.selectedMapName, 
                                   remoteServer='http://localhost:8000', password='singleplayer')
        runner.start()
        self.exit_launcher()
    
    def message(self, text):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(text)
        msg.exec_()
    
    def load_cont_single(self):
        self.mainMenu.setCurrentIndex(3)
        self.selectedDBOnDisk = None
        entries = self.getCurrentGamesOnDisk()
        if entries == []:
            return
        
        model = QtGui.QStandardItemModel()
        self.lstChooseGameContSingle.setModel(model)
        
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)        
        
    def cont_single_game(self):
        if self.selectedDBOnDisk == None:
            self.message('Please select an existing game')
            return
        runner = run.COSMICARunner(galaxy=self.selectedDBOnDisk, serverPort=None, mapfile="quickstart-4man.map", 
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
        self.selectedMapName = None
        entries = self.getAvailableMapNames()
        if entries == []:
            return
        
        model = QtGui.QStandardItemModel()
        self.lstChooseMapNewMulti.setModel(model)
        
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        
    def start_new_multi_game(self):
        if self.selectedMapName == None:
            self.message('Please select a map')
            return
        if str(self.txtAddressNewMulti.text()) == '':
            self.message('Please provide a server address and port for your players to connect to, (http://address:port)')
            return
        
        # check that players are valid from neurojump servers
        nicknames = [str(self.txtPlayer1.text()),str(self.txtPlayer2.text()),str(self.txtPlayer3.text()),str(self.txtPlayer4.text()),
                     str(self.txtPlayer5.text()),str(self.txtPlayer6.text()),str(self.txtPlayer7.text()),str(self.txtPlayer8.text())]
        nicknames = filter(None, nicknames)
        nicknames = list(set(nicknames))
        if len(nicknames) > int(self.selectedMapName[:1]):
            self.message('You have chosen %d players for a map of max size of %d players, choose a larger map or remove some players' % (len(nicknames), int(self.selectedMapName[:1])))
            return
        server = ServerProxy(self.serverAddress)
        result = server.create_new_game(self.myInfo, nicknames, str(self.txtAddressNewMulti.text()), self.selectedMapName)
        # result should return ('GALAXYNAME', [email1@email.com,email2@email.com,...])
        # determine which players will be in what empireID and what password, send to server so players can log in properly.
        
        if isinstance(result, list):
            # shuffle colors of starting empires
            playerGenData = {}
            playerList = result[1]
            random.shuffle(playerList)
            s = range(1,8) #maxEmpires is 8
            random.shuffle(s)
            for email in playerList:
                # assign player to random empireID from 1-8
                empireID = str(s.pop(0))
                # assign sever passwords for each player
                chars = string.ascii_lowercase + string.digits
                pw = ''.join( random.choice(chars) for _ in range(8) )
                playerGenData[empireID] = {'email': email, 'password': pw}
            
            # with player empireID and passwords assigned insert player data into neurojump servers so players can log in later
            server = ServerProxy(self.serverAddress)
            result2 = server.register_players_into_game(self.myInfo, self.id, result[0], playerGenData)
            
            if result2 == 1: # successfully registered players into neurojump servers
                runner = run.COSMICARunner(galaxy=result[0], serverPort=int(str(self.txtAddressNewMulti.text())[-4:]), mapfile=self.selectedMapName, 
                                           remoteServer=str(self.txtAddressNewMulti.text()), singlePlayer=False, playerList=result[1], playerGenData=playerGenData)
                runner.start()
                self.exit_launcher()
            else:
                self.message('Registering Players Error:%s' % result2)
        else:
            self.message('Start New Game Error:%s' % result)   

    def load_cont_multi(self):
        self.mainMenu.setCurrentIndex(6)
    
    def cont_multi_game(self):
        runner = run.COSMICARunner(galaxy='COSMICA3', serverPort=8003, singlePlayer=False)
        runner.start()
        self.exit_launcher()
        
    def register_user(self):
        self.myInfo = {'email':str(self.txtNewEmail.text()), 'nickname':str(self.txtNickname.text()), 'password':str(self.txtNewPassword.text())}
        server = ServerProxy(self.serverAddress)
        result = server.register_new_player(self.myInfo)
        if result == 1:
            self.mainMenu.setCurrentIndex(1)
            self.message("Welcome to Cosmica %s" % str(self.txtNickname.text()))
        else:
            self.message("Error in Registration: %s" % result)      
            
    def login_user(self):
        self.myInfo = {'email':str(self.txtEmail.text()), 'password':str(self.txtPassword.text())}
        server = ServerProxy(self.serverAddress)
        result = server.login_player(self.myInfo)
        if len(result) == 4:
            self.id = result[0]
            self.email = result[1]
            self.nickname = result[2]
            self.mainMenu.setCurrentIndex(1)
            self.myInfo['nickname'] = self.nickname
            self.message('Welcome to Cosmica %s' % self.nickname)
        else:
            self.message('Login Error:%s' % result)
    
    def exit_launcher(self):
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = Launcher()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main() 