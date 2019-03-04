# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# ai.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# An AI is a player controlled by the computer
# ---------------------------------------------------------------------------
import random
import string
from anw.func import root, funcs, globals, storedata

ai_types = [{'type':'1', 'name':'patton', 'tech':20, 'minthreat':1.2, 'aggressiveness':0.9},
            {'type':'2', 'name':'montgomery', 'tech':20, 'minthreat':0.6, 'aggressiveness':0.5},
            {'type':'3', 'name':'yamato', 'tech':20, 'minthreat':0.8, 'aggressiveness':0.7}
            ]

ai_builds_techreq = {'misc': [ ['1'], ['107','111'] ],
                     'depot': [ ['1'], ['107', '111'] ],
                     'defence': [ ['1'], ['101'] ],
                     'energy': [ ['1'], ['118'] ],
                     'array': [ ['1'], ['129'] ],
                     'alloy': [ ['1'], ['111'] ],
                     }
                      

ai_builds = {'misc0':{10:['2-RC'],
                         15:['2-RC','5-AF'],
                         20:['5-RC'],
                         30:['5-RC','25-AF'],
                         40:['35-AF','5-WG'],
                         50:['45-AF','5-WG']},
             'misc1':{10:['10-RC'],
                         15:['9-RC','5-AF','1-DC'],
                         20:['20-RC'],
                         30:['5-RC','25-AF'],
                         40:['35-AF','5-WG'],
                         50:['45-AF','5-WG']},
             'depot0':{10:['1-FA','1-MA','1-SY','1-MI','2-WG','2-AF'],
                         15:['1-FA','1-MA','2-SY','2-MI','2-WG','3-AF'],
                         20:['1-FA','1-MA','3-SY','2-MI','3-WG','5-AF'],
                         30:['2-FA','5-RC','2-MA','3-SY','3-MI','10-AF'],
                         40:['2-SY','2-MI','10-RC','1-FA','1-MA','18-AF','1-SC','1-DC'],
                         50:['28-AF','6-RC','2-FA','2-MA','3-SY','3-MI']},
             'depot1':{10:['1-FA','1-MA','1-SY','1-MI','2-WG','2-AF'],
                         15:['1-FA','1-MA','2-SY','2-MI','2-WG','3-AF'],
                         20:['1-FA','1-MA','3-SY','2-MI','3-WG','5-AF'],
                         30:['2-FA','5-RC','2-MA','3-SY','3-MI','9-AF'],
                         40:['2-SY','2-MI','10-RC','1-FA','1-MA','18-AF','1-SC','1-DC'],
                         50:['25-AF','6-RC','2-FA','2-MA','3-SY','3-MI']},
             'defence0':{10:['1-RS'],
                         15:['1-RS'],
                         20:['1-RS'],
                         30:['1-RS'],
                         40:['20-MF'],
                         50:['25-MF']},
             'defence1':{10:['4-MF','1-RS','1-JS'],
                         15:['6-MF','2-RS','1-JS'],
                         20:['8-MF','2-RS','2-JS'],
                         30:['12-MF','3-RS','3-JS'],
                         40:['20-MF'],
                         50:['25-MF']},
             'alloy0':{10:['10-AF'],
                         15:['15-AF'],
                         20:['20-AF'],
                         30:['30-AF'],
                         40:['40-AF'],
                         50:['50-AF']},
             'alloy1':{10:['10-AF'],
                         15:['15-AF'],
                         20:['20-AF'],
                         30:['30-AF'],
                         40:['40-AF'],
                         50:['50-AF']},
             'energy0':{10:['10-CM'],
                         15:['15-CM'],
                         20:['20-CM'],
                         30:['30-CM'],
                         40:['40-CM'],
                         50:['50-CM']},
             'energy1':{10:['10-CM'],
                         15:['15-CM'],
                         20:['20-CM'],
                         30:['30-CM'],
                         40:['40-CM'],
                         50:['50-CM']},
             'array0':{10:['10-SS'],
                         15:['15-SS'],
                         20:['20-SS'],
                         30:['30-SS'],
                         40:['40-SS'],
                         50:['50-SS']},
             'array1':{10:['10-RS'],
                         15:['15-SS'],
                         20:['20-SS'],
                         30:['30-SS'],
                         40:['40-SS'],
                         50:['50-SS']}
             }

class AIPlayer(root.Root):
    """An AI Player runs an empire on its own"""
    def __init__(self, args):
        # Attributes
        self.id = str() # Unique Game Object ID
        self.type = str() # ai type
        self.name = str() # Name of AI
        self.tech = int() # Initial tech that AI player will add to each tech item
        self.minthreat = float() # minimum threat AI player will tolerate on border planets before they go defensive
        self.aggressiveness = float() # how aggressive the ai is for attacking
        self.defaultAttributes = ('id', 'type', 'name', 'tech')
        self.setAttributes(args)
        self.mySystemOrders = {} # key = systemID, value = system assessment and orders for round
        self.setRandomAI()
        self.topIndustry = {} # key = industry string desc, value = best industry data obj avail
        self.tempSystems = [] # used to aid in connecting systems to homeworld
        self.round = 0
        self.myEmpireID = ''
        self.myHomeworldID = ''
        self.myGalaxy = None
        self.myEmpire = None
        self.myShipDesigns = None
        self.myDroneDesigns = None
        self.clusterCount = 1       

    def setMyShipDesignsFromFile(self, path):
        """Ship Designs come from a file which has them pickled and ready for use"""
        self.myShipDesigns = storedata.loadFromFile('%s/shipdesigns.ai' % path)
        self.myShipDesigns.reverse()
        
    def setMyDroneDesignsFromFile(self, path):
        """Drone Designs come from a file which has them pickled and ready for use"""
        self.myDroneDesigns = storedata.loadFromFile('%s/dronedesigns.ai' % path)
        self.myDroneDesigns.reverse()
        
    def setRandomAI(self):
        """Retrieve and set a random AI Player from choices avaialble"""
        myAI = random.choice(ai_types)
        self.type = myAI['type']
        self.name = myAI['name']
        self.tech = myAI['tech']
        self.minthreat = myAI['minthreat']
        self.aggressiveness = myAI['aggressiveness']
    
    def setMyGalaxy(self, galaxyObject):
        """Set the Galaxy Object Owner of this AI Player"""
        self.myGalaxy = galaxyObject
        galaxyObject.AIPlayers[self.id] = self
    
    def setMyEmpire(self, empireObject):
        """Set the Empire of this AI Player"""
        self.myEmpire = empireObject
        self.myEmpireID = empireObject.id
        empireObject.myAIPlayer = self
    
    def setLog(self, message):
        """Set a log message for this AI player"""
        myInfo = 'ROUND(%d):%s:' % (self.myGalaxy.currentRound, self.name)
        #file_object = open('ai_%s.log' % self.myEmpire.name[:3], 'a')
        #file_object.write(myInfo+message+'\n')
        #file_object.close()
        
    def doMyTurn(self):
        """Do the AI round of decisions"""
        self.reset()
        self.assessSituation()
        self.updateRound()
        self.doMyTech()
        self.getClusterBuildOrders()
        self.doMySystemBuilds()
        self.updateCityFocus()
        self.depotOrders()
        self.moveFleets() # move before build so you don't move what you built
        self.buildMarines()
        self.buildShips()
        
    def moveFleets(self):
        #create a list of systems where I have ships to give them orders
        try:
            myFleetLocations = []
            for shipID, myShip in self.myGalaxy.ships.iteritems():
                if myShip.empireID == self.myEmpireID and myShip.toSystem not in myFleetLocations and myShip.fromSystem == myShip.toSystem:
                    myFleetLocations.append(myShip.toSystem)
            
            for mySystemID in myFleetLocations:
                mySystem = self.myGalaxy.systems[mySystemID]
                targetSystems = self.findTargetSystems(mySystem)
                if targetSystems <> []:
                    targetSystem = random.choice(targetSystems)
                    if targetSystem.id not in mySystem.connectedSystems:
                        # not on the border so just pick a system to get closer
                        closestSystems = self.moveCloserToTargetSystem(mySystem, targetSystem)
                        if closestSystems <> []:
                            closestSystem = random.choice(closestSystems)
                            self.warpEverythingToSystem(closestSystem)
                    else:
                        # on the border so be careful what we warp to the system
                        self.invasionAnalysis(targetSystem)
        except:
            self.setLog('general error moving ships and regiments, round:%d' % self.round)
    
    def invasionAnalysis(self, targetSystem):
        """Determine if Target System is ready for invasion"""
        targetSystemFleetStrength = 0
        targetSystemArmyStrength = 0
        myConnectedFleetStrength = 0
        myConnectedArmyStrength = 0
        
        targetSystemFleetStrength = self.calcFleetStrength(targetSystem, calcMyStrength=False)
        targetSystemArmyStrength = self.calcMarineStrength(targetSystem, calcMyStrength=False)
        
        for systemID in targetSystem.connectedSystems:
            connectedSystem = self.myGalaxy.systems[systemID]
            if (connectedSystem.myEmpireID == self.myEmpireID):
                myConnectedFleetStrength += self.calcFleetStrength(connectedSystem, calcMyStrength=True)
                myConnectedArmyStrength += self.calcMarineStrength(connectedSystem, calcMyStrength=True)
        
        if myConnectedFleetStrength > targetSystemFleetStrength and myConnectedArmyStrength > targetSystemArmyStrength:
            if self.aggressiveness >= random.random():
                self.warpEverythingToSystem(targetSystem)
    
    def warpEverythingToSystem(self, targetSystem):
        """Warp everything to the target system"""
        shipDict = {}
        regDict = {}
        for shipID, myShip in self.myGalaxy.ships.iteritems():
            if myShip.empireID == self.myEmpireID and myShip.toSystem == myShip.fromSystem and myShip.fromSystem in targetSystem.connectedSystems:
                if myShip.fromSystem not in shipDict.keys():
                    shipDict[myShip.fromSystem] = [shipID]
                else:
                    shipDict[myShip.fromSystem].append(shipID)
        
        for regID, myReg in self.myGalaxy.regiments.iteritems():
            if myReg.empireID == self.myEmpireID and myReg.toSystem == myReg.fromSystem and myReg.fromSystem in targetSystem.connectedSystems:
                if myReg.fromSystem not in regDict.keys():
                    regDict[myReg.fromSystem] = [regID]
                else:
                    regDict[myReg.fromSystem].append(regID)
        
        if shipDict <> {}:
            for fromSystemID, shipList in shipDict.iteritems():
                result = self.myGalaxy.moveShips(shipList, self.myEmpireID, targetSystem.id)
                if result == 1:
                    self.setLog('MOVED %d SHIPS to %s, round:%d' % (len(shipList), targetSystem.name, self.round))
                else:
                    self.setLog('ERROR moving ships to %s, round:%d, Error: %s' % (targetSystem.name, self.round, result))
                
        if regDict <> {}:
            for fromSystemID, regList in regDict.iteritems():
                result = self.myGalaxy.moveReg(regList, self.myEmpireID, targetSystem.id)
                if result == 1:
                    self.setLog('MOVED %d MARINES to %s, round:%d' % (len(regList), targetSystem.name, self.round))
                else:
                    self.setLog('ERROR moving marines to %s, round:%d, Error: %s' % (targetSystem.name, self.round, result))

    def findTargetSystems(self, mySystem):
        """Find a target system to move to"""
        closestSystemRange = 9999
        closestSystems = []
        for systemID, targetSystem in self.myGalaxy.systems.iteritems():
            otherEmpire = self.myGalaxy.empires[targetSystem.myEmpireID]
            if otherEmpire.id == '0' or otherEmpire.ai == 0:
                range = funcs.getTargetRange(mySystem.x, mySystem.y, targetSystem.x, targetSystem.y)
                if range == closestSystemRange:
                    closestSystems.append(targetSystem)
                elif range < closestSystemRange:
                    closestSystems = [targetSystem]
                    closestSystemRange = range
        return closestSystems                

    def moveCloserToTargetSystem(self, mySystem, targetSystem):
        """decide on a system to travel to that is on the way to the target system"""
        closestSystemRange = 9999
        closestSystems = []
        for id in mySystem.connectedSystems:
            connectedSystem = self.myGalaxy.systems[id]
            if (connectedSystem.myEmpireID == self.myEmpireID):
                range = funcs.getTargetRange(connectedSystem.x, connectedSystem.y, targetSystem.x, targetSystem.y)
                if range == closestSystemRange:
                    closestSystems.append(connectedSystem)
                elif range < closestSystemRange:
                    closestSystems = [connectedSystem]
                    closestSystemRange = range
        return closestSystems
    
    def calcFleetStrength(self, chosenSystem, calcMyStrength=True):
        strength = 0
        for shipID, myShip in self.myGalaxy.ships.iteritems():
            if myShip.toSystem == chosenSystem.id:
                if (calcMyStrength == True and myShip.empireID == self.myEmpireID) or (calcMyStrength == False and myShip.empireID <> self.myEmpireID):
                    strength += myShip.myDesign.myShipHull.mass
        return strength
    
    def calcMarineStrength(self, chosenSystem, calcMyStrength=True):
        strength = 0
        for regID, myReg in self.myGalaxy.regiments.iteritems():
            if myReg.toSystem == chosenSystem.id:
                if (calcMyStrength == True and myReg.empireID == self.myEmpireID) or (calcMyStrength == False and myReg.empireID <> self.myEmpireID):
                    strength += 1
        
        if calcMyStrength == False:
            for dataID, amount in chosenSystem.myIndustry.iteritems():
                myIndustryData = self.myGalaxy.industrydata[dataID]
                if myIndustryData.abr[1:] == 'MF':
                    strength += (myIndustryData.output * amount)
        
        return strength

    def buildShips(self):
        if self.round > 6:
            for systemID, mySystem in self.myGalaxy.systems.iteritems():
                if mySystem.myEmpireID == self.myEmpireID and self.myEmpire.CR > 200000:
                    result = 1
                    while result == 1:
                        s = random.choice(self.getValidDesignsToBuild())
                        dOrder = {'type':'Add Ship', 'value':'1-%s' % s,
                                  'system':systemID, 'round':self.round}
                        result = self.myEmpire.genIndustryOrder(dOrder)
                        if result == 1:
                            self.setLog('BUILDSHIP: name:%s, round:%d' % (mySystem.name, self.round))
    
    def getValidDesignsToBuild(self):
        designs = []
        for designID, myShipDesign in self.myEmpire.shipDesigns.iteritems():
            myShipDesign.setMyStatus()
            if myShipDesign.hasAllTech == 1 and myShipDesign.id in ['2','3','4','6','7','8','17','18','19']:
                designs.append(myShipDesign.id)
        return designs
                
    def buildMarines(self):
        if self.round > 6 and self.myEmpire.CR > 200000:
            for systemID, mySystem in self.myGalaxy.systems.iteritems():
                if mySystem.myEmpireID == self.myEmpireID and self.myEmpire.CR > 200000:
                    result = 1
                    while result == 1:
                        s = random.choice(['10','7','4'])
                        dOrder = {'type':'Add Regiment', 'value':'1-%s' % s,
                                  'system':systemID, 'round':self.round}
                        result = self.myEmpire.genIndustryOrder(dOrder)
                        if result == 1:
                            self.setLog('BUILDMARINE: name:%s, round:%d' % (mySystem.name, self.round))

    def reset(self):
        """Reset AI assessments from last round"""
        self.resetMySystems()
        self.setMyHomeworld()
        self.setHomeworldPaths()
        self.resetTopIndustry()
    
    def setMyHomeworld(self):
        """The AI Empire always needs a homeworld, set it if there is none"""
        if self.myHomeworldID == '' or self.myGalaxy.systems[self.myHomeworldID].myEmpireID != self.myEmpireID:
            max = 0
            for systemID, mySystem in self.myGalaxy.systems.iteritems():
                if mySystem.myEmpireID == self.myEmpireID and mySystem.cities > max:
                    max = mySystem.cities
                    self.myHomeworldID = mySystem.id
        
    def resetMySystems(self):
        """Reset dict of my current systems under control, key = system id, value = dict"""
        self.mySystemOrders = {}
        for systemID, mySystem in self.myGalaxy.systems.iteritems():
            if mySystem.myEmpireID == self.myEmpireID:
                if systemID in self.mySystemOrders.keys():
                    self.mySystemOrders[systemID]['tobuild']=''
                    self.mySystemOrders[systemID]['threat']=0.0
                    self.mySystemOrders[systemID]['myValue']=1.0
                    self.mySystemOrders[systemID]['CRwanted']=0.0
                    self.mySystemOrders[systemID]['ALwanted']=0.0
                    self.mySystemOrders[systemID]['ECwanted']=0.0
                    self.mySystemOrders[systemID]['IAwanted']=0.0
                    self.mySystemOrders[systemID]['stepsToHomeworld']=999
                    self.mySystemOrders[systemID]['closestID']=systemID
                    self.mySystemOrders[systemID]['cluster']=0
                    self.mySystemOrders[systemID]['myDepot']=''
                else:
                    self.mySystemOrders[systemID] = {'threat':0.0,
                                                     'myValue':1.0,
                                                     'CRwanted':0.0,
                                                     'ALwanted':0.0,
                                                     'ECwanted':0.0,
                                                     'IAwanted':0.0,
                                                     'stepsToHomeworld':999,
                                                     'closestID':systemID,
                                                     'tobuild':'',
                                                     'cluster':0,
                                                     'myDepot':''}
    
    def setHomeworldPaths(self):
        """Each System needs to analyse how far it is from homeworld and which other system is the right
        direction for ships or resources to move towards the homeworld if that is needed"""
        myHomeworld = self.myGalaxy.systems[self.myHomeworldID]
        self.setMyChildPaths(myHomeworld.id, 0, '')
        
    def setMyChildPaths(self, mySystemID, distance, closestID):
        mySystem = self.myGalaxy.systems[mySystemID]
        homeSystem = self.myGalaxy.systems[self.myHomeworldID]
        if mySystemID != self.myHomeworldID:
            self.mySystemOrders[mySystemID]['stepsToHomeworld'] = distance
            self.mySystemOrders[mySystemID]['closestID'] = closestID
            ##mySystem.name = 'ID:%s-CL:%s-D:%d' % (mySystemID,closestID,distance)##
        for id in self.myGalaxy.systems[mySystemID].connectedSystems:
            childSystem = self.myGalaxy.systems[id]
            if (childSystem.myEmpireID == self.myEmpireID and 
                closestID not in childSystem.connectedSystems and
                id != closestID and self.mySystemOrders[id]['stepsToHomeworld'] == 999):
                if funcs.getTargetRange(childSystem.x, childSystem.y, homeSystem.x, homeSystem.y) > funcs.getTargetRange(mySystem.x, mySystem.y, homeSystem.x, homeSystem.y):
                    self.setMyChildPaths(id, distance+1, mySystemID)
    
    def resetTopIndustry(self):
        """Reset the dict of topIndustry to see what is available to build based on current tech"""
        self.topIndustry = {}
        for dataID in funcs.sortStringList(self.myGalaxy.industrydata.keys()):
            myIndustryData = self.myGalaxy.industrydata[dataID]
            if self.myEmpire.techTree[myIndustryData.techReq].complete == 1: 
                id = myIndustryData.abr[1:]
                self.topIndustry[id] = myIndustryData
            
    def assessSituation(self):
        """Scan the system with all legal means and fill up information for later decisions"""
        # system - threat level, build for research, build for defence, build for economy, build marine depot, build ship depot
        for systemID, orderDict in self.mySystemOrders.iteritems():
            mySystem = self.myGalaxy.systems[systemID]
            if self.myHomeworldID in mySystem.connectedSystems:
                self.setToBuildCluster(orderDict)
            else:
                orderDict['threat'] = self.getThreatLevel(mySystem)
                if orderDict['threat'] > self.minthreat:
                    orderDict['tobuild'] = 'defence'
                else:
                    orderDict['tobuild'] = ''
        self.setToBuildCluster(self.mySystemOrders[self.myHomeworldID])
        self.clusterScan()
    
    def setToBuildCluster(self, orderDict):
        """Set the orderDict to the latest cluster number"""
        orderDict['tobuild'] = 'cluster-%d' % self.clusterCount
        orderDict['cluster'] = self.clusterCount
        
    def clusterScan(self):
        """Continually scan systems into clusters and border planets"""
        while self.doAllSystemsHaveOrders() == 0:
            dClusterCenters = self.getClusterCenters()
            if dClusterCenters != {}:
                lSortedCenters = funcs.sortDictByValue(dClusterCenters, True)
                chosenCenter = lSortedCenters[0]
            else:
                return
            self.setupNewCluster(chosenCenter)
    
    def doAllSystemsHaveOrders(self):
        """Do all AI controlled systems have an assignment, ie cluster-x, defence, etc"""
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if orderDict['tobuild'] == '':
                return 0
        return 1
    
    def getClusterCenters(self):
        """return a list of systems that have at least 3 connections to systems that have no build order yet"""
        systems = []
        centers = {}
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if orderDict['tobuild'] == '':
                systems.append(systemID)
        for systemID in systems:
            mySystem = self.myGalaxy.systems[systemID]
            connections = self.getFreeConnections(mySystem)
            if connections > 2:
                centers[systemID] = connections
        return centers
    
    def getFreeConnections(self, mySystem):
        """Return number of free connections for system to systems that have no orders yet"""
        count = 0
        for otherSystemID in mySystem.connectedSystems:
            if otherSystemID in self.mySystemOrders.keys():
                if self.mySystemOrders[otherSystemID]['tobuild'] == '':
                    count += 1
        return count
    
    def getClosestToHomeworld(self, newClusterCenters):
        """Go through list of new Cluster System hopefuls and choose the closest one to Homeworld"""
        closestID = ''
        closestRange = 99999.999
        myHomeworld = self.myGalaxy.systems[self.myHomeworldID]
        for systemID in newClusterCenters:
            mySystem = self.myGalaxy.systems[systemID]
            range = funcs.getTargetRange(mySystem.x, mySystem.y, myHomeworld.x, myHomeworld.y)
            if range < closestRange:
                closestRange = range
                closestID = systemID
        return systemID
    
    def setupNewCluster(self, centerID):
        """Setup a new cluster based on the cluster center that was chosen"""
        self.clusterCount += 1
        tobuild = 'cluster-%d' % self.clusterCount
        myCenterSystem = self.myGalaxy.systems[centerID]
        self.setToBuildCluster(self.mySystemOrders[centerID])
        for systemID in myCenterSystem.connectedSystems:
            if systemID in self.mySystemOrders.keys():
                if self.mySystemOrders[systemID]['tobuild'] == '':
                    self.setToBuildCluster(self.mySystemOrders[systemID])
    
    def getThreatLevel(self, mySystem):
        """Scan the border planets and determine threat level 0 - 1.0"""
        threat = 0.0
        for systemID in mySystem.connectedSystems:
            borderSystem = self.myGalaxy.systems[systemID]
            if borderSystem.myEmpireID != mySystem.myEmpireID:
                if borderSystem.myEmpireID == '0':
                    threat += 0.01
                elif self.myGalaxy.empires[borderSystem.myEmpireID].diplomacy.diplomacyID <= 3:
                    threat += 0.3
                    ##TODO: scan for ships and troops?  add to threat
        return threat
            
    def updateRound(self):
        self.round = self.myGalaxy.currentRound
        
    def doMyTech(self):
        """An AI will research technology each round"""
        myTechs = self.getAvailTechToResearch()
        random.shuffle(myTechs)
        while self.myEmpire.rpAvail != 0:
            for myTech in myTechs:
                self.researchTech(myTech)
            if self.allTechResearched(myTechs) == 1:
                return
    
    def allTechResearched(self, myTechs):
        """If all current tech is set to max research then end tech researching"""
        for myTech in myTechs:
            id = '%s-%d' % (myTech.id, self.round)
            if id in self.myEmpire.techOrders.keys():
                remain = myTech.requiredPoints - eval(self.myEmpire.techOrders[id].value) - myTech.currentPoints
            else:
                remain = myTech.requiredPoints
            if remain > 0:
                return 0
        return 1
                
    def getAvailTechToResearch(self):
        """Return a list of technology that is available to research this round"""
        myTechs = []
        for id, myTech in self.myEmpire.techTree.iteritems():
            if myTech.complete == 0:
                avail = 1
                for preTechID in myTech.preTechs:
                    preTech = self.myEmpire.techTree[preTechID]
                    if preTech.complete == 0:
                        avail = 0
                if avail == 1:
                    myTechs.append(myTech)
        return myTechs
        
    def researchTech(self, myTech):
        """Actually try to research the technology chosen by the default amount specified by this AI type"""
        amount = self.getResearchAmount(myTech)
        if amount > 0:
            self.setLog('TECH: type:%s, value:%d, round:%d' % (myTech.id, amount, self.round))
            self.myEmpire.genTechOrder({'type':myTech.id, 'value':amount, 'round':self.round})
    
    def getResearchAmount(self, myTech):
        """How much can the AI actually research at this moment"""
        tech = 0
        if self.myEmpire.rpAvail < self.tech:
            tech = self.myEmpire.rpAvail
        else:
            tech = self.tech
        if myTech.requiredPoints - myTech.currentPoints < tech:
            return myTech.requiredPoints - myTech.currentPoints
        return tech

    def isDesignValidToResearch(self, myDesign):
        """This check is for carrier designs which depend on drone designs being researched first"""
        for key, value in myDesign[3].iteritems():
            if 'dronedesign' in value.keys():
                if value['dronedesign'] not in self.myEmpire.droneDesigns.keys():
                    return 0
        return 1
                
    def doMyDroneDesign(self):
        """Research a Drone Design instead, because the ship design requires it most likely"""
        myDroneDesign = self.myDroneDesigns.pop()
        self.setLog('DRONEDESIGN: name:%s, round:%d' % (myDroneDesign[0], self.round))
        self.myEmpire.genDroneDesign(myDroneDesign[0],myDroneDesign[1],myDroneDesign[2],myDroneDesign[3])

    def getClusterBuildOrders(self):
        """Multiple Planet Clusters identified have to be given orders as to what each planet should build
        to support the cluster"""
        clusters = {}
        for i in range(1,100):
            clusters[i] = []
        for systemID, orderDict in self.mySystemOrders.iteritems():
            mySystem = self.myGalaxy.systems[systemID]
            if 'cluster' in orderDict['tobuild']:
                (clusterName, clusterID) = string.split(orderDict['tobuild'], '-')
                clusters[int(clusterID)].append(systemID)
        for clusterID, systemIDList in clusters.iteritems():
            if systemIDList != []:
                self.setMyClusterBuildOrder(systemIDList)
            
    def setMyClusterBuildOrder(self, systemIDList):
        """This List of Systems is in a cluster, figure out what
        each planet should be building within that cluster"""
        (lConnect, lCities) = self.sortCluster(systemIDList)
        if self.myHomeworldID in lConnect:
            depotID = self.myHomeworldID
        else:
            depotID = lConnect[0]
        self.mySystemOrders[depotID]['tobuild'] = 'depot'
        lCities.remove(depotID)
        assignOrder = ['energy','array','alloy','energy','array','misc','alloy','misc']
        count = 0
        for systemID in lCities:
            self.mySystemOrders[systemID]['tobuild'] = assignOrder[count]
            self.mySystemOrders[systemID]['myDepot'] = depotID
            count += 1
                
    def sortCluster(self, systemIDList):
        """take list of systems and return a dict = {planetid:num connections, ...} 
        and list [planet ID with most connections, ....]"""
        dConnect = {}
        lConnect = []
        dCities = {}
        lCities = {}
        for systemID in systemIDList:
            count1 = 0
            mySystem = self.myGalaxy.systems[systemID]
            for connectID in mySystem.connectedSystems:
                if connectID in systemIDList:
                    count1 += 1
            dConnect[systemID] = count1
            dCities[systemID] = mySystem.cities
        lConnect = funcs.sortDictByValue(dConnect, True)
        lCities = funcs.sortDictByValue(dCities, True)
        return (lConnect,lCities)

    def doMySystemBuilds(self):
        """Every system needs to go through its system build orders based on earlier assessments"""
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if orderDict['tobuild'] != '':
                mySystem = self.myGalaxy.systems[systemID]
                self.removeAllIndustry(mySystem)
                ##mySystem.name = '%s-%d' % (orderDict['tobuild'], orderDict['cluster'])## DEBUG
                self.buildNewIndustry(mySystem, orderDict['tobuild'])
                self.setupGenTradeRoute(mySystem)
                
    def setupGenTradeRoute(self, mySystem):
        """Any System that was setup needs to assess if it should send its resources to its cluster depot center"""
        if self.mySystemOrders[mySystem.id]['tobuild'] == 'depot':
            return
        else:
            for systemID, orderDict in self.mySystemOrders.iteritems():
                if (orderDict['cluster'] == self.mySystemOrders[mySystem.id]['cluster'] and
                    orderDict['tobuild'] == 'depot'):
                    self.addGenTradeRoute(mySystem.id, systemID)
                    return
    
    def updateCityFocus(self):
        """City focus should change if system builds have changed"""
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if orderDict['tobuild'] != '':
                mySystem = self.myGalaxy.systems[systemID]
                if 'energy' in orderDict['tobuild']:
                    self.changeCityIndustry(systemID, [0, mySystem.cities, 0])
                elif 'array' in orderDict['tobuild']:
                    self.changeCityIndustry(systemID, [0, 0, mySystem.cities])
                else:
                    self.changeCityIndustry(systemID, [mySystem.cities, 0, 0])
    
    def removeAllIndustry(self, mySystem):
        """System will remove all industry in preparation for changing system industry focus"""
        result1 = 'error'
        result2 = 'error'
        result3 = 'error'
        for dataID, number in mySystem.myIndustry.iteritems():
            myOldIndustryData = self.myGalaxy.industrydata[dataID]
            if number > 0:
                result1 = mySystem.validateRemoveIndustry(self.myEmpireID, number, myOldIndustryData.id)
                if result1 == 1:
                    result2 = mySystem.removeIndustry(number, myOldIndustryData.id)
                    if result2 == 1:
                        result3 = mySystem.refundForRemoveIndustry(number, myOldIndustryData.id)
                self.setLog('REMOVE %s from %s <%s,%s,%s>' % (myOldIndustryData.name, mySystem.name, result1, result2, result3))
                
    def changeCityIndustry(self, systemID, newIndustryList):
        """change city industry focus list=[AL,EC,IA]"""
        result1 = 'error'
        result2 = 'error'
        mySystem = self.myGalaxy.systems[systemID]
        result1 = mySystem.validateUpdateCityIndustry(self.myEmpireID, newIndustryList)
        if result1 == 1:
            result2 = mySystem.updateCityIndustry(newIndustryList)
        self.setLog('UPDATE %s CITY FOCUS to %s <%s,%s>' % (mySystem.name, newIndustryList, result1, result2))
                
    def buildNewIndustry(self, mySystem, order):
        """System has been given orders to build or upgrade industry of order = depot for example which breaks down to a list of facilities"""
        result1 = 'error'
        result2 = 'error'
        result3 = 'error'
        order = self.getOrderBasedOnTech(order)
        buildList = ai_builds[order][mySystem.cities]
        for buildOrder in buildList:
            (num, type) = string.split(buildOrder, '-')
            num = int(num)
            try:
                myIndustryData = self.topIndustry[type]
            except:
                return
            space = mySystem.cities - mySystem.citiesUsed
            if space == 0:
                return
            for i in range(0,num):
                if mySystem.checkResources(myIndustryData.costCR,myIndustryData.costAL,myIndustryData.costEC,myIndustryData.costIA) == 1:
                    result1 = mySystem.validateAddIndustry(self.myEmpireID, 1, myIndustryData.id)
                    if result1 == 1:
                        result2 = mySystem.payForAddIndustry(1, myIndustryData.id)
                        if result2 == 1:
                            result3 = mySystem.addIndustry(1, myIndustryData.id)
                    self.setLog('ADD %s to %s <%s,%s,%s>' % (myIndustryData.name, mySystem.name, result1, result2, result3))
                else:
                    self.mySystemOrders[mySystem.id]['CRwanted'] += myIndustryData.costCR
                    self.mySystemOrders[mySystem.id]['ALwanted'] += myIndustryData.costAL
                    self.mySystemOrders[mySystem.id]['ECwanted'] += myIndustryData.costEC
                    self.mySystemOrders[mySystem.id]['IAwanted'] += myIndustryData.costIA
    
    def getOrderBasedOnTech(self, order):
        """Cycle through current researched technology to decide which order dict to use"""
        count = 0
        for techList in ai_builds_techreq[order]:
            valid = 1
            for techID in techList:
                myTech = self.myEmpire.techTree[techID]
                if myTech.complete == 0:
                    valid = 0
            if valid == 0:
                return '%s%d' % (order, count-1)
            count += 1
        return '%s%d' % (order, count-1)
    
    def addGenTradeRoute(self, fromSystemID, toSystemID):
        """Setup a GEN trade route from one system to another"""
        result1 = 'error'
        id = '%s-%s-GEN' % (fromSystemID, toSystemID)
        if id in self.myGalaxy.tradeRoutes.keys():
            return
        tradeRouteDict = {'AL':0,'EC':0,'IA':0,'fromSystem':fromSystemID,
                          'toSystem':toSystemID, 'id':id,
                          'oneTime':0, 'type':'GEN'}
        result1 = self.myGalaxy.genTradeRoute(tradeRouteDict)
        self.setLog('ADD GEN TRADE ROUTE %s-%s <%s>' % (fromSystemID, toSystemID, result1))
    
    def depotOrders(self):
        """Each depot system has has special tasks to perform"""
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if 'depot' in orderDict['tobuild']:
                self.depotGiveResForIndustry(systemID)
    
    def depotGiveResForIndustry(self, depotID):
        """Depot System should distribute its resources to its systems in need for industry building"""
        for systemID, orderDict in self.mySystemOrders.iteritems():
            if orderDict['myDepot'] == depotID:
                self.addREGTradeRoute(depotID, systemID, orderDict['ALwanted'],
                                      orderDict['ECwanted'],orderDict['IAwanted'])

    def addREGTradeRoute(self, fromSystemID, toSystemID, AL, EC, IA):
        """Setup a REG trade route from one system to another"""
        if (AL == 0 and EC == 0 and IA == 0):
            return
        result1 = 'error'
        id = '%s-%s-REG' % (fromSystemID, toSystemID)
        if id in self.myGalaxy.tradeRoutes.keys():
            return
        tradeRouteDict = {'AL':AL,'EC':EC,'IA':IA,'fromSystem':fromSystemID,
                          'toSystem':toSystemID, 'id':id,
                          'oneTime':1, 'type':'REG'}
        result1 = self.myGalaxy.genTradeRoute(tradeRouteDict)
        self.setLog('ADD REG TRADE ROUTE %s-%s AL=%d EC=%d IA=%d <%s>' % (fromSystemID, toSystemID, AL, EC, IA, result1))
    