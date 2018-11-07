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
    def __init__(self, path, x=0, y=0, text='Insert Dialog Text Here',textColor=globals.colors['guiyellow']):
        RootButton.__init__(self, path, x=x, y=y, name='okiunderstand',ignoreShortcutButtons=[],createButtons=False)
        self.scale = 0.25
        wordwrap = 50
        rows = int(len(text) / (wordwrap)) + (len(text) % (wordwrap) > 0)
        self.createInfoPane(text, wordwrap=wordwrap,x=x-0.25,z=y+0.01+(0.022*rows), scale=0.025, textColor=textColor)
        self.createButtons()

    def createButtons(self):
        """Create all Buttons"""
        for key in ['blank']:
            buttonPosition = (self.posInitX-0.01,0,self.posInitY)
            self.createButton(key, buttonPosition, geomX=0.5, geomY=0.0525)

    def pressblank(self):
        """Press Ok I understand button"""
        self.mode.removeDialogBox()

                    
if __name__ == "__main__":
    myGui = DialogBox('media')
    run()        

        
    