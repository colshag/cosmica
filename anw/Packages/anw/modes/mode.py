# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# mode.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This is the base mode class in COSMICA
# ---------------------------------------------------------------------------
import random
import types
import logging

from anw.func import globals, funcs, storedata
if globals.serverMode == 0:
    from panda3d.core import Point2, Point3, Vec3, Vec4, BitMask32
    from panda3d.core import PandaNode,NodePath, TextNode
    from direct.task import Task
    from panda3d.core import CollisionTraverser,CollisionNode
    from panda3d.core import CollisionHandlerQueue,CollisionRay
    from panda3d.core import Shader, ColorBlendAttrib
    import direct.directbase.DirectStart #camera
    from anw.gui import textonscreen, fadingtext, mainmenubuttons, line, dialogbox
    from direct.directtools.DirectGeometry import LineNodePath

class Mode(object):
    """This is the base Mode class"""
    def __init__(self, game):
        self.name = "MODE"
        self.guiMediaPath = '../Packages/anw/gui/media/'
        self.alive = 1
        self.enableMouseCamControl = 1
        self.enableScrollWheelZoom = 1
        self.canSelectFlags = {}
        self.messagePositions = []
        self.selectTypes = []
        self.gui = []
        self.help = []
        self.sims = []
        self.game = game
        self.depth = 20.0
        self.zoomCameraDepth = 10.0
        self.zoomCameraOutDepth = -10.0
        self.zoomSpeed = 5
        self.panSpeed = 1.0
        self.runningTasks = []
        if globals.serverMode == 0:
            self.setMyBackground()
            camera.setHpr(0,0,0)
        self.mainmenu = None
        self.scrollSpeed = 0.1

        if globals.serverMode == 0:
            self.setMousePicker()
            self.setCameraPosition()
        
        self.selector = None
        self.selector2 = None
        self.dialogBox = None
        self.log = logging.getLogger('mode')
        
        self.entryFocusList = ('anw.gui.mainmenubuttons','anw.gui.industryvalue',
                                'anw.gui.cityindustry','anw.gui.weapondirection',
                                'anw.gui.scrollvalue','anw.gui.shipdesignvalue',
                                'anw.gui.systemmenu','anw.gui.tradevalue',
                                'anw.gui.designmenu','anw.gui.shipyardmenu', 'anw.gui.mimenu',
                                'anw.gui.textentry', 'anw.gui.marketsystemsellvalue', 
                                'anw.gui.sendcreditsvalue')
    
    def __getstate__(self):
        odict = self.__dict__.copy() # copy the dict since we change it
        del odict['log']             # remove stuff not to be pickled
        return odict

    def __setstate__(self,dict):
        log=logging.getLogger('mode')
        self.__dict__.update(dict)
        self.log=log
    
    def setMousePicker(self):
        self.picker = CollisionTraverser()
        self.pq = CollisionHandlerQueue()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.pq)
        self.selectable = render.attachNewNode("selectable")

    def setCameraPosition(self):
        self.cameraPos = (camera.getX(), camera.getY(), camera.getZ())
        self.cameraMoving = 0
    
    def setCanSelectFlag(self, key):
        """Set the Flag"""
        self.clearAllCanSelectFlags()
        self.canSelectFlags[key] = 1
        
    def clearAllCanSelectFlags(self):
        """Clear any selection flags"""
        for key in self.canSelectFlags.keys():
            self.canSelectFlags[key] = 0
     
    def isAnyFlagSelected(self):
        """Return 1 if any flags are selected"""
        for key in self.canSelectFlags.keys():
            if self.canSelectFlags[key] == 1:
                return 1
        return 0
            
    def validateSelection(self):
        """Can something be selected right now"""
        if self.cameraMoving == 0:
            return 1
        else:
            return 0
        
    def removeMyGui(self, myGuiName):
        """Remove gui"""
        try:
            myGui = getattr(self, myGuiName)
            if myGui in self.gui:
                self.gui.remove(myGui)
            if myGui != None:
                myGui.destroy()
                setattr(self, myGuiName, None)
        except:
            pass
    
    def createMainMenu(self, key):
        self.mainmenu = mainmenubuttons.MainMenuButtons(self.guiMediaPath)
        self.mainmenu.setMyGame(self.game)
        self.mainmenu.setMyMode(self)
        self.mainmenu.enableLastButton(key)
        self.mainmenu.checkDisableButton(key)
        self.mainmenu.writeGameInfo()
        self.mainmenu.acceptSpaceBarKey()
        self.gui.append(self.mainmenu)
    
    def removeMainMenu(self):
        if self.mainmenu != None:
            self.mainmenu.destroyMe()
            self.mainmenu = None
    
    def centerCameraOnSim(self, sim):
        """Center the camera on the sim position"""
        self.game.app.disableMouseCamControl()
        camera.setPos(sim.getX(), camera.getY(), sim.getZ())
        camera.setHpr(0,0,0)
        if self.enableMouseCamControl == 1:
            self.game.app.enableMouseCamControl()
    
    def drawBox(self, x, y, width, height, color='guiblue1', lineWidth=0.15, glow=1):
        """Draw a box"""
        #LEFT
        myLine = line.Line(self.guiMediaPath,(x,y),(x,y+height), 'square_grey', lineWidth, glow)
        myLine.sim.setColor(globals.colors[color])
        self.gui.append(myLine)
        #TOP
        myLine = line.Line(self.guiMediaPath,(x,y+height),(x+width,y+height), 'square_grey', lineWidth, glow)
        myLine.sim.setColor(globals.colors[color])
        self.gui.append(myLine)
        #RIGHT
        myLine = line.Line(self.guiMediaPath,(x+width,y+height),(x+width,y), 'square_grey', lineWidth, glow)
        myLine.sim.setColor(globals.colors[color])
        self.gui.append(myLine)
        #BOTTOM
        myLine = line.Line(self.guiMediaPath,(x+width,y),(x,y), 'square_grey', lineWidth, glow)
        myLine.sim.setColor(globals.colors[color])
        self.gui.append(myLine)
    
    def stopCameraTasks(self):
        taskMgr.remove('zoomInCameraTask')
        taskMgr.remove('zoomOutCameraTask')
        self.cameraMoving = 0
        self.game.app.enableMouseCamControl()
        self.enableMouseCamControl=1
        
    def resetCamera(self):
        self.game.app.disableMouseCamControl()
        camera.setPos(self.cameraPos[0], self.zoomCameraOutDepth, self.cameraPos[2])
        # I don't really understand why this doesn't reset the view when having a planet selected and hitting spacebar?    
        camera.setHpr(0,0,0)

        if self.enableMouseCamControl == 1:
            self.game.app.enableMouseCamControl()
    
    def zoomInCamera(self):
        
        if camera.getY() <= self.zoomCameraDepth:
            self.game.app.disableMouseCamControl()
            taskMgr.add(self.zoomInCameraTask, 'zoomInCameraTask', extraArgs=[self.zoomCameraDepth])
            self.runningTasks.append('zoomInCameraTask')
    
    def zoomInCameraAmount(self, amount):
        """Zoom in Camera a certain amount specified"""
        depth = camera.getY()+amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.zoomInCameraTask, 'zoomInCameraTask', extraArgs=[depth])
        self.runningTasks.append('zoomInCameraTask')
    
    def zoomInCameraTask(self, depth):
        """Zoom in the camera until its at depth"""
        y = camera.getY()
        if y + 0.1 >= depth: # or y >= 8.0:  # TODO: tacking this on will mess with the design screen but prevents you from zooming in too close everywhere else.  
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            camera.setY(y)    
            return Task.done
        else:
            camera.setY(y+self.getZoomSpeed(y, depth))
            self.cameraMoving = 1
            return Task.cont
        
    def getZoomSpeed(self, y, depth):
        """Make Camera zoom in faster if camera is further away"""
        diff = depth-y
        return diff/5.0
    
    def zoomOutCamera(self):
        if camera.getY() >= self.zoomCameraOutDepth:
            self.game.app.disableMouseCamControl()
            taskMgr.add(self.zoomOutCameraTask, 'zoomOutCameraTask', extraArgs=[self.zoomCameraOutDepth])
            self.runningTasks.append('zoomOutCameraTask')
            
    def zoomOutCameraAmount(self, amount):
        """Zoom out Camera a certain amount sepecified"""
        depth = camera.getY()-amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.zoomOutCameraTask, 'zoomOutCameraTask', extraArgs=[depth])
        self.runningTasks.append('zoomOutCameraTask')
    
    def zoomOutCameraTask(self, depth):
        """Zoom out the camera until its at 0 Depth"""
        y = camera.getY()
        if y - 0.1 <= depth:
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            camera.setY(y)
            return Task.done
        else:
            camera.setY(y+self.getZoomSpeed(y, depth))
            self.cameraMoving = 1
            return Task.cont
    
    def panCameraLeft(self, amount):
        """Pan Camera"""
        pos = camera.getX()-amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.panCameraLeftTask, 'panCameraLeftTask', extraArgs=[pos])
        self.runningTasks.append('panCameraLeftTask')
    
    def panCameraLeftTask(self, pos):
        """pan the camera to new position"""
        x = camera.getX()
        if x <= pos:
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            return Task.done
        else:
            camera.setX(x-self.panSpeed)
            self.cameraMoving = 1
            return Task.cont

    def panCameraRight(self, amount):
        """Pan Camera"""
        pos = camera.getX()+amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.panCameraRightTask, 'panCameraRightTask', extraArgs=[pos])
        self.runningTasks.append('panCameraRightTask')
    
    def panCameraRightTask(self, pos):
        """pan the camera to new position"""
        x = camera.getX()
        if x >= pos:
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            return Task.done
        else:
            camera.setX(x+self.panSpeed)
            self.cameraMoving = 1
            return Task.cont
        
    def panCameraUp(self, amount):
        """Pan Camera"""
        pos = camera.getZ()+amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.panCameraUpTask, 'panCameraUpTask', extraArgs=[pos])
        self.runningTasks.append('panCameraUpTask')
    
    def panCameraUpTask(self, pos):
        """pan the camera to new position"""
        z = camera.getZ()
        if z >= pos:
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            return Task.done
        else:
            camera.setZ(z+self.panSpeed)
            self.cameraMoving = 1
            return Task.cont

    def panCameraDown(self, amount):
        """Pan Camera"""
        pos = camera.getZ()-amount
        self.game.app.disableMouseCamControl()
        taskMgr.add(self.panCameraDownTask, 'panCameraDownTask', extraArgs=[pos])
        self.runningTasks.append('panCameraDownTask')
    
    def panCameraDownTask(self, pos):
        """pan the camera to new position"""
        z = camera.getZ()
        if z <= pos:
            self.cameraMoving = 0
            if self.enableMouseCamControl == 1:
                self.game.app.enableMouseCamControl()
            return Task.done
        else:
            camera.setZ(z-self.panSpeed)
            self.cameraMoving = 1
            return Task.cont
        
    def createSelector(self,type='select',speed=2.0):
        """Create selector for indication of selected objects"""
        self.selector = self.loadObject(type, scale=2, parent=render, transparency=True, pos=Point2(0,0), glow=1)
        self.selector.hide()
        ival = self.selector.hprInterval((speed), Vec3(0, 0, 360))
        ival.loop()
    
    def createSelector2(self,type='select',speed=2.0):
        """Create selector2 for indication of secondary selected objects"""
        self.selector2 = self.loadObject(type, scale=2, parent=render, transparency=True, pos=Point2(0,0), glow=1)
        self.selector2.hide()
        ival = self.selector2.hprInterval((speed), Vec3(0, 0, 360))
        ival.loop()
    
    def playSound(self, soundName):
        """Play a Sound based on soundName given, call app"""
        if globals.serverMode == 0:
            self.game.app.playSound(soundName)
    
    def askForHelp(self):
        """Ask the Server to analyse Player and provide help"""
        try:
            serverResult = self.game.server.askForHelp(self.game.authKey)
            if type(serverResult) == types.ListType:
                self.help = serverResult
                self.displayHelpMessage()
            else:
                self.modeMsgBox(serverResult)
        except:
            self.modeMsgBox('askForHelp->Connection to Server Lost')
    
    def displayHelpMessage(self):
        """Look for any remaining help messages and display one of them"""
        if self.dialogBox == None:
            if len(self.help) > 0:
                message = self.help.pop()
                if 'SCANNING RESEARCH' in message:
                    color = globals.colors['cyan']
                elif 'SCANNING INDUSTRY' in message:
                    color = globals.colors['orange']
                elif 'SCANNING MILITARY' in message:
                    color = globals.colors['red']
                self.createDialogBox(x=-0.1,y=0.7,text=message,textColor=color)
       
    def assignSelector(self, myObj, scale):
        """create the Selector and assign to myObj at scale"""
        if self.selector == None:
            self.createSelector()
            self.selector.show()
            
        self.selector.setPos(myObj.getX(), myObj.getY(), myObj.getZ())
        self.selector.setScale(scale)
    
    def assignSelector2(self, myObj, scale):
        """create the Selector2 and assign to myObj at scale"""
        if self.selector2 == None:
            self.createSelector2()
            self.selector2.show()
            
        self.selector2.setPos(myObj.getX(), myObj.getY(), myObj.getZ())
        self.selector2.setScale(scale)
    
    def exitGame(self, doLogout=True):
        """Exit the game"""
        self.setEmpireDefaults(self.game.authKey)
        if doLogout:
            self.setLogout(self.game.authKey)
        self.alive = 0
        if globals.isTutorial:
            tutorialInfo = {'tutorialStep':globals.tutorialStep, 'tutorialStepComplete':globals.tutorialStepComplete}
            storedata.saveToFile(tutorialInfo, '%s/tutorial.data' % self.game.app.path)        
        self.game.app.quit()
    
    def getCreditInfoFromServer(self):
        self.getEmpireUpdate(['CR'])
    
    def refreshCredit(self):
        """Ask the Server for an updated Credit Info"""
        self.mainmenu.updateCR()
    
    def getEmpireUpdate(self, listAttr):
        """Ask the Server for updated Empire info"""
        try:
            serverResult = self.game.server.getEmpireUpdate(self.game.authKey, listAttr)
            if type(serverResult) == types.StringType:
                self.modeMsgBox(serverResult)
            else:
                for key, value in serverResult.iteritems():
                    self.game.myEmpire[key] = value
        except:
            self.modeMsgBox('getEmpireUpdate->Connection to Server Lost')
    
    def getMailUpdate(self):
        """Ask the Server for any updated mail"""
        try:
            myMailDict = self.game.myEmpire['mailBox']
            serverResult = self.game.server.getMailUpdate(self.game.authKey, myMailDict.keys())
            if type(serverResult) == types.StringType:
                self.modeMsgBox(serverResult)
            else:
                for key, value in serverResult.iteritems():
                    myMailDict[key] = value
        except:
            self.modeMsgBox('getMailUpdate->Connection to Server Lost')
    
    def getGalaxyUpdate(self, listAttr):
        """Ask the Server for updated Galaxy info"""
        try:
            serverResult = self.game.server.getGalaxyUpdate(listAttr, self.game.authKey)
            if type(serverResult) == types.StringType:
                self.modeMsgBox(serverResult)
            else:
                for key, value in serverResult.iteritems():
                    self.game.myGalaxy[key] = value
        except:
            self.modeMsgBox('getGalaxyUpdate->Connection to Server Lost')
    
    def getSystemUpdate(self, listAttr, systemID):
        """Ask the Server for updated System info"""
        try:
            serverResult = self.game.server.getSystemUpdate(listAttr, systemID, self.game.authKey)
            if type(serverResult) == types.StringType:
                self.modeMsgBox(serverResult)
            else:
                mySystemDict = self.game.allSystems[systemID]
                for key, value in serverResult.iteritems():
                    mySystemDict[key] = value
        except:
            self.modeMsgBox('getSystemUpdate->Connection to Server Lost')
        
    def enterMode(self):
        """Enter the mode."""
        self.alive = 1
        self.setShortcuts()
        if globals.isTutorial and globals.initialLogin:
            self.mainmenu.pressU()
            globals.initialLogin = False
    
    def setShortcuts(self):
        """Set the default mode shortcuts"""
        self.game.app.accept('mouse1', self.onMouse1Down)
        self.game.app.accept('mouse3', self.onMouse2Down)
        self.game.app.accept('space', self.onSpaceBarClear)
        if self.enableMouseCamControl == 1:
            self.game.app.accept('wheel_up', self.onMouseWheelUp)
            self.game.app.accept('wheel_down', self.onMouseWheelDown)
        
    def exitMode(self):
        """Exit the mode"""
        self.removeMySims()
        self.removeAllGui()
        self.game.app.ignoreAll()
        self.removeAllTasks()
        self.alive = 0
    
    def removeAllTasks(self):
        """Remove and Stop any tasks running"""
        for taskName in self.runningTasks:
            taskMgr.remove(taskName)

    def removeMySims(self):
        """Remove all sims in mode"""
        for sim in self.sims:
            try:
                sim.destroy()
            except:
                sim.removeNode()
    
    def removeAllGui(self):
        """Remove all DirectGUI"""
        for gui in self.gui:
            gui.destroy()
    
    def setPlanePickable(self, obj, dictName):
        """Set the plane model itself to be collideable with the mouse ray"""
        obj.sim.reparentTo(self.selectable)
        obj.sim.find('**/pPlane1').node().setIntoCollideMask(BitMask32.bit(1))
        obj.sim.find('**/pPlane1').node().setTag(dictName, obj.id)
    
    def setSpherePickable(self, obj, dictName):
        """Set the sphere model itself to be collideable with the mouse ray"""
        obj.sim.reparentTo(self.selectable)
        obj.sim.find('**/pSphere1').node().setIntoCollideMask(BitMask32.bit(1))
        obj.sim.find('**/pSphere1').node().setTag(dictName, obj.id)
    
    def setMySelector(self, x, y, z, scale):
        """Show selector if it is not in current position else return false"""
        selectorPos = (self.selector.getX(), self.selector.getY(), self.selector.getZ())
        if selectorPos != (x,y,z):
            self.selector.setPos(x,y,z)
            self.selector.show()
            self.selector.setScale(scale)
            return 1
        else:
            self.selector.setPos(-1,-1,-1)
            return 0
        #self.enableScrollWheelZoom = 0
    
    def getListButton(self, id, myScrolledList):
        """Return Button selected from buttonList gui based on id"""
        for button in myScrolledList.buttonsList:
            if button['extraArgs'][1] == id:
                return button
        
    def setMySelector2(self, x, y, z, scale):
        """Show selector2 if it is not in current position else return false"""
        selectorPos = (self.selector2.getX(), self.selector2.getY(), self.selector2.getZ())
        if selectorPos != (x,y,z):
            self.selector2.setPos(x,y,z)
            self.selector2.show()
            self.selector2.setScale(scale)
            return 1
        else:
            self.selector2.setPos(-1,-1,-1)
            return 0
        #self.enableScrollWheelZoom = 0
    
    def hideMySelector(self):
        """Hide the selector, move its position"""
        self.selector.setPos(-1,-1,-1)
        self.selector.hide()
        if self.selector2 != None:
            self.selector2.hide()
    
    def onMouse1Down(self):
        """Allow dynamic picking of an object within mode"""
        #Check to see if we can access the mouse. We need it to do anything else
        if base.mouseWatcherNode.hasMouse():
            #get the mouse position
            mpos = base.mouseWatcherNode.getMouse()
         
            #Set the position of the ray based on the mouse position
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            
            #Do the actual collision pass (Do it only on the selectable for
            #efficiency purposes)
            self.picker.traverse(self.selectable)
            if self.pq.getNumEntries() > 0:
                #if we have hit something, sort the hits so that the closest
                #is first, and highlight that node
                self.pq.sortEntries()
                for selectable in self.selectTypes:
                    name = self.pq.getEntry(0).getIntoNode().getTag(selectable)
                    if name != '':
                        self.clearAnyGui()
                        mySelectedDict = getattr(self, selectable)
                        mySelected = mySelectedDict[name]
                        myMethod = getattr(self, '%sSelected' % selectable)
                        if self.validateSelection():
                            myMethod(mySelected)
                        break
                    
    def onMouseWheelUp(self):
        """ zoom out """
        if self.enableScrollWheelZoom:
            self.stopCameraTasks()
            self.zoomInCameraAmount(20.0)
        
    def onMouseWheelDown(self):
        """ zoom in """
        if self.enableScrollWheelZoom:
            self.stopCameraTasks()
            self.zoomOutCameraAmount(20.0)
        
    def onMouse2Down(self):
        """clear"""
        self.onSpaceBarClear()
    
    def onSpaceBarClear(self):
        """Space bar should reset the view in the mode"""
        if self.validateSelection():
            self.resetCamera()
            self.clearMouseSelection()
            self.zoomOutCamera()
            self.setShortcuts()
            self.enableScrollWheelZoom = 1
    
    def clearMouseSelection(self):
        """Clear mouse selection before selecting something new"""
        pass

    def clearAnyGui(self):
        pass
    
    def update(self, interval):
        """update the mode, return the status, 0 means stop game"""
        return self.alive
        
    def setMyBackground(self):
        """Set the Background of mode"""
        base.setBackgroundColor(globals.colors['guiblue3'])
        
    def setEmpireDefaults(self, clientKey):
        """Read the defaults currently set and change them in the database"""
        try:
            # setup attributes to send to server
            defaults = ['viewIndustry', 'viewMilitary', 'viewResources', 'viewTradeRoutes']
            d = {}
            for item in defaults:
                d[item] = self.game.myEmpire[item]
            serverResult = self.game.server.setEmpire(clientKey, d)
            if serverResult == 1:
                print 'Setup Empire Defaults Success'
            else:
                self.modeMsgBox(serverResult)
        except:
            self.modeMsgBox('SetEmpireDefaults->Connection to Server Lost, Login Again')

    def setEmpireValues(self, dValues):
        """Update Empire with d = key: empire attribute name,
        value = new value"""
        try:
            serverResult = self.game.server.setEmpire(self.game.authKey, dValues)
            if serverResult == 1:
                for key, value in dValues.iteritems():
                    self.game.myEmpire[key] = value
                print 'Empire Update Success'
            else:
                self.modeMsgBox(serverResult)
        except:
            self.modeMsgBox('setEmpireValues->Connection to Server Lost, Login Again')

    def setLogout(self, clientKey):
        """Send a Logout Request to the Server"""
        try:
            serverResult = self.game.server.logout(clientKey)
            if serverResult == 1:
                print 'Logout Successful, Exit Program'
            else:
                self.modeMsgBox(serverResult)
        except:
            self.modeMsgBox('setLogout->Connection to Server Lost, Login Again')
    
    def submitDesign(self, name):
        """Take Ship Design and submit it to Server for verification and storage"""
        (oldName, hullID, compDict, weaponDict) = self.myShipDesign.getMyDesign()
        dOrder = {'name':name, 'hullID':hullID, 'compDict':compDict, 'weaponDict':weaponDict}
        try:
            serverResult = self.game.server.addShipDesign(self.game.authKey, dOrder)
            if type(serverResult) == types.StringType:
                self.modeMsgBox(serverResult)
            else:
                # design has been accepted by server, retrieve design ID and add to client
                (ID,name) = serverResult
                self.game.shipDesigns[ID] = (name, hullID, compDict, weaponDict)
                self.getEmpireUpdate(['designsLeft'])
        except:
            self.modeMsgBox('submitDesign->Connection to Server Lost, Login Again')
      
    def destroyTempFrames(self):
        """Destroy any Temp Frames"""
        for frame in self.tempFrames:
            frame.destroy()
        self.tempFrames = []
    
    def modeMsgBox(self, messageText):
        """Create a message for the user"""
        self.createMessage(messageText)
    
    def createDialogBox(self, x=-0.1, y=-0.85, text='Insert Dialog Here', 
                        textColor=globals.colors['orange'],displayNextMessage=False):
        """Create a dialog box with text and an ok button"""
        if self.dialogBox == None:
            if globals.isTutorial:
                text = "                    ====================== Cosmica Tutorial Step: %s of %s ======================\n\n%s" % (globals.tutorialStep, globals.tutorialTotalSteps, text)
            self.dialogBox = dialogbox.DialogBox(path=self.guiMediaPath,x=x, y=y, 
                                                 text=text,textColor=textColor,displayNextMessage=displayNextMessage)
            self.dialogBox.setMyMode(self)
            self.gui.append(self.dialogBox)       
    
    def removeDialogBox(self):
        """remove dialogbox"""
        if self.dialogBox != None:
            self.dialogBox.destroy()
            self.dialogBox = None
    
    def createMessage(self, text):
        """Create a new message for user"""
        myMessage = fadingtext.FadingText(self.guiMediaPath, text, self.messagePositions)
        self.messagePositions.append(myMessage.getMyPosition())
        self.playSound('beep03')
    
    def writeToScreen(self, myText, x, z, scale=0.2, 
                      color='default', font=3, wordwrap=10):
        if color == 'default':
            color = Vec4(.1,.1,.8,.8)
        text = textonscreen.TextOnScreen(self.guiMediaPath, myText, scale,font=3)
        text.writeTextToScreen(x, self.depth, z, wordwrap=wordwrap)
        text.setColor(color)
        self.gui.append(text)
    
    def loadObject(self, tex=None, pos='default', depth=55, scale=1,
               transparency=True, parent='cam', model='plane', glow=0):
        if pos == 'default':
            pos = Point2(0,0)
        if parent == 'cam':
            parent = camera
        scaleX = 187.5
        scaleZ = 117.1875
        obj = loader.loadModelCopy('%s%s' % (self.guiMediaPath, model)) #default object uses the plane model
        if parent:
            obj.reparentTo(parent)              #Everything is parented to the camera so
                                            #that it faces the screen
        obj.setPos(Point3(pos.getX(), depth, pos.getY())) #Set initial position
        obj.setSx(scaleX)
        obj.setSz(scaleZ)
        obj.setBin("unsorted", 0)           #This tells Panda not to worry about the
                                            #order this is drawn in. (it prevents an
                                            #effect known as z-fighting)
        if transparency: obj.setTransparency(1) #All of our objects are trasnparent
        if tex:
            tex = loader.loadTexture('%s%s.png' % (self.guiMediaPath, tex)) #Load the texture
            obj.setTexture(tex, 1)                           #Set the texture
      
        self.sims.append(obj)
        obj.setShaderInput('glow',Vec4(glow,0,0,0),glow)
        return obj

    def onEntryFocus(self):
        """When a text Entry is in focus disable all shortcut keys"""
        for gui in self.gui:
            if gui.__module__ in self.entryFocusList:
                gui.ignoreShortcuts()
    
    def onEntryOutFocus(self):
        """When an text Entry is out of focus enable all shortcut keys"""
        for gui in self.gui:
            if gui.__module__ in self.entryFocusList:
                gui.setShortcuts()
    
    def tutorial0(self):
        message = "Welcome to Cosmica!\n\nI see you have selected to go through the tutorial, hence this welcome message, great! \n\nI have setup the tutorial by explaining how Cosmica is played and asking you to complete specific orders by submitting moves to your tutorial game which will activate the next message after you click the help button.\n\nWhen you click ok to remove a message you can always retrieve the message later by clicking the help button, which is always available as one of the top menu buttons.\n\nNormally the help button plays a different role in that it will scan your current situation and give you a quick AI assessment of how you are doing and any areas you might want to focus some thought on. That feature is disabled for this tutorial game.\n\nMy hope is that this tutorial will give you the basics of Cosmica, however, please join the forums on our website at www.playcosmica.com to get more advanced techniques, join multiplayer games, and watch our many developer and user created videos.\n\nI hope you consider joining our growing community of strategy gamers!\n\n -- Chris Lewis (game creator)"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial1(self):
        message = "Thanks for trying out this tutorial, keep in mind that this tutorial does not limit you in what you can do at any given time. If you want the next step to activate you are going to want to follow the directions exactly. If you start doing other things, that's ok, but it might remove your ability to follow the tutorial steps.\n\nIf you really have trouble feel free to bring it up in our forums at www.playcosmica.com.\n\nAs this is a new indie-game I hope you have some patience with us as we work hard to make Cosmica better every week!"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial2(self):
        message = "Ok, lets start with what is Cosmica exactly?\n\nConsider Cosmica a turn-based hybrid strategy game that combines elements of board games like Risk and Diplomacy, with the well established 4X space strategy genre of video games that follow a general game mechanic of:\n\nGrowing an empire (aquiring planets)\nIncreasing your technology (research)\nBuilding a military (ships and troops)\nMaking relationships (diplomacy)\n\nWith the final goal of taking over the provided galactic map, potentially with allies (depending on the map configuration)."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial3(self):
        message = "Like many strategy games the beginning moves are critical to get your empire off on the right start.\n\nAlthough Cosmica maps can be setup in any configuration, the standard maps will have players on the edge of a galaxy map with a homeworld (usually a 40 city sized planet), and some support planets (3 or 4) to support the homeworld.\n\nThis number of planets gives your empire enough cities (population) to get your economy and research going, as you are going to want to establish a good economy if you want to start building military units and expanding towards other empires."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial4(self):
        message = "Lets start with your economy. Your economy is composed of three resources:\nAlloys (AL) (blue color)\nEnergy (EC) (yellow color)\nArrays (IA) (red color)\n\nIt is important that you make sure your planets are setup to build these resources early in the game, and that you are transferring these resources where they are needed to support future turns.\n\nYour homeworld which currently starts the game with some shipyards (to build ships)\nmilitary installations (to build marines)\nresearch centers (to build research points)\ndesign centers (to create ship designs)\nsimulation centers (to simulate ship designs)\nand alloy factories (to increase the production of alloys) each turn.\n\nNotice that in this galaxy your homeworld says 40/40 beside its name. This means all 40 cities are employed, which is what you want.\n\nNotice that your other three planets are not currently working as hard, let's get them working fully over the next few turns."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial5(self):
        # check that steps complete
        mySystem = self.game.allSystems['21']
        if mySystem['name'] == 'Onatarin' and mySystem['cityIndustry'] == [0, 20, 0]:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Notice that all your planets have a blue triangle at the bottom, this designates that the planet cities are focused on building alloys currently. There is also a blue number below each planet.\n\nAny colored number represents the exact amount of that type of resource residing on that planet this turn. You can make your planets focus on multiple resources, but it is more efficient to have them focus on one due to the power of resource factories.\n\nIt is important to get your various planets focusing on different resources so that you are generating all three resources early in the game.\n\nClick on your planetary system: Onatarin, Click cities, reduce the alloys(AL) focus to 0, increase the energy(EC) focus to 20, and click submit"
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial6(self):
        # check that steps complete
        mySystem = self.game.allSystems['21']
        if mySystem['name'] == 'Onatarin' and mySystem['myIndustry']['4'] == 4:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Great! You have now focused Onatarin to build energy (yellow) instead of alloys (blue).\n\nThis will be helpful for future military growth in a few turns. Lets now click back on Onatarin, click industry, click on Crystal Mine, choose Basic, and build the max mines you can at 100 Alloys per mine which is 4 (you only have 400 Alloys on your planet), then click submit."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial7(self):
        # check that steps complete
        mySystem1 = self.game.allSystems['41']
        mySystem2 = self.game.allSystems['53']
        if mySystem1['name'] == 'Cygnus' and mySystem1['cityIndustry'] == [0, 0, 30] and mySystem1['myIndustry']['7'] == 6 and \
           mySystem2['name'] == 'Strig' and mySystem2['cityIndustry'] == [0, 20, 0] and mySystem2['myIndustry']['4'] == 4:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Nice Work! You now have focused 4 of your 20 cities on crystal mines, notice that the output of energy is higher as each mine increases the percentage of crystal production, and since all your cities are focused on energy, the total energy production (yellow) is higher than if you divided a planet into multiple resource types.\n\nChange the city focus to energy on Strig and build 4 simple Cystal Mines.\n\nChange the city focus to arrays (IA) on Cygnus, and build 6 Simple Synthetic Systems on Cygnus as well.\n\nDo this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial8(self):
        message = "Excellent! you now have a homeworld focused on alloys(blue), systems Strig and Onatarin focused on energy(yellow), and Cygnus focused on arrays(red). The next thing we want to do is move resources around to where they need to go to accomplish two short term goals:\n\n1) make sure all our planets are fully focused on industry (no idle cities)\n\n2) make sure our homeworld has resources streaming into it via trade routes so that in a few turns we can start building ships and troops to start our expansion into the galaxy. \n\nTo accomplish this we need to leverage trade routes."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
        
    def tutorial9(self):
        message = "Trade routes allow an empire to move the three resources (alloys, energy, arrays) from one planet to another. The planets have to either be adjacent to each other (connected via a line designating a warp point), or if two planets have warp gates, trade can warp between them (taking away some warp gate points).\n\nThere are three trade types:\n\nA Gen trade route will allow a planets newly created resources to all be sent towards another planet on the same turn they are generated.\n\nA one-time trade route will send resources from one planet to another one-time only.\n\nA standard trade route will attempt to send trade between planets forever as long as the sending planet has the resources available."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial10(self):
        # check that steps complete
        mySystemFrom = self.game.allSystems['40']
        mySystemTo = self.game.allSystems['21']
        if mySystemFrom['name'] == 'Iphameda' and mySystemTo['name'] == 'Onatarin' and '40-21-REG' in self.game.tradeRoutes.keys():
            myTradeRouteDict = self.game.tradeRoutes['40-21-REG']
            if myTradeRouteDict['oneTime'] == 1 and myTradeRouteDict['AL'] == 1600 and myTradeRouteDict['EC'] == 0 and myTradeRouteDict['IA'] == 0:
                globals.tutorialStep += 1
                self.displayTutorialMessage()
                return
            
        message = "Lets start with creating a one-type trade route to send all the current alloys on our homeworld to Onatarin so that it will have more alloys to build factories in the following turn.\n\nClick on your homeworld, click trade, click on Onatarin, choose alloys, and choose all of the available alloys.\n\n Finally, click the one-time trade button."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
               
    def tutorial11(self):
        # check that steps complete
        mySystemFrom = self.game.allSystems['40']
        mySystemTo = self.game.allSystems['53']
        if mySystemFrom['name'] == 'Iphameda' and mySystemTo['name'] == 'Strig' and '40-53-GEN' in self.game.tradeRoutes.keys():
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Great job! Notice that the trade route has been created, feel free to click on it, you could modify it, cancel it, or just leave it there (which is what we want for now).\n\nNow, to expedite alloys going to our feeder planets, lets create a gen trade route from our homeworld (that creates alloys) to Strig.\n\nThis will send whatever our homeworld makes next turn in alloys directly to Strig next round. Click on our homeworld, click on trade, click on Strig, and click gen trade route. Do This Now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
    
    def tutorial12(self):
        # check that steps complete
        if '53-40-GEN' in self.game.tradeRoutes.keys() and '21-40-GEN' in self.game.tradeRoutes.keys() and '41-40-GEN' in self.game.tradeRoutes.keys():
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Nice work! Notice that this arrow looks different, all gen trade routes have the same look, but if you zoom in you can see what expected resources will go to the receiving planet, which is based on the production of resources from the planet setting up the trade.\n\nNext I want you to setup gen trade routes from Onatarin, Strig, and Cygnus to your homeworld (sending any created EC and IA resources there for future use). energy to your homeworld). Do this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)
        
    def tutorial13(self):
        message = "Our economy has been setup to startup quite nicely, we will continue to build it up next round, in the meantime lets move over to technology.\n\nClick on the tech button at the top to view your technology tree, do this now."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guigreen'],displayNextMessage=message)    

    def tutorial14(self):
        # check that steps complete
        if self.game.myEmpire['rpAvail'] == 0:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message = "Great, in Cosmica the technology tree is faster to develop than your more standard 4X game. Once you build a few research centers you should be gaining technology every round, sometimes you could be gaining 5-10 technologies in one round! In this game setup you are given the first age of technology (the nuclear age).\n\nIn some games you will be given the fusion age as well, but not in this tutorial.\n\nIn order to research the many technologies in the fusion age you first need to research the Fusion Age of Technology tech beaker.\n\nNotice you can click on any technology and gain information about what it does for you. For now, click on the Fusion Age of Technology, and commit all of your available technology points (225) (that you got from your research centers on your homeworld), and click submit. Do this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guigreen'],displayNextMessage=message)
        
    def tutorial15(self):
        message = "Nice, notice that you have an 37 percent chance of gaining this technology. When the round ends the game will determine via a random roll if you gained that technology or not. Once you gain that technology you can start researching other technologies and gaining the benefits they offer.\n\nIt is my suggestion that you prioritize on research centers (so you can upgrade them and get more technology points per turn, followed by the alloy, energy, and array factories (so you can upgrade and make more resources and credits).\n\nThen start focusing on your ship components and weapons (so you can make more powerful ships to take over the galaxy)."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guigreen'],displayNextMessage=message) 
        
    def tutorial16(self):
        message = "Ok, you have now done almost everything you should do in your first round of play. You will find that the first 5 rounds are very quick as players build out their economy, start some simple research, and maybe play with a few ship designs.\n\nExpansion and combat will not start until enough resources are gathered that a fleet and army can be assembled.\n\nSome players might even avoid expansion and focus on technology early on, other players would take a different approach. It is my suggestion that some light expansion is recommended to give your empire more cities to control allowing more research in the long run. Before we end our turn lets take a quick look at the ship design screen by clicking on it from the main menu above. Do this now."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message) 
        
    def tutorial17(self):
        message = "Notice that the first thing you have to decide is if you want to design with your current technology or with all technology, or just start a simulation of existing designs.\n\nCosmica was purposely designed to give a player a lot of flexibility in ship design.\n\nAs you play Cosmica you will find that a well-designed fleet of ships will make a big difference in your attempts to dominate opponents in space. As you start to play Cosmica you will learn that critical fleet battles between empires can swing the fortunes of empires quickly.\n\nFor this reason a well-designed and upgraded fleet composed of ship designs that counter other fleet designs, and complement each other is of critical importance. Ship designing and simulating is also a lot of fun, and can take a lot of time for players that want that extra edge."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message) 
        
    def tutorial18(self):
        message = "First, lets start with the easy part, simulating a ship battle. If ship designing is something that intimidates you, do not worry. Cosmica comes with a set of neutral ship designs that the neutral (white) planets use to defend themselves from aggressive empires such as yours. These designs are generally quite sound, and you could get away with using them without worrying too much about making your own designs.\n\nSince these ship designs are already pre-made and available, lets setup a ship simulation between several ship variants.\n\nIn order to simulate ships you need to have constructed Simulation Centers. Each simulation center you build on a system will provide you will a certain number of simulation points per round. These points do not stack for later use. Think of them as simulation engineers waiting for you to ask them to run some simulations on your behalf. If you do not ask them to do anything they just hang out and drink space coffee all day."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial19(self):
        # check that steps complete
        if self.game.myEmpire['simulationsLeft'] == 0:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message = "Since you are a new empire and you are focusing on building up your economy you only have one lonely Simple Simulation Center currently on your homeworld.\n\nThis gives you only 1 simulation point, which is enough to simulation one ship design against one other design. The formulae for how many ship simulation points will be required:\n\n  = (the number of ship designs of Team A x (the number of ship designs of Team B)\n\nFor our test feel free to select any ship design, assign a number of the ships to team A, select another design, and assign to Team B. Then click the Simulate button. Do this now and enjoy the Battle!\n\nRemember, you press space-bar to pause and un-pause, use the mouse to navigate and zoom, feel free to select ships to see how they act with each other. Click on any main menu bar to leave the simulation at any time."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial20(self):
        message = "I hope that was entertaining! One good way to learn about ship designs is to use the singleplayer function to build a bunch of simulation centers and play with ship designs, then take that knowledge to your slower (but more important) multiplayer games. Simulations are also critical when we are designing ships as it is a great way to make sure your designs work as you intend.\n\nIt is very common for example to make a ship that does not have the correct ammunition, something you would want to learn from your simulations, not in real battle!"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial21(self):
        message = "Ok, lets try to create a ship design. click back on design and choose all technology. Notice that the screen is full of every type of ship hull, and there is a list of every Neutral Ship Design for you to review at any time.\n\nCosmica was designed to give you the option to build any ship design before you have the technology to build your ships.\n\nThe reasoning here is that you can plan out your fleet and research towards those goals.\n\nClick on the Neutral Design with SDN in its name. Notice that it says SHIP PAST TECH LEVEL, this lets you know that you cannot build this ship currently.\n\nNow click the Design button again and click on Current Technology."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial22(self):
        # check that steps complete
        if self.game.myEmpire['designsLeft'] == 0:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message = "Now notice that you have far fewer designs to select from. The only available designs will be ones that you can currently build. Click on a hull type. To build a valid ship design in Cosmica you need to have at least one Engine component, one Rotation Component, and one power component.\n\nNotice that there are 4 quadrants. When a ship takes damage it will go into the quadrant that the weapon hit into. When you place a weapon notice that you can also place its direction.\n\nThis is important as a ship will behave based on the direction its weapons face. Try builing a valid design. Remember to give it a name in the text box to the right. You will have to press enter on the text box in order to enable the submit design button. Do this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)        
        
    def tutorial23(self):
        message = "Good Job, your first Ship Design! I would not build any of these ships without first testing them in the simulator, but since we used our our 1 simulation point we have no idea if this design is any good. The good news is that if you go back to the Designs main screen, click on current technology, click on your new design, and click remove design. This will remove the design from your list of designs.\n\nThis is a nice feature when you have older designs that are no longer being used, but it can only be done if you have no more ships with that design in play.\n\nKeep in mind that you can always upgrade your ships from one design to a new design, and the costs will depend on how many components are different. So when you are making new upgrades, try to keep them as similar to the old design as you can, but with better components, if you want a reasonable upgrade cost."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial24(self):
        message = "I do recommend that you look on our website forums for more information and videos on ship designs, however I feel I should explain the different ship classes.\n\nShips are divided into several classes:\n\nMost ships are Warships, these ships will attack the nearest ship or drone and shoot at it until it dies with whatever weapons the warship has. Some warship hulls are specialized to target other warship hulls like carriers and assault ships.\n\nConsider any ship that is not a Carrier, Assault Ship, or a Platform to be a Warship of various sizes."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial25(self):
        message = "Carriers are specialized ships that cannot carry regular weapons, instead you install drones as weapons. Drones are also hull types, but they can only be installed in Carriers or Platforms, not warships.\n\nCarriers are powerful mid to late game ships as they provide a fighter screen that distracts most warships, keeping them from shooting at more valuable ships.\n\nDrones are also expendable as long as the Carrier survives the battle, any drones will be reset for the next battle."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial26(self):
        message = "Assault ships are specilized ships that cannot carry weapons, instead you want to install marine pods which house special space marines that are trained to board enemy ships. If an assault ship is fast enough and protected enough it will crash into an enemy ship and its space marines will attempt to board and take over the enemy ship, making it your ship, even if it is of a higher technology then what you possess currently."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial27(self):
        message = "Platforms are defensive ships that cannot be used to attack any enemy planetary systems. They do however have much more flexibility in that they hold a lot of space for anything from drones to large weapons.\n\nPlatforms can also be converted into mobile shipyards by installing engineering stations, a powerful tactic in the mid to late game of Cosmica."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['guiyellow'],displayNextMessage=message)
        
    def tutorial28(self):
        # check that steps complete
        if self.game.currentRound > 1:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message = "Ok that was a lot of good information, lets move into the next round and build up our forces to take over one of the nearby neutral systems.\n\nTo do this click on the End Round button from the top menu, and choose to End and Wait so that we can start our next round of play. Do this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['ltpurple'],displayNextMessage=message)
        
    def tutorial29(self):
        message = "When the round ends, I suggest your first step besides seeing visually on the galactic map how your empire did from a military standpoint would be to click on the Mail button from the top menu. Do this now."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['ltpurple'],displayNextMessage=message)
        
    def tutorial30(self):
        message = "Notice that the mail is broken down into rounds, you can click on any past round of play and review any messages in there as well. If you are playing a multiplayer game you will also get all your end-round messages emailed to you as a way both inform you that a new round has started, and to also give you some information on how your empire faired when the round ended.\n\nThis is a good time to explain that Cosmica deals with turn-based strategy differently then many strategy games in that all empire moves are handled at the same time once every player has submitted their turns to the game server.\n\nThe game server will turn-over after a certain limit of time that you can access from to top left corner, or it will end sooner based on players finishing their turn of play.\n\nThe advantage of this system is that players can finish their turn when it works with their schedule and as long as everyone stays engaged with their turns, Cosmica tends to turn into a deep strategy and diplomacy game without the requirement for a ton of player committment time-wise, day-to-day."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['ltpurple'],displayNextMessage=message)    
    
    def tutorial31(self):
        # check that steps complete
        if self.game.currentRound > 5:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message = "Ok, lets try to invade a planet. To do this we are first going to need some resources. Notice your trade routes in Round 2 activated and you now have some alloys (blue) at two of your three sub-systems.\n\nTake this opportunity to build the appropriate factories at these locations so that more resources will be generated each round. Also send some more alloys from your homeworld via a gen trade to your other systems that still need alloys to build factories in round 3. I wont check if you do this, but try to get all your systems fully activated with industry.\n\nYour goal is to build a stockpile of resources on your homeworld.\n\nOne other thing you can try is to buy resources (or sell them) directly on the market. You do this by clicking on your homeowlrd, click market, and buy or sell resources. Generally speaking choose a price one above or below the asking price if you want a better chance of succeeding.\n\nYou do not have to do this now, but I wanted to point it out.\n\nThe market is a great way to make some quick cash by selling extra resources, and it is a great way to build up your fleets and armies quickly at the expense of credits.\n\nI will leave you to this till lets say round 6."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['orange'],displayNextMessage=message)    
    
    def tutorial32(self):
        # check that steps complete
        for industryID in funcs.sortStringList(self.game.myEmpire['industryOrders'].keys()):
            myOrder = self.game.myEmpire['industryOrders'][industryID]
            if myOrder['type'] == 'Add Regiment' and myOrder['round'] == self.game.currentRound:
                globals.tutorialStep += 1
                self.displayTutorialMessage()                
                return
            
        message = "Great, it is at least round 6 for you and if you are in round 6 and you did not use the market you should have around 4000 alloys (blue), 5360 energy (yellow), and 2160 arrays (red) on your homeworld.\n\nThis assumes you built up your three sub planetary systems with factories and sent any remaining alloys back to your homeworld. In any case you now have enough resources to build some ships and marines!\n\nMarines are easy to build, click on your homeworld, click on Marines, click on Build Marines, choose Light Nuclear Artillery, and build the maximum which would be 6 and click submit. Do this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)    
    
    def tutorial33(self):
        message = "Nice work. In the current version of Cosmica marines are fairly simple. There are three types:\n\nArtillery Marines require energy (EC) resources to build and are strong against Infrantry and Militia Fortresses (what the neutral planets use to defend themselves).\n\nMechanical Marines require alloy (AL) resources to build and are strong against Artillery marines.\n\nInfantry Marines require array (IA) resources and are strong against Mechanical marines. Generally it is a good tactic to focus on Artillery marines early on to make your expansion against neutral systems easier, and then switch to other types depending on what your opponents are building.\n\nLike anything in Cosmica you can change your mind while doing your turn. If you click on your marines you can decide to reduce the number of marines from this order and the server will give you back the appropriate resources and credits. Also notice that near your homeworld there is now a symbol that used to be grey, but now it is yellow. This gives you the tip that your industry is working on building something on that Planetary System.\n\nLets focus on ships next."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)
        
    def tutorial34(self):
        # check that steps complete
        for industryID in funcs.sortStringList(self.game.myEmpire['industryOrders'].keys()):
            myOrder = self.game.myEmpire['industryOrders'][industryID]
            if myOrder['type'] == 'Add Ship' and myOrder['round'] == self.game.currentRound:
                globals.tutorialStep += 1
                self.displayTutorialMessage()                
                return
        
        message = "Great. Now lets build some ships. Click on your homeworld, click on Ships, click on Build Ships. You will see a list of ship designs that you are allowed to build based on your current technology. Choose one and the Ship information will pop up including its cost. Choose any ship that you have the resources for, select one and submit. If you cannot add any ships it is because you do not have enough resources. Fast forward a few more rounds and try again. Try this now."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)    
    
    def tutorial35(self):
        # check that steps complete
        if len(self.game.myShips.keys()) > 0 and len(self.game.myArmies.keys()) > 0:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return
        
        message = "Nice work! If you had an optimal amount of resources you should have been able to build up to 5 HCO-11 Neutral Ships. This is a side note, but in this version of Cosmica the early testers have noticed that the HCO-11 design is quite solid, and I recommend you consider this design if you want to mass up a bunch of ships that will do a lot of damage in the early game against smaller neutral planets (size 10-15-20).\n\nSo at this point you should have put in orders with your military for 6 marine regiments, and up to 5 corvettes, not bad! End the round and lets see what we can do with your new recruits!"
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)
        
    def tutorial36(self):
        message = "Looks like you have some ships and some armies which is great, lets give them some a glorious battle!\n\nAll Neutral (white) planets will have a random fleet that is based on the map configuration, but generally goes up in defence as the neutral planets get bigger in size.\n\nYour five HCO11 ships should have a good chance against the neutral planet.\n\nOne important thing you can do to make sure is to build a radar station on a nearby friendly planet. Radar stations once built will provide you with the ability to click on adjacent planets and you will get a report on their strength.\n\nAnother way would be to sacrifice a cheap ship or one marine troop to attack early. Every ship battle is recorded for your later viewing, so you can use this information to determine the exact makeup of the planet defences, which gives you the option to simulate potential solutions as required.\n\nNeutral Planets will never attack you, and their ships will never repair, they are meant to slow you down, your real concern are the other empires in play."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)    
        
    def tutorial37(self):
        # check that steps complete
        if len(self.game.warpedArmadas.keys()) > 0 and len(self.game.warpedArmies.keys()) > 0:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return
        
        message = "Ok, lets attack the 5 city Neutral Planet. If you wanted to play it safe you would attack with your Fleet first, wait one round then move in your troops. Lets take a chance and send them in together!\n\nTo move your Ships simply click on the ship icon on the top right corner of your Homeworld. Click on the Neutral 5 Planet, select all the ships, and click WARP SHIPS.\n\nNotice they will show up in the bottom right corner of the Neutral Planet. Any Ships or Armies that have not moved will be in the top right corner, and moved ones in the bottom right.\n\nDo the same thing with your Army. Each Marine Regiments comes with its own transport ship, when you do not move them and they are on a friendly Planet they will defend on the planet surface.\n\nIf you move them however they have to survive the space battle as a troop transport before they are allowed to land on the Planetary System in question. Once they have both moved end the turn and you will notice that there is a bit of a delay.\n\nThis is because the server is resolving all battles, it should not take too long."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['red'],displayNextMessage=message)    
    
    def tutorial38(self):
        message = "Ok, well hopefully we took this planet, you will be able to tell if its color changed, but to watch the battle click on the WAR button and click on your battle and watch the results! After that if you go to the MAIL section you can review how the ground battle unfolded. We might have been a bit too agressive here, but by my calculations you should have won this small planet, congrats!"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['ltpurple'],displayNextMessage=message)
        
    def tutorial39(self):
        message = "I think at this point you should have the basic grasp of Cosmica, and everyone here at NeuroJump wants to thank you for considering our indie game.\n\nWe hope you consider joining our community as we build out this game and the many planned improvements in store!\n\nWe Hope to see you online at www.playcosmica.com!\n\nChris, Steve, and Jeremy (NeuroJump) 2018-2019."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, text=message,textColor=globals.colors['pink'],displayNextMessage=message)        
    
    def displayTutorialMessage(self):
        """Display the latest tutorial message"""
        try:
            myMethod = getattr(self, 'tutorial%s' % globals.tutorialStep)
            myMethod() 
        except:
            globals.isTutorial = False

            
        