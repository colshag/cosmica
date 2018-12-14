# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# dialogbox.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This gui will provide a box with some text and an ok button
# ---------------------------------------------------------------------------
from rootbutton import RootButton
from anw.func import globals

class DialogBox(RootButton):
    """The Dialog Box Gui"""
    def __init__(self, path, x=0, y=0, texts=['Insert Dialog Text Here'],textColors = ['orange']):
        RootButton.__init__(self, path, x=x, y=y, name='okiunderstand',ignoreShortcutButtons=[],createButtons=False)
        self.scale = 0.25
        height = 0
        i = 0
        for color in textColors:
            height += self.createInfoPane(text=texts[i], wordwrap=40,x=x-0.25,z=y-(height/19.0), scale=0.045, textColor=globals.colors[color])
            i += 1
        self.createButtons(height)

    def createButtons(self, height):
        """Create all Buttons"""
        buttonPosition = (self.posInitX-0.01,0,self.posInitY-(height/19.0))
        self.createButton('blank', buttonPosition, geomX=0.5, geomY=0.0525)
        
        if globals.isTutorial and globals.tutorialStep > 0:
            buttonPosition = (self.posInitX+0.5,0,self.posInitY-(height/19.0))
            self.createButton('blankback', buttonPosition, geomX=0.5, geomY=0.0525)            

    def pressblank(self):
        """Press Ok I understand button"""
        self.mode.removeDialogBox()
        if globals.isTutorial and globals.tutorialStepComplete:
            globals.tutorialStep += 1
            globals.tutorialGoBackDisabled = True
            self.mode.displayTutorialMessage()
        if globals.isTutorial == False:
            self.mode.displayHelpMessage()
            
    def pressblankback(self):
        """Press go back a step button"""
        self.mode.removeDialogBox()
        if globals.isTutorial:
            globals.tutorialStep -= 1
            globals.tutorialStepComplete = True
            globals.tutorialGoBackDisabled = False
            self.mode.displayTutorialMessage()
                    
if __name__ == "__main__":
    myGui = DialogBox('media')
    run()        

        
    