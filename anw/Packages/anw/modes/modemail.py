# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# modemail.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This is the galactic mail mode
# ---------------------------------------------------------------------------
import mode
from anw.gui import buttonlist
from anw.func import globals

class ModeMail(mode.Mode):
    """This represents the Mail System Mode"""
    def __init__(self, game):
        # init the mode
        mode.Mode.__init__(self, game)
        self.enableMouseCamControl = 0
        self.resetCamera()
        self.name = 'MAIL'
        self.createMainMenu('Y')
        self.mailRound = None
        self.mailInfo = None
        self.mailBody = None
        self.roundStatus = None
        self.getMailUpdate()
        self.createMailRoundFrame()
        self.createMailInfoFrame()
        self.createMailBodyFrame()
        self.createRoundStatusFrame()
        self.populateMailRound()
        self.populateRoundStatus()
        self.populateMailInfo(self.game.currentRound, 0, None)
        if globals.isTutorial:
            globals.tutorialGoBackDisabled = True
            self.mainmenu.pressU()        

    def setMyBackground(self):
        """Set the Background of mode"""
        try:
            from direct.gui.OnscreenImage import OnscreenImage
            # use render2d for front rendering and render2dp for background rendering.
            self.background = OnscreenImage(parent=render2dp, image=self.guiMediaPath+"backgroundspace.mov", scale=(1.1,1,1.9), pos=(0.05,0,0.9))            
            base.cam2dp.node().getDisplayRegion(0).setSort(-20)
            self.gui.append(self.background)
        except:
            base.setBackgroundColor(globals.colors['guiblue4'])

    def createMailRoundFrame(self):
        """Build the Mail Round Frame"""
        self.mailRound = buttonlist.ButtonList(self.guiMediaPath, 'Choose Round:', 0.3, 0.6)
        self.mailRound.setMyPosition(-0.8, 0.45)
        self.mailRound.setMyMode(self)
        self.mailRound.setOnClickMethod('populateMailInfo')
        self.gui.append(self.mailRound)
        
    def createMailInfoFrame(self):
        """Build the Mail Info Frame"""
        self.mailInfo = buttonlist.ButtonList(self.guiMediaPath, 'Select Message:', 1.5, 0.6)
        self.mailInfo.setMyPosition(0.2, 0.45)
        self.mailInfo.setMyMode(self)
        self.mailInfo.setOnClickMethod('populateMailBody')
        self.gui.append(self.mailInfo)
    
    def createMailBodyFrame(self):
        """Build a Mail Body Frame"""
        self.mailBody = buttonlist.ButtonList(self.guiMediaPath, 'Message Details:', 1.9, 0.6)
        self.mailBody.setMyPosition(0, -0.2)
        self.gui.append(self.mailBody)
        
    def createRoundStatusFrame(self):
        """Build a Round Status Frame"""
        self.roundStatus = buttonlist.ButtonList(self.guiMediaPath, 'Round Status:', 1.9, 0.4)
        self.roundStatus.setMyPosition(0, -0.75)
        self.gui.append(self.roundStatus)
    
    def populateRoundStatus(self):
        """Fill Round Status List"""
        notdone = 0
        for empireID, myEmpire in self.game.allEmpires.iteritems():
            if (empireID != '0' and empireID != self.game.myEmpireID and
                myEmpire['alive'] == 1):
                if myEmpire['roundComplete'] == 0:
                    notdone += 1

        if self.game.myEmpire['roundComplete'] == 0 and notdone == 0:
            text = 'You are the last person to finish your turn, once complete the round will end'
            self.roundStatus.myScrolledList.addItem(text=text, extraArgs=1, textColorName='guired')
        elif notdone > 0:
            text = "%d of the other Empires has yet to complete their turn this round" % notdone
            self.roundStatus.myScrolledList.addItem(text=text, extraArgs=1, textColorName='guiyellow')


    def populateMailRound(self):
        """Fill Mail Round List"""
        myRounds = range(1,self.game.currentRound+1)
        myRounds.reverse()
        for roundNum in myRounds:
            self.mailRound.myScrolledList.addItem(text='Round %d' % roundNum, 
                                                  extraArgs=roundNum)
        
    def populateMailInfo(self, roundNum, index, button):
        """Fill Mail Info List with all Mail Messages from round selected"""
        myMailBoxDict = self.game.myMailBox
        self.mailInfo.myScrolledList.clear()
        self.mailBody.myScrolledList.clear()
        for id, mailBoxDict in myMailBoxDict.iteritems():
            if mailBoxDict['round'] == roundNum:
                self.mailInfo.myScrolledList.addItem(text=mailBoxDict['subject'], 
                                                     extraArgs=id)
    
    def populateMailBody(self, mailID, index, button):
        """Fill Mail Body with info based on Mail Info Click"""
        self.mailBody.myScrolledList.clear()
        myMailDict = self.game.myMailBox[mailID]
        self.playSound('beep01')
        self.mailBody.addMultiLines(eval(myMailDict['body']))
    
    def enterMode(self):
        """Do not accept Mouse Events"""