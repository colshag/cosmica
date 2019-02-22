# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# launcher.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This is main cosmica launcher
# ---------------------------------------------------------------------------
from PyQt4 import QtGui, QtCore
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
        # load the resolutions
        resolutions = ['640x480', '800x600', '960x720', '1024x768', '1280x960', '1400x1050', '1440x1080', '1600x1200', '1856x1392', '1920x1440', '2048x1536', '1280x800', '1440x900', '1680x1050', '1920x1200', '1920x1080', '2560x1600']
        self.cboResolution.clear()
        self.cboResolution.addItems(resolutions)
        self.fullscreen = False
        self.resolution = ''
        self.tutorial = False
        try:
            f = open("resolution.txt", "r")
            resolution = f.read()
            if resolution == '':
                self.fullscreen = False
            else:
                self.chkFullScreenMode.toggle()
                self.fullscreen = True
                self.resolution = resolution
            self.cboResolution.setCurrentIndex(resolutions.index(resolution))
        except:
            pass
        
        self.cboResolution.currentIndexChanged.connect(self.cboResolution_clicked)
        self.chkFullScreenMode.stateChanged.connect(self.chkFullScreenMode_clicked)
        self.chkTutorialMode.stateChanged.connect(self.chkTutorialMode_clicked)
        
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
        self.lstChooseGameJoinMulti.clicked.connect(self.lstChooseGameJoinMulti_clicked)
        self.lstChooseServerContMulti.clicked.connect(self.lstChooseServerContMulti_clicked)
        self.selectedMapName = None
        self.selectedDBOnDisk = None
        
        self.id = 0
        self.email = ''
        self.nickname = ''
        self.myInfo = {}
        f = open('neurojump.info', 'r')
        self.serverAddress = f.read()
        self.gamesICanJoin = []
        self.selectedGameToJoin = 0
        self.serversIAmHosting = []
        self.selectedServerToCont = 0

    def cboResolution_clicked(self, index):
        if self.chkFullScreenMode.isChecked():
            self.chkFullScreenMode.toggle()           
            self.fullscreen = False

    def chkFullScreenMode_clicked(self, state):
        if state == QtCore.Qt.Checked:
            text_file = open("resolution.txt", "w")
            text_file.write(self.cboResolution.currentText())
            text_file.close()
            self.fullscreen = True
            self.resolution = self.cboResolution.currentText()
        else:
            text_file = open("resolution.txt", "w")
            text_file.write('')
            text_file.close() 
            self.fullscreen = False
    
    def chkTutorialMode_clicked(self, state):
        if state == QtCore.Qt.Checked:
            self.tutorial = True
        else:
            self.tutorial = False
           
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')    
        
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
            if line in ['COSMICA1','COSMICA2','COSMICA3','COSMICA4','COSMICA5',
                        'COSMICA6','COSMICA7','COSMICA8','COSMICA9','COSMICA10']:
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
        
    def lstChooseGameJoinMulti_clicked(self, index):
        # load selected game info
        self.selectedGameToJoin = index.row()
        gameInfo = self.gamesICanJoin[index.row()]
        # turn status
        if gameInfo[8] == 1:
            turnStatus = 'You have Ended your Turn'
        else:
            turnStatus = 'Please end your turn'
        
        # player color
        empireName = ['Neutral','Yellow Empire','Brown Empire','Green Empire','Blue Empire','Pink Empire','Red Empire','Cyan Empire','Fire Empire']
        
        self.lblGalaxyNameJoinMulti.setText(gameInfo[1])
        self.lblGalaxyNameJoinMulti.setStyleSheet('color: #FFFFFF; background-color: #4075CC;')
        self.lblMapNameJoinMulti.setText(gameInfo[2])
        self.lblMapNameJoinMulti.setStyleSheet('color: cyan; background-color: black;')
        self.lblAddressJoinMulti.setText(gameInfo[3])
        self.lblAddressJoinMulti.setStyleSheet('color: yellow; background-color: black;')
        self.lblRoundNumJoinMulti.setText('ROUND: %s' % gameInfo[4])
        self.lblRoundNumJoinMulti.setStyleSheet('color: yellow; background-color: black;')
        self.lblVersionJoinMulti.setText(gameInfo[5])
        self.lblVersionJoinMulti.setStyleSheet('color: orange; background-color: black;')
        self.lblEmpireNameJoinMulti.setText(empireName[int(gameInfo[6])])
        self.lblEmpireNameJoinMulti.setStyleSheet('color: white; background-color: black;')
        self.lblTurnStatusJoinMulti.setText(turnStatus)
        self.lblTurnStatusJoinMulti.setStyleSheet('color: white; background-color: black;')
    
    def lstChooseServerContMulti_clicked(self, index):
        # load selected game info
        self.selectedServerToCont = index.row()
        gameInfo = self.serversIAmHosting[index.row()]
        
        self.lblGalaxyNameContMulti.setText(gameInfo[1])
        self.lblGalaxyNameContMulti.setStyleSheet('color: #FFFFFF; background-color: #4075CC;')
        self.lblMapNameContMulti.setText(gameInfo[2])
        self.lblMapNameContMulti.setStyleSheet('color: cyan; background-color: black;')
        if 'http://' in gameInfo[3]:
            address = gameInfo[3][7:]
        self.txtAddressContMulti.setText(address)
        self.lblRoundNumContMulti.setText('ROUND: %s' % gameInfo[4])
        self.lblRoundNumContMulti.setStyleSheet('color: yellow; background-color: black;')
        self.lblVersionContMulti.setText(gameInfo[5])
        self.lblVersionContMulti.setStyleSheet('color: orange; background-color: black;')
    
    def start_new_single_game(self):
        if self.selectedMapName == None:
            self.message('Please select a map')
            return
        dataBaseName = self.getAvailableDatabaseNameOnDisk()
        if dataBaseName == None:
            self.message('Please delete some of your existing games from your Database folder')
            return
        runner = run.COSMICARunner(galaxy=dataBaseName, serverPort=None, mapfile=self.selectedMapName, 
                                   remoteServer='http://localhost:8000', password='singleplayer', 
                                   fullscreen=self.fullscreen, resolution=self.resolution, tutorial=self.tutorial)
        runner.start()
        self.exit_launcher()
    
    def message(self, text):
        w = QtGui.QWidget()
        QtGui.QMessageBox.warning(w, "Cosmica", text)
    
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
                                   remoteServer='http://localhost:8000', password='singleplayer', fullscreen=self.fullscreen, resolution=self.resolution)
        runner.start()
        self.exit_launcher()        
    
    def load_join_multi(self):
        self.mainMenu.setCurrentIndex(4)
        server = ServerProxy(self.serverAddress)
        result = server.request_active_multiplayer_games(self.myInfo)
        
        # result should return list of games that player is currently playing in
        if isinstance(result, list):
            # list all the games and store information for selection and launching purposes
            model = QtGui.QStandardItemModel()
            self.lstChooseGameJoinMulti.setModel(model)            
            self.gamesICanJoin = result
            for gameInfo in self.gamesICanJoin:
                item = QtGui.QStandardItem(gameInfo[1])
                model.appendRow(item)           
        else:
            self.message('Join Multiplayer Error: %s' % result)

    def join_multi_game(self):
        try:
            gameInfo = self.gamesICanJoin[self.selectedGameToJoin]
            # gameInfo valid, update user stats to server
            gameID = gameInfo[0]
            server = ServerProxy(self.serverAddress)
            result = server.join_multiplayer_game(self.myInfo, gameID)
            if result == 1:
                # check if a local connection overides the neurojump address for this user
                address = ''
                try:
                    f = open('connections.info', 'r')
                    li = f.read()
                    li = li.split(',')
                    for idx, elem in enumerate(li):
                        thiselem = elem
                        nextelem = li[(idx + 1) % len(li)]
                        if thiselem == gameInfo[1]:
                            address = nextelem
                except:
                    pass
                
                if address == '':
                    address = gameInfo[3]
                # run game
                runner = run.COSMICARunner(galaxy=gameInfo[1], serverPort=None, empire=gameInfo[6], password=gameInfo[7],
                                       remoteServer=address, startSinglePlayerServer=False, fullscreen=self.fullscreen, resolution=self.resolution)
                runner.start()
                self.exit_launcher()
            else:
                self.message('Join Multiplayer Error: %s' % result)
        except:
            pass

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
        newAddress = str(self.txtAddressNewMulti.text())
        newAddress = 'http://' + newAddress
        result = server.create_new_game(self.myInfo, nicknames, newAddress, self.selectedMapName)
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
                self.message('Registering Players Error: %s' % result2)
        else:
            self.message('Start New Game Error: %s' % result)   

    def load_cont_multi(self):
        self.mainMenu.setCurrentIndex(6)
        server = ServerProxy(self.serverAddress)
        result = server.request_my_active_servers(self.myInfo)
    
        # result should return list of servers that player is currently hosting for others
        if isinstance(result, list):
            # list all the servers and store information for selection and launching purposes
            model = QtGui.QStandardItemModel()
            self.lstChooseServerContMulti.setModel(model)            
            self.serversIAmHosting = result
            for gameInfo in self.serversIAmHosting:
                item = QtGui.QStandardItem(gameInfo[1])
                model.appendRow(item)           
        else:
            self.message('Continue Server Error: %s' % result)
    
    def cont_multi_game(self):             
        try:
            gameInfo = self.serversIAmHosting[self.selectedServerToCont]
            # gameInfo valid, update server stats and server address to neurojump servers
            gameID = gameInfo[0]
            server = ServerProxy(self.serverAddress)
            newAddress = str(self.txtAddressContMulti.text())
            newAddress = 'http://' + newAddress
            result = server.cont_multiplayer_server(self.myInfo, gameID, newAddress)
            if result == 1:
                # run server
                runner = run.COSMICARunner(galaxy=gameInfo[1], serverPort=int(newAddress[-4:]), singlePlayer=False)
                runner.start()
                self.exit_launcher()
            else:
                self.message('Continue Server Error: %s' % result)
        except:
            pass
        
    def register_user(self):
        self.myInfo = {'email':str(self.txtNewEmail.text()), 'nickname':str(self.txtNewNickname.text()), 'password':str(self.txtNewPassword.text())}
        server = ServerProxy(self.serverAddress)
        result = server.register_new_player(self.myInfo)
        if result == 1:
            self.mainMenu.setCurrentIndex(1)
            self.message("Welcome to Cosmica %s, your registered email is: %s" % (str(self.txtNewNickname.text()), str(self.txtNewEmail.text())))
        else:
            self.message("Error in Registration: %s" % result)      
            
    def login_user(self):
        self.myInfo = {'nickname':str(self.txtNickname.text()), 'password':str(self.txtPassword.text())}
        server = ServerProxy(self.serverAddress)
        result = server.login_player(self.myInfo)
        if len(result) == 4:
            self.id = result[0]
            self.email = result[1]
            self.nickname = result[2]
            self.mainMenu.setCurrentIndex(1)
            self.myInfo['email'] = self.email
            self.message('Welcome to Cosmica %s, your registered email is: %s' % (self.nickname, self.email))
        else:
            self.message('Login Error: %s' % result)
    
    def exit_launcher(self):
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    form = Launcher()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main() 