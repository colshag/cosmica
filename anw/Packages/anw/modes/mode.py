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
    import direct.directbase.DirectStart
    from anw.gui import textonscreen, fadingtext, mainmenubuttons, line, dialogbox
    from direct.directtools.DirectGeometry import LineNodePath
    from direct.gui.OnscreenImage import OnscreenImage    

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
        self.zoomSpeed = 5.0
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
                    color = ['cyan']
                elif 'SCANNING INDUSTRY' in message:
                    color = ['orange']
                elif 'SCANNING MILITARY' in message:
                    color = ['red']
                self.createDialogBox(x=-0.1,y=0.7,texts=[message],textColors=color)
       
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
            tutorialInfo = {'tutorialGame':self.game.myGalaxy['name'], 'tutorialStep':globals.tutorialStep, 'tutorialStepComplete':globals.tutorialStepComplete}
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
        """ zoom in """
        if camera.getY() <= 5:
            if self.enableScrollWheelZoom:
                self.stopCameraTasks()
                self.zoomInCameraAmount(10.0)
        
    def onMouseWheelDown(self):
        """ zoom out """
        if camera.getY() >= -100:
            if self.enableScrollWheelZoom:
                self.stopCameraTasks()
                self.zoomOutCameraAmount(10.0)
        
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
        base.setBackgroundColor(globals.colors['guiblue4'])

    def endMyTurn(self):
        """End the players Turn"""
        try:
            result = self.game.server.endEmpireTurn(self.game.authKey)
            if result == 0:
                if self.game.myEmpire['roundComplete'] == 1:
                    self.modeMsgBox('You have now un-ended your turn')
                    self.game.myEmpire['roundComplete'] = 0
                else:
                    self.modeMsgBox('Your turn has been ended, thankyou')
                    self.game.myEmpire['roundComplete'] = 1
                self.mainmenu.writeTextRoundEnds()
            elif type(result) == types.StringType:
                self.modeMsgBox(result)
            else:
                """End Turn and wait for it to end"""
                result = self.game.server.endRound(self.game.authKey)
                self.game.server.logout(self.game.authKey)
                from anw.modes.modelogin import ModeLogin
                newMode = ModeLogin(self.game, 200)
                self.game.enterMode(newMode)
        except:
            self.modeMsgBox('endMyTurn->Connection to Server Lost')

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
    
    def createDialogBox(self, x=-0.1, y=-0.85, texts=['Insert Dialog Here'], 
                        textColors=['orange'],displayNextMessage=False):
        """Create a dialog box with text and an ok button"""
        if self.dialogBox == None:
            if globals.isTutorial:
                texts[0] = "      ====================== Cosmica Tutorial Step: %s of %s ======================\n\n%s" % (globals.tutorialStep, globals.tutorialTotalSteps, texts[0])
            self.dialogBox = dialogbox.DialogBox(path=self.guiMediaPath, x=x, y=y, texts=texts, textColors=textColors)
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
        message1 = "Welcome to Cosmica, a turn-based strategy game combining elements of strategic board and video games."
        message2 = "This tutorial will walk you through several turns of a typical game. You will learn how to navigate the interface, develop your planets industry, research technology, build ships and marines, and you will even have a small skirmish to take over a neighbouring planet.\n\nIn order to advance through each stage of the tutorial, you will have to complete the tasks required. At any time, you may click on the HELP button on the Galactic Command Bar to review you current task."
        message3 = "Press MAP to go to the Galactic Map Screen."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2,message3],textColors=['guigreen','orange','cyan'])
    
    def tutorial1(self):
        message1 = "This is the galaxy map. You will see several planets. Some of them are under your control (gold) and others are neutral planets (white). The number beside each planet represents how many cities are on each planet. These cities can be put to work.\n\nYour homeworld has 40 cities on it."
        message2 = "Click on your Homeworld."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial2(self):
        message1 = "This is the planets details. Information regarding each planets cities, industries, trade deals, market investments, and ship and marine build orders can be found here by clicking on each of the buttons on the Planetary Command Bar."
        message2 = "Click Industry."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial3(self):
        message1 = "Your homeworld is currently using all 40 of its cities in some capacity. Whenever possible, ensure all your cities are assigned to an Industry. Unassigned cities are a drain on your economy and you will be penalized each round for each unassigned city in your empire."
        message2 = "Click the right mouse button or press escape to go back to the Galaxy Map."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial4(self):
        message1 = "In Cosmica, your cities are assigned one of three resources to produce. Alloys (blue), Energy, (yellow), and Arrays (red).\n\nThe coloured arrows under each planet will tell you which of these resources are being produced there."
        message2 = "Click on Onatarin."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial5(self):
        message1 = "Lets change the resource focus of the Cities on Onatarin.\n\n"
        message2 = "Click on Cities."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])    
    
    def tutorial6(self):
        # check that steps complete
        mySystem = self.game.allSystems['21']
        if mySystem['name'] == 'Onatarin' and mySystem['cityIndustry'] == [0, 20, 0] and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "It is important to create a diverse economy. Since your homeworld is producing Alloys, assign Onatarin to produce Energy. Using the addition/subtraction menu, do the following:"
        message2 = "Reduce Alloy (AL) production to 0.\nIncrease Energy (EC) production to 20.\nNote: You can use the Mousewheel to increase and decrease faster!\nClick Submit."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial7(self):
        # check that steps complete
        mySystem = self.game.allSystems['21']
        if mySystem['name'] == 'Onatarin' and mySystem['myIndustry']['4'] == 4 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "Now that your cities are focused on producing energy, lets build some industry that will make Onatarin more productive at building the energy resource."
        message2 = "Click on Onatarin.\nClick Industries.\nClick on Crystal Mines.\nAdd four basic Crystal Mines.\nClick submit."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
        
    def tutorial8(self):
        # check that steps complete
        mySystem1 = self.game.allSystems['41']
        mySystem2 = self.game.allSystems['53']
        if mySystem1['name'] == 'Cygnus' and mySystem1['cityIndustry'] == [0, 0, 30] and mySystem1['myIndustry']['7'] == 6 and \
           mySystem2['name'] == 'Strig' and mySystem2['cityIndustry'] == [0, 20, 0] and mySystem2['myIndustry']['4'] == 4 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "Now do the following for your other planets:"
        message2 = "Change Strigs production focus to Energy and build Crystal Mines.\nChange Cyngus production focus to Arrays and build Synthetic Systems."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
        
    def tutorial9(self):
        message1 = "Excellent! You have now learned the basics of changing a planets production focus and building the correct mines to match. Next, we will look at how trade works between planets."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['guigreen'])
        
    def tutorial10(self):
        message1 = "Trade is critical to an empires success. Trade routes allow an empire to move the three resources (Alloys, Energy, Arrays) from one adjacent planet to another.\n\nThere are three types of Trade routes:\n\nGen Trade: a reoccurring trade agreement that automatically sends whatever resources the trading planet generates each turn to the receiving planet.\n\nOne-Time Trade: a single trade that sends a specified amount of resources from the trading planet to the receiving planet.\n\nStandard Trade: a trade route that will attempt to continue the route as long as the resource is available each turn."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['orange'])
    
    def tutorial11(self):
        # check that steps complete
        mySystemFrom = self.game.allSystems['40']
        mySystemTo = self.game.allSystems['21']
        if mySystemFrom['name'] == 'Iphameda' and mySystemTo['name'] == 'Onatarin' and '40-21-REG' in self.game.tradeRoutes.keys():
            myTradeRouteDict = self.game.tradeRoutes['40-21-REG']
            if myTradeRouteDict['oneTime'] == 1 and myTradeRouteDict['AL'] == 1600 and myTradeRouteDict['EC'] == 0 and myTradeRouteDict['IA'] == 0 and globals.tutorialGoBackDisabled:
                globals.tutorialStep += 1
                self.displayTutorialMessage()
                return
            
        message1 = "Since we assigned Onatarin to produce energy, it needs alloys to build more mines. This requires Alloys that you currently have at your homeworld, lets send alloys to Onatarin."
        message2 = "DO the following:\nClick on your homeworld.\nClick Trade.\nClick Onatarin.\nClick Alloys.\nClick to add all available alloys to trade.\nClick One-Time Trade."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
               
    def tutorial12(self):
        # check that steps complete
        mySystemFrom = self.game.allSystems['40']
        mySystemTo = self.game.allSystems['53']
        if mySystemFrom['name'] == 'Iphameda' and mySystemTo['name'] == 'Strig' and '40-53-GEN' in self.game.tradeRoutes.keys() and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "Strig will also need alloys for its factories, but our homeworld has no more to give from available alloys, however we can send its alloys that it will produce next round as a Gen Trade. Lets create a Gen Trade route to Strig from your homeworld."
        message2 = "Do the following:\nClick on your homeworld.\nClick Trade.\nClick Strig.\nClick Gen Trade Route."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
    
    def tutorial13(self):
        # check that steps complete
        if '53-40-GEN' in self.game.tradeRoutes.keys() and '21-40-GEN' in self.game.tradeRoutes.keys() and '41-40-GEN' in self.game.tradeRoutes.keys() and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "It is important in the early game to ensure your planets are sending their resources back to your homeworld."
        message2 = "Using your knowledge of trading, do the following:\nEstablish a Gen Trade agreement from Onatarin to your homeworld.\nEstablish a Gen Trade agreement from Strig to your homeworld.\nEstablish a Gen Trade agreement from Cygnus to your homeworld."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
        
    def tutorial14(self):
        message1 = "Perfect! You now know how to create the three different trade agreements available to you in Cosmica. You can also adjust a trade agreement by clicking on the arrow that represents it on the Galaxy Map."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['guigreen'])
    
    def tutorial15(self):
        message1 = "Next, we need to develop technology to give our empire the edge in production, ship design, and military."
        message2 = "Click on Technology."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, texts=[message1,message2],textColors=['orange','cyan'])
    
    
    def tutorial16(self):
        message1 = "This is the technology tree. It is divided into three ages of technology, Nuclear, Fusion, and Plasma. It is completely up to you how you advance through the tree and what technology you prioritize."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.7, texts=[message1],textColors=['orange'])
      
    def tutorial17(self):
        # check that steps complete
        if self.game.myEmpire['rpAvail'] == 0 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message1 = "Your available research points are based on how many research centers you have in your empire. The more points you assign to researching a technology increases your chances of discovering it. This means you can even make discoveries without putting all of the required points into it. Luck often plays a role in research."
        message2 = "Do the following:\nClick on the Fusion Age of Technology.\nAdd all of your available technology points.\nClick submit."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
        
    def tutorial18(self):
        # check that steps complete
        if self.game.currentRound > 1 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()            
            return
        
        message1 = "Congratulations! You have completed all of the tasks you will want to consider on your first turn. You have changed your cities production focus, established trade routes, and spent your research points.\n\nCosmica is a turn-based game and you will not see the fruits of your labour until you advance to the next turn. This is true for both single and multiplayer games."
        message2 = "Click End Round."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.7, texts=[message1,message2],textColors=['guigreen','cyan'])
         
    def tutorial19(self):
        # check that steps complete
        if self.game.currentRound > 5 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()
            return
        
        message1 = "It is now Round %d and the trades you made and technology you researched will have progressed." % self.game.currentRound
        message2 = "Continue to build mines on your cities and add research points to the Technology tree each turn.\n\nRepeat these tasks until Round 6."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2],textColors=['orange','cyan'])

    def tutorial20(self):
        message1 = "Congratulations! It is Round 6 and all your cities are working and you have a thriving economy. Your homeworld should have around 4000 Alloys, 5360 Energy, and 2160 Arrays at this point. We will need these resources to build ships and a military to invade a nearby planet."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['guigreen'])

    def tutorial21(self):
        message1 = "In order to successfully invade a planet, an empire must destroy any enemy ships protecting the planet, as well as overwhelm the planets ground defenses using your military."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['orange'])

    def tutorial22(self):
        # check that steps complete
        for industryID in funcs.sortStringList(self.game.myEmpire['industryOrders'].keys()):
            myOrder = self.game.myEmpire['industryOrders'][industryID]
            if myOrder['type'] == 'Add Regiment' and myOrder['round'] == self.game.currentRound and globals.tutorialGoBackDisabled:
                globals.tutorialStep += 1
                self.displayTutorialMessage()                
                return
            
        message1 = "There are three types of marines: Artillery, Mechanical, and Infantry. Each type has different build requirements and are strong against different types of units."
        message2 = "Do the following to build marines:\nClick on your homeworld.\nClick Marines.\nClick Build Marines.\nClick Heavy Nuclear Artillery.\nOrder six marines.\nClick submit."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])
  
    def tutorial23(self):
        message1 = "Cosmica allows players to build completely custom ship designs. Ingenious ship design can be a significant strategic advantage. This tutorial will use default designs, but it is worth your time to explore that area of the game once you are comfortable with the basics."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['guigreen'])

    def tutorial24(self):
        # check that steps complete
        if len(self.game.myShips.keys()) > 0 and len(self.game.myArmies.keys()) > 0 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return
            
        message1 = "It is time to build a small fleet of ships."
        message2 = "Do the following:\nClick on your homeworld.\nClick Ships.\nClick Build Ships.\nClick HCO 11 Neutral Ship Design.\nPlace an order for five ships.\nClick Submit.\nEnd Your Turn."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.15, y=-0.25, texts=[message1,message2],textColors=['orange','cyan'])  

    def tutorial25(self):
        message1 = "Nice! You have now learned the basics of ship and marine building. you should have around six marine regiments and five corvettes. Lets use them!"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['guigreen'])

    def tutorial26(self):
        message1 = "The first planets you will encounter will be neutral (white). Each neutral planet has its own planetary defenses based on its size. Neutral Planets will never attack you and their ships will never repair. The are meant to slow you down, not eliminate you. Your real concern are the other empires in play."
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1],textColors=['orange'])
          
    def tutorial27(self):
        # check that steps complete
        if len(self.game.warpedArmadas.keys()) > 0 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return
        
        message1 = "It is time to launch your attack. Target the 5 city Neutral Planet. Normally, you would send your fleet in to destroy the ships and send your military afterward so you do not expose your defenseless military transports to enemy ships. However, this planet has very weak defense and will pose no threat to your invading force."
        message2 = "Send your ships to the neutral planet by doing the following:\nClick on the ship icon near your homeworld.\nClick on the Neutral Planet.\nClick Select all.\nClick Warp Ships."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.25, y=0.8, texts=[message1,message2],textColors=['orange','cyan'])

    def tutorial28(self):
        # check that steps complete
        if len(self.game.warpedArmies.keys()) > 0 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return
        
        message1 = "Notice the ship icon has moved from your homeworld to the neutral planet. They are in transit and will attack once you end your turn."
        message2 = "Do the same thing with your military.\nClick on the tank icon near your homeworld.\nClick on the Neutral Planet.\nClick Select All.\nClick Warp Armies."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=0.25, y=0.8, texts=[message1,message2],textColors=['orange','cyan'])


    def tutorial29(self):
        # check that steps complete
        if len(self.game.shipBattleDict.keys()) > 0 and globals.tutorialGoBackDisabled:
            globals.tutorialStep += 1
            self.displayTutorialMessage()                
            return            
        message1 = "Congratulations! You have just sent your ships and military to invade a neighbouring planet. Once you end your turn, your battle will resolve and you will be able to watch a replay of the outcome."
        message2 = "End your turn now to allow the game to resolve your invasion."
        globals.tutorialStepComplete = False
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2],textColors=['guigreen','cyan'])
        
    def tutorial30(self):
        message1 = "You will notice the neutral planet is now gold! You have taken your first planet and can now use it to produce more resources for your empire. To watch the battle click on the WAR button from the main menu.\n\nYou have now experienced the basics of Cosmica. There is still a lot to learn, technologies to discover, strategies to master, and empires to conquer, but this should give you a strong starting point before entering into multiplayer."
        message2 = "To learn more about advanced gameplay strategies and tutorials, join our community at playcosmica.com. Thanks for playing!"
        globals.tutorialStepComplete = True
        self.createDialogBox(x=-0.5, y=0.8, texts=[message1,message2],textColors=['orange','ltpurple'])
       
    def displayTutorialMessage(self):
        """Display the latest tutorial message"""
        try:
            myMethod = getattr(self, 'tutorial%s' % globals.tutorialStep)
            myMethod() 
        except:
            globals.isTutorial = False

            
        