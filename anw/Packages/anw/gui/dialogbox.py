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
    def __init__(self, path, x=0, y=0, text='Insert Dialog Text Here',textColor=globals.colors['orange'], displayNextMessage=False):
        RootButton.__init__(self, path, x=x, y=y, name='okiunderstand',ignoreShortcutButtons=[],createButtons=False)
        self.scale = 0.25
        self.displayNextMessage = displayNextMessage
        height = self.createInfoPane(text, wordwrap=50,x=x-0.25,z=y, scale=0.035, textColor=textColor)
        self.createButtons(height)

    def createButtons(self, height):
        """Create all Buttons"""
        for key in ['blank']:
            buttonPosition = (self.posInitX-0.01,0,self.posInitY-(height/25.0))
            self.createButton(key, buttonPosition, geomX=0.5, geomY=0.0525)

    def pressblank(self):
        """Press Ok I understand button"""
        self.mode.removeDialogBox()
        if globals.isTutorial and globals.tutorialStepComplete:
            globals.tutorialStep += 1
            self.mode.displayTutorialMessage()
        if globals.isTutorial == False:
            self.mode.displayHelpMessage()
                    
if __name__ == "__main__":
    myGui = DialogBox('media')
    run()        

        
    