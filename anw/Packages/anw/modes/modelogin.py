# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# modelogin.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This is representation of the Login Mode in COSMICA
# ---------------------------------------------------------------------------
import mode
from anw.modes import modemail
from direct.task import Task
from anw.func import globals
    
class ModeLogin(mode.Mode):
    """This is the Login Mode, this should only come up on login error"""
    def __init__(self, game, wait):
        # init the mode
        mode.Mode.__init__(self, game)
        self.name = 'LOGIN'
        self.myLogo = self.loadObject(tex='cosmica', depth=300, glow=1)
        self.sims.append(self.myLogo)
        self.count = wait
        taskMgr.add(self.login, 'loginTask')
        
    def login(self, task):
        """Check if we can login"""
        if self.count <= 0:
            self.game.loginToGame()
            return Task.done
        else:
            self.count -= 1
            return Task.cont

    #def setMyBackground(self):
        #"""Set the Background of mode"""
        #try:
            #from direct.gui.OnscreenImage import OnscreenImage
            ## use render2d for front rendering and render2dp for background rendering.
            #self.background = OnscreenImage(parent=render2dp, image=self.guiMediaPath+"backgroundspace.mov", scale=(1.1,1,1.9), pos=(0.05,0,0.9))            
            #base.cam2dp.node().getDisplayRegion(0).setSort(-20)
            #self.gui.append(self.background)
        #except:
            #base.setBackgroundColor(globals.colors['guiblue3'])

    def enterMode(self):
        """Do not accept Mouse Events"""
        