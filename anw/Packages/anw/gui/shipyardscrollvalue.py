# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# shipyardscrollvalue.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This uses scroll mouse up/down or plus and minus buttons to create a number
# number is saved to mode, number can be negative
# ---------------------------------------------------------------------------
from anw.gui import scrollvalue

class ShipyardScrollValue(scrollvalue.ScrollValue):
    """The Scroll Value Gui"""
    def __init__(self, path, x, y, name, addShips, myParent):
        self.addShips = addShips
        self.myParent = myParent
        scrollvalue.ScrollValue.__init__(self, path, x, y, name, 'Z')

    def createTitleCard(self, name, text, wordwrap, x, z, scale=0.025):
        """Default Title label for gui controls"""
        if self.addShips == 1:
            text = 'Choose Amount of Selected Ship Design to Add:'
        else:
            text = 'Choose Amount of Ship order to Reduce:'
        scrollvalue.ScrollValue.createTitleCard(self, name, text, wordwrap, x, z, scale=0.025)
        
    def pressS(self):
        """Submit value to server"""
        if self.addShips == 1:
            self.mode.addShipOrder(self.currentValue, self.id, self.myParent.mySystemDict['id'])
        else:
            self.mode.modifyShipOrder(self.currentValue, self.id)
        self.disableButton('S')
        
    def validateValue(self, value):
        """Validate that value can be set"""
        if value > self.maxValue:
            self.giveInformativeMessageForMaxReached(value)
            return 0
        if value < self.minValue:
            return 0
        return 1
    
    def giveInformativeMessageForMaxReached(self, value):
        """Tell player why max value was reached"""
        reason = ""
        max = self.myParent.getMaxFromFundsAvail()
        max2 = self.myParent.getMaxFromAvailSYC()
        if max2 < max:
            reason = "you do not have enough Shipyard Capacity"
        else:
            reason = "you do not have enough resources"
        self.myParent.game.mode.createMessage(reason)
    
if __name__ == "__main__":
    myScrollValue = ShipyardScrollValue('media', -0.3, -0.17, 'scroll', addShips=0, myParent=None)
    myScrollValue.setMaxValue(219)
    myScrollValue.setMinValue(-119)
    run()