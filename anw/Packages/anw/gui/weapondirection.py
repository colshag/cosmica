# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# weapondirection.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# Allows user to declare weapon direction on ship
# ---------------------------------------------------------------------------
from anw.gui import rootbutton

class WeaponDirection(rootbutton.RootButton):
    """Allows user to declare weapon direction on ship"""
    def __init__(self, path, x, y):
        rootbutton.RootButton.__init__(self, path, x=x, y=y, name='design')
        self.allKeys = ['1','2','3','4']
        self.disableButtonTime = -1
        self.disableButtonIgnore = []
        self.direction = 0
        self.press1()
    
    def createButtons(self):
        """Create all Buttons"""
        #fore weapon direction
        buttonPosition = (0.3,0,0.75)
        self.createButton('1', buttonPosition)        
        
        #aft weapon direction
        buttonPosition = (0.26,0,-0.35)
        self.createButton('2', buttonPosition)        
        
        #port weapon direction
        buttonPosition = (-0.05,0,0.2)
        self.createButton('3', buttonPosition)        
        
        #star weapon direction
        buttonPosition = (0.65,0,0.2)
        self.createButton('4', buttonPosition)      
    
    def press1(self):
        """Press Fore Quad"""
        self.enableLastButton('1')
        self.disableButton('1')
        self.direction = 0
    
    def press2(self):
        """Press Aft Quad"""
        self.enableLastButton('2')
        self.disableButton('2')
        self.direction = 180
    
    def press3(self):
        """Press Port Quad"""
        self.enableLastButton('3')
        self.disableButton('3')
        self.direction = 270
    
    def press4(self):
        """Press Star Quad"""
        self.enableLastButton('4')
        self.disableButton('4')
        self.direction = 90

if __name__ == "__main__":
    myGui = WeaponDirection('media', 0, 0)
    run()