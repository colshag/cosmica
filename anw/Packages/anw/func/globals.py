# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# globals.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# Store Global Variables
# ---------------------------------------------------------------------------
try:
    from panda3d.core import Vec4
except:
    pass
currentVersion = '0.16.0'
currentVersionShort = 'master'
currentVersionTag = '.20190119'
serverMode = 0

maxShipsPerBattle = 120

try:
    colors = {'yellow':Vec4(0.922,0.910,0.047,1),
          'orange':Vec4(0.996, 0.359, 0, 1),
          'green':Vec4(0.242, 0.973, 0.309, 1),
          'cyan':Vec4(0, 0.758, 0.883, 1),
          'red':Vec4(0.93, 0.08, 0.08, 1),
          'pink':Vec4(0.99, 0.61, 0.688, 1),
          'white':Vec4(0.99, 0.961, 0.969, 1),
          'ltpurple':Vec4(0.93, 0.563, 0.977, 1),
          'blue':Vec4(0.223, 0.6445, 0.95, 1),
          'brown':Vec4(0.7059, 0.396, 0.192, 1),
          
          'blood':Vec4(0.6, 0, 0, 1),
          'dkgrey':Vec4(0.234, 0.234, 0.234, 1),
          'dkpurple':Vec4(110, 4, 122, 1),
          'dkblue':Vec4(0.43, 0.05, 0.531, 1),
          'black':Vec4(0.04, 0.04, 0.04, 1),
          'dkyellow':Vec4(0.6, 0.6, 0, 1),
          'dkgreen':Vec4(0,0.6,0,1),
          
          'guiblue1':Vec4(0,0.4,0.91,1),
          'guiblue2':Vec4(0,0.255,0.58,1),
          'guiblue3':Vec4(0,0.114,0.255,1),
          'guiblue4':Vec4(0,0.02,0.1,1),
          'guigrey':Vec4(0.549,0.549,0.549,1),
          'guiyellow':Vec4(0.922,0.910,0.047,1),
          'guired':Vec4(1,0,0,1),
          'guigreen':Vec4(0,1,0,1),
          'guiblack':Vec4(0,0,0,1),
          'guiwhite':Vec4(1,1,1,1),
          
          'mod0':Vec4(0.6,0.8,0.9,1),
          'mod1':Vec4(0.8,0.8,0,1),
          'mod2':Vec4(1,0.5,0.2,1),
          'mod3':Vec4(0.5,0.6,0.6,1),
          'mod4':Vec4(0.8,0,1,1),
          'mod5':Vec4(0.6,0.8,0.1,1),
          'mod6':Vec4(1,0.5,0.5,1),
          'mod7':Vec4(0,0.8,0.9,1),
          'mod8':Vec4(0.4,0.2,0,1)
          }
except:
    colors = {}

empires = [{'id':'0', 'name':'Neutral', 'color1':'white', 'color2':'black','CR':0, 'ai':1},
           {'id':'1', 'name':'Yellow Empire', 'color1':'yellow', 'color2':'black','CR':0},
           {'id':'2', 'name':'Brown Empire', 'color1':'brown', 'color2':'black','CR':0},
           {'id':'3', 'name':'Green Empire', 'color1':'green', 'color2':'black','CR':0},
           {'id':'4', 'name':'Blue Empire', 'color1':'blue', 'color2':'black','CR':0},
           {'id':'5', 'name':'Pink Empire', 'color1':'pink', 'color2':'dkpurple','CR':0},
           {'id':'6', 'name':'Red Empire', 'color1':'red', 'color2':'black','CR':0},
           {'id':'7', 'name':'Cyan Empire', 'color1':'cyan', 'color2':'black','CR':0},
           {'id':'8', 'name':'Fire Empire', 'color1':'yellow', 'color2':'blood','CR':0},]


initialLogin = True
isTutorial = False
tutorialStep = 0
tutorialStepComplete = False
tutorialTotalSteps = 30
tutorialGoBackDisabled = True

marinesPerTransport = 10

alternateTargetRadius = 4

# simulator interval value
intervalValue = 0.02

resourceNames = ['AL','EC','IA']
resourceColors = {'CR':'guigreen', 'AL':'guiblue1', 'EC':'guiyellow', 'IA':'guired'}
# amount of resources required to add one city to a system
addCityResource = {'CR':5000.0, 'AL':1000.0, 'EC':250.0, 'IA':100.0}

# amount to modify the resource focus of one city
updateCityResource = {'CR':500.0, 'AL':0.0, 'EC':0.0, 'IA':0.0}

# amount of resources one city will generate without bonuses
cityCRGen = 200.0
cityALGen = 20.0
cityECGen = 10.0
cityIAGen = 5.0

# default value of resources in credits [AL,EC,IA]
resourceCreditValue = [20.0,40.0,80.0]

AL = resourceCreditValue[0]/2
EC = resourceCreditValue[1]/2
IA = resourceCreditValue[2]/2

systemSize = 6
techSize = 3

# armor modifiers
reflectiveArmorModifier = 0.5
impactArmorModifier = 0.5

# quadrants
quadAngles = {'fore':0.0, 'star':90.0, 'aft':180.0, 'port':270.0}
angleQuads = {0.0:'fore', 270.0:'port', 180.0:'aft', 90.0:'star'}

# components
weaponComponent = '64'

# max movement
maxAccel = 5.0
maxRotation = 60.0
droneAccel = 5.0
droneRotation = 60.0

targetPreference = {'INT':['ECA','HCA','BCA'],
                    'COR':['LAS','HAS','BAS'],
                    'FRG':['ECA','HCA','BCA'],
                    'BFR':['LAS','HAS','BAS'],
                    'HCU':['ECA','HCA','BCA'],
                    'BCU':['LAS','HAS','BAS']
                    }

targetPrefDisplay = {'INT':'drone carriers',
                    'COR':'assault ships',
                    'FRG':'drone carriers',
                    'BFR':'assault ships',
                    'HCU':'drone carriers',
                    'BCU':'assault ships'
                    } 

# hardpoints
hardPoints = {'SCT':{'fore-1':[0,8],
                     'aft-1':[180,7],
                     'port-1':[225,7],
                     'star-1':[135,7]
                     },
              'INT':{'fore-1':[0,8],
                     'aft-1':[180,8],
                     'port-1':[270,8],
                     'star-1':[90,8]
                     },
              'COR':{'fore-1':[30,4],'fore-2':[330,4],
                     'aft-1':[150,4],'aft-2':[210,4],
                     'port-1':[120,16],'port-2':[120,12],
                     'star-1':[240,16],'star-2':[240,12]
                     },
              'HCO':{'fore-1':[30,4],'fore-2':[330,4],
                     'aft-1':[150,4],'aft-2':[210,4],
                     'port-1':[120,16],'port-2':[120,12],
                     'star-1':[240,16],'star-2':[240,12]
                     },
              'FRG':{'fore-1':[0,30],'aft-1':[225,8],'port-1':[340,12],'star-1':[20,12],
                     'fore-2':[10,30],'aft-2':[135,8],'port-2':[330,4],'star-2':[30,4],
                     'fore-3':[350,30],'aft-3':[180,8],'port-3':[225,26],'star-3':[135,26]
                     },
              'BFR':{'fore-1':[0,35],'aft-1':[225,8],'port-1':[335,18],'star-1':[25,18],
                     'fore-2':[10,35],'aft-2':[135,8],'port-2':[330,10],'star-2':[30,10],
                     'fore-3':[350,35],'aft-3':[180,8],'port-3':[225,30],'star-3':[135,30]
                     },
              'DST':{'fore-1':[5,46],'aft-1':[180,20],'port-1':[337,20],'star-1':[23,20],
                     'fore-2':[355,46],'aft-2':[200,20],'port-2':[330,14],'star-2':[30,14],
                     'fore-3':[13,46],'aft-3':[220,20],'port-3':[315,4],'star-3':[45,4],
                     'fore-4':[347,46],'aft-4':[180,30],'port-4':[225,30],'star-4':[135,30]
                     },
              'CRU':{'fore-1':[5,50],'aft-1':[180,40],'port-1':[260,40],'star-1':[100,40],
                     'fore-2':[355,50],'aft-2':[200,30],'port-2':[250,42],'star-2':[110,42],
                     'fore-3':[13,45],'aft-3':[220,30],'port-3':[235,44],'star-3':[125,44],
                     'fore-4':[347,45],'aft-4':[180,10],'port-4':[260,18],'star-4':[100,18]
                     },
              'HCU':{'fore-1':[7,50],'aft-1':[180,40],'port-1':[260,40],'star-1':[100,40],
                     'fore-2':[353,50],'aft-2':[200,30],'port-2':[250,42],'star-2':[110,42],
                     'fore-3':[16,45],'aft-3':[220,30],'port-3':[235,44],'star-3':[125,44],
                     'fore-4':[346,45],'aft-4':[200,40],'port-4':[255,18],'star-4':[105,18],
                     'fore-5':[0,50],'aft-5':[220,40],'port-5':[270,16],'star-5':[90,16]
                     },
              'BCU':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16]
                     },
              'DRN':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16],
                     'fore-6':[0,16],'aft-6':[180,16],'port-6':[270,16],'star-6':[90,16]
                     },
              'SDN':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16],
                     'fore-6':[0,16],'aft-6':[180,16],'port-6':[270,16],'star-6':[90,16],
                     'fore-7':[0,16],'aft-7':[180,16],'port-7':[270,16],'star-7':[90,16]
                     },
              'ECA':{'fore-1':[10,15],'aft-1':[170,15],'port-1':[320,25],'star-1':[40,25],
                     'fore-2':[350,15],'aft-2':[190,15],'port-2':[260,20],'star-2':[260,20],
                     'fore-3':[0,15],'aft-3':[180,15],'port-3':[210,25],'star-3':[150,25]
                     },
              'HCA':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16]
                     },
              'BCA':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16]
                     },
              'LAS':{'fore-1':[10,15],'aft-1':[170,15],'port-1':[320,25],'star-1':[40,25],
                     'fore-2':[350,15],'aft-2':[190,15],'port-2':[260,20],'star-2':[260,20],
                     'fore-3':[0,15],'aft-3':[180,15],'port-3':[210,25],'star-3':[150,25]
                     },
              'HAS':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16]
                     },
              'BAS':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16]
                     },
              'LWP':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16]
                     },
              'HWP':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16],
                     'fore-6':[0,16],'aft-6':[180,16],'port-6':[270,16],'star-6':[90,16],
                     'fore-7':[0,16],'aft-7':[180,16],'port-7':[270,16],'star-7':[90,16]
                     },
              'BWP':{'fore-1':[0,16],'aft-1':[180,16],'port-1':[270,16],'star-1':[90,16],
                     'fore-2':[0,16],'aft-2':[180,16],'port-2':[270,16],'star-2':[90,16],
                     'fore-3':[0,16],'aft-3':[180,16],'port-3':[270,16],'star-3':[90,16],
                     'fore-4':[0,16],'aft-4':[180,16],'port-4':[270,16],'star-4':[90,16],
                     'fore-5':[0,16],'aft-5':[180,16],'port-5':[270,16],'star-5':[90,16],
                     'fore-6':[0,16],'aft-6':[180,16],'port-6':[270,16],'star-6':[90,16],
                     'fore-7':[0,16],'aft-7':[180,16],'port-7':[270,16],'star-7':[90,16],
                     'fore-8':[0,16],'aft-8':[180,16],'port-8':[270,16],'star-8':[90,16],
                     'fore-9':[0,16],'aft-9':[180,16],'port-9':[270,16],'star-9':[90,16]
                     }
              }
              
# limitations
componentLimitations = {'warship':['SES','PES','UES'],
                        'drone':['SMP','PMP','UMP','SJD','PJD','UJD','SES','PES','UES',
                                 'SSE','PSE','USE','SRT','PRT','URT','SRX','PRX','URX','CSE','CRT'],
                        'platform':['CSE','CRT'],
                        'carrier':['LNTA','MNTA','HNTA','LFTA','MFTA','HFTA','LPTA',
                                   'MPTA','HPTA','LGGA','MGGA','HGGA','LACA','MACA',
                                   'HACA','LRGA','MRGA','HRGA','LNMA','MNMA','HNMA',
                                   'LFMA','MFMA','HFMA','LPMA','MPMA','HPMA','SES','PES','UES','CSE','CRT'],
                        'assault':['LNTA','MNTA','HNTA','LFTA','MFTA','HFTA','LPTA',
                                     'MPTA','HPTA','LGGA','MGGA','HGGA','LACA','MACA',
                                     'HACA','LRGA','MRGA','HRGA','LNMA','MNMA','HNMA',
                                     'LFMA','MFMA','HFMA','LPMA','MPMA','HPMA',
                                     'SES','PES','UES','CSE','CRT']}

weaponLimitations = {'warship':['LNL','MNL','HNL','LFL','MFL','HFL','LPL','MPL','HPL'],
                     'drone':['LNL','MNL','HNL','LFL','MFL','HFL','LPL','MPL','HPL',
                              'APG','AFC','APC','AGG','AAC','ARG'],
                     'platform':[],
                     'carrier':['LPG','MPG','HPG','LFC','MFC','HFC','LPC','MPC','HPC',
                                'LNT','MNT','HNT','LFT','MFT','HFT','LPT','MPT','HPT',
                                'LGG','MGG','HGG','LAC','MAC','HAC','LRG','MRG','HRG',
                                'LNM','MNM','HNM','LFM','MFM','HFM','LPM','MPM','HPM'],
                     'assault':['LNL','MNL','HNL','LFL','MFL','HFL','LPL','MPL','HPL',
                                  'LPG','MPG','HPG','LFC','MFC','HFC','LPC','MPC','HPC',
                                  'LNT','MNT','HNT','LFT','MFT','HFT','LPT','MPT','HPT',
                                  'LGG','MGG','HGG','LAC','MAC','HAC','LRG','MRG','HRG',
                                  'LNM','MNM','HNM','LFM','MFM','HFM','LPM','MPM','HPM']}

# fleet Ranks
shipRank0 = 'Rookie'
shipRank1 = 'Cadet'
shipRank2 = 'Ensign'
shipRank3 = 'Lieutenant'
shipRank4 = 'Captain'
shipRank5 = 'Commander'
shipRank6 = 'Admiral'
shipRank7 = 'Legendary'

# army Ranks
armyRank0 = 'Green'
armyRank1 = 'Trained'
armyRank2 = 'Veteran'
armyRank3 = 'Elite'
armyRank4 = 'Legend'

# any existing modifiers from targeting computers)
rankMods = {shipRank0:{'weaptarget':200,'retarget':400,'toHit':50,'kWtoSPfactor':0.3,'targetLock':0,'missileSpeed':0.8,'droneDodge':20},
            shipRank1:{'weaptarget':150,'retarget':360,'toHit':60,'kWtoSPfactor':0.6,'targetLock':0,'missileSpeed':1.1,'droneDodge':30},
            shipRank2:{'weaptarget':50,'retarget':320,'toHit':70,'kWtoSPfactor':0.7,'targetLock':0,'missileSpeed':1.2,'droneDodge':40},
            shipRank3:{'weaptarget':40,'retarget':280,'toHit':80,'kWtoSPfactor':0.8,'targetLock':10,'missileSpeed':1.3,'droneDodge':50},
            shipRank4:{'weaptarget':30,'retarget':240,'toHit':90,'kWtoSPfactor':0.9,'targetLock':20,'missileSpeed':1.4,'droneDodge':60},
            shipRank5:{'weaptarget':20,'retarget':200,'toHit':100,'kWtoSPfactor':1.0,'targetLock':30,'missileSpeed':1.5,'droneDodge':70},
            shipRank6:{'weaptarget':10,'retarget':160,'toHit':100,'kWtoSPfactor':1.0,'targetLock':50,'missileSpeed':2.0,'droneDodge':80},
            shipRank7:{'weaptarget':5,'retarget':120,'toHit':100,'kWtoSPfactor':2.0,'targetLock':70,'missileSpeed':3.0,'droneDodge':90},
            
            armyRank0:{'bonus':0},
            armyRank1:{'bonus':100},
            armyRank2:{'bonus':400},
            armyRank3:{'bonus':800},
            armyRank4:{'bonus':1200}
            }

# kW to shield point conversion factor: 0.5 means 1kW makes 0.5SP
# targetLock: percentage improvment to target lock time (applies to all ship weapons and stacks on

# map quadrant information
battlemapQuadrants = {}
battlemapQuadSize = 200.0/3.0
midQuadDistance = battlemapQuadSize/2
i = 1
for y in range(0,3):
    for x in range(0,3):
        battlemapQuadrants[i] = (midQuadDistance-100+battlemapQuadSize*x, midQuadDistance-100+battlemapQuadSize*y)
        i += 1

regimentCombinedBonus = 100
missileHitDroneMultiplier = 3

militiaType = {'BMF':'1', 'AMF':'11', 'IMF':'21'}

# diplomacy
diplomacy = {1:{'name':'At War', 'engage':1, 'invade':1, 'trade':0, 'move':1, 'alliance':0,
                'description':'Being At War means you can attack and invade another player, you can do this at No Relations, however its one step harder to move to better relations when you are at War' },
             2:{'name':'No Relations', 'engage':1, 'invade':1, 'trade':0, 'move':1, 'alliance':0,
                'description':'Being At No Relations is the default relations, you can decide to attack another player without warning, however this will move you to an At War state'},
             3:{'name':'Non Agression Pact', 'engage':1, 'invade':0, 'trade':0, 'move':0, 'alliance':0,
                'description':'A Non Agression pack means your ships can only attack each other if they meet on a neutral battlefield.  You cannot move your ships onto each others planets until you decrease diplomacy'},
             4:{'name':'Trade Agreement', 'engage':0, 'invade':0, 'trade':1, 'move':0, 'alliance':0,
                'description':'A Trade Agreement allows two Empires to trade resources directly to each other including using warp gates to trade, your ships will also not fight each other if they meet on a neutral system, you can move your ships to your new friends planets, but if they lower diplomacy you could get stuck there.'},
             5:{'name':'Mutual Trading Partnership', 'engage':0, 'invade':0, 'trade':1, 'move':1, 'alliance':0,
                'description':'A Mutual Trading Partnership is the same as a Trade Agreement, you can still move ships and troops onto each others planets (you will not invade), its just one step closer to an alliance, and one step further from being backstabbed later, ie it would take one more turn of decreased diplomacy before the player could be attacked'},
             6:{'name':'Alliance', 'engage':0, 'invade':0, 'trade':1, 'move':1, 'alliance':1,
                'description':'An Alliance is the highest level of diplomacy, at this level players can use each others warp gates, although you can have many trade partners, you can only have one ally in the game at one time'}
             }


signalreceived = False            
dolePerCity = 700.0
shipUpkeep = 5.0 #ship mass divided by this number
armyUpkeep = 400.0
cityupkeepMultiplier = 400.0 #upkeep based on cities in empire in relation to this number

adminaccess = "will be filled in by main"

techDesciptions = {'Nuclear Age of Technology':'The Starting Age of Technology of all Empires',
'Fortresses':'Allows an Empire to build Fortresses on planets. Fortresses will provide some automated renewable defence from ground invasion with or without marines on the planet',
'Industry':'A Key technology that allows for the construction of Nuclear Age Factories. These Factories will allow planets to build more resources quicker. They are critical to a strong economy and should be one of the first things researched.',
'Starship Design':'The beginning technology to research new ship hulls, this also allows for the construction of Design Centers. Design Centers allow an Empire to build designs every turn',
'Radar':'Allows an Empire to build radar stations. Radar Stations on a planet will scan adjacent planets which allow an empire to view basic ship, marine, and planet information. If the planet has less jamming than an Empire with radar stations has radar.',
'Simulation Centers':'Allows for the construction of simulation centers on planets. Simulation Centers allow an empire to conduct simulations which are critical to determine good ship designs (that they function as designed). Simulations can also be used to set up large space battles to determine a powerful combination of ship designs working together. Simulation Centers are critical early game to make good ship designs for early expansion, and late game to determine the best fleet designs.',
'Simple Starship Components':'Simple Startship Components allow an Empire to begin to research the basic critical starship components required to build a startship such as Engines, Rotation Thrusters, and Power Plants. A critical technology that should be researched soon after Research Centers and Industry Factories.',
'Research Centers':'Research Centers are the most critical industry, and it should be assumed that most game maps will include this basic technology, which lets an Empire build research stations, which are critical to build research points. Remember that research is conducted by placing research into available (blue and yellow) technology beakers. When the round ends a percentage roll is conducted to determine if a research breakthrough occurs. The percentage is based on fraction of two numbers in the beaker (research being conducted / total research required).',
'Construction':'Construction will open up technology into building key military buildings that build ships, marines, and warp gates.',
'Fleet Academy':'The Fleet Academy will allow an empire to build Fleet Academies on their planets. Fleet Academies will produce a certain number of Fleet Cadets per round that are stored on the planet. Fleet cadets cannot be transferred and are only activated when that planet builds ships. For every ship built a fleet cadet (if available) will be assigned to the ship in question. This gives the ship the rank of cadet instead of rookie. A cadet will have slightly better abilities when operating a ship, and will more quickly increase in rank through ship battles. You can view the number of fleet cadets available when you click one of your planets and click to build ships.',
'Marine Academy':'The Marine Academy allows for further research into marines. The marine academy will also open up the ability of a planet to build marine academies. Much like fleet academies, marine academies will build a set number of marine cadets each round. These cadets cannot be transferred off the planet and will only activate if a marine regiment is built on the same planet. This will give that marine regiment the status of Trained, which gives a slight power increase, and allows a regiment to upgrade to the next experience levels as it successfully survives ground battles. You can view the number of marine cadets available when you click on one of your planets and click build marines.',
'Alloy Factories':'A critical technology Alloy Factories will allow an empire to build Allow Factories on a planet. These Factories will provide a certain percentage of increased alloy (blue resource) production if a planet has some of its cities focused on alloys. It is advised that an empire tries to keep planets focused on one resource type per planet to leverage the percentage bonuses of multiple factories boosting the production of a certain resource. The Blue resource is a key resource to build almost all industry and should be focused on when expanding or upgrading older industry on your planets. Make sure you transfer this resource from your Alloy focused planets to planets that do not make this industry in step with an increase of technology for key industry.',
'Starship Hulls':'Starship Hulls do not provide any benefit other than moving an empire closer to the starship technologies that open up new and more powerful ship and platform hull types.',
'Jamming':'In the early game Jamming is not important and should not be prioritized early. Jamming allows for the construction of Jamming Stations. These stations are important as an empire expands to the borders of other empires. Jamming stations will block other players radar stations from scanning your planet if they have radar stations. This can support hiding large fleets and armies, or other critical industry such as militia fortresses or warp gates from their intelligence (radar) supporting your efforts to deceive an upcoming attack or a strong defense.',
'Nuclear Starship Weapons':'Nuclear Starship weapons does not open up any technologies, but allows an empire to begin to research the Nuclear Energy and Nuclear Impact weapon streams.',
'Shipyards':'Shipyards is a basic technology that allows an empire to build Shipyards on their planets. Without shipyards being constructed a player cannot easily build ships (unless they have mobile shipyards, which you can learn about by clicking on engineering station technology).',
'Marine Installations':'This technology allows a player to build marine installations on a planet. These installations will allow an empire the capacity to build a certain number of marine regiments a turn, assuming the empire has the available credits and resources available. Remember, to learn how many of any industry you can build, click on your planet and click on Industry. Click on the industry in question and choose a technological age to see the effectiveness of that particular industry or installation. ',
'Nuclear Star Marines':'This technology by itself does not activate the ability to build star marines, but it opens up the technology choices of the three marine types (artillery, mechanized, and infantry. These are critical if a player wants to eventually invade and capture any planets. Although ships are critical to an Empire\'s success, without marines an empire will not be able to take any planets. There is no colonization in this game, the only way to expand is through invasion with space marines. Space marines come with their own built in transport, however, when moving to a planet for an invasion, they are vulnerable to destruction in space if that planet has space defences (ships or platforms).',
'Crystal Mines':'This technology allows for the construction of Crystal Mines, which is a factory that will increase the effectiveness of a planet in building Energy Crystals (yellow resource). This yellow resource is critical to building starships, advanced military industry, and Artillery marine regiments. ',
'Light Military Hulls':' This technology does not open up any construction ability but leads to the light starship hull technologies which do.',
'Platforms':'This technology allows an empire to build Platform based ships. Platforms are a unique hull design which has a lot more component space to build powerful ships that are built for two purposes. The first purpose is to defend an empires planets from invasion, the second is to build a mobile shipyard. Platforms cannot attack enemy planets. Learn about mobile shipyards by clicking on the engineering stations technology beaker.',
'Light Assault Ships':'This technology allows an empire to build Assault ship hulls. Assault ships are a unique ship type that allows a player to build an assault ship. These ships can be loaded with special marine pods that load up the ship with special space marines that do not invade planets, but instead invade other starships in the middle of a ship battle. The assault ship cannot carry any offensive weapons, however it can carry a combination of anti-missle guns, armor and shields as it tries to board an enemy ship. If the assault ship manages to board an enemy ship it will unload its space marines from their pods, and these marines will attempt to take over the enemy ship. ',
'Nuclear Drones':'This technology will allow an empire to research carriers and drone hulls.',
'Nuclear Impact Weapons':'This technology will allow an empire to research direct fire impact weapons (Graviton guns), and impact based missile launchers (nuclear missiles). The only difference between impact weapons and energy weapons is that impact weapons are not as affected by reflective armor, and impact weapons take more ammo requirements at a bonus of less energy required.',
'Nuclear Energy Weapons':'This technology will allow an empire to research direct fire energy weapons (phasor guns), and energy based missile launchers (nuclear torpedoes). The only difference between energy weapons and impact weapons is that energy weapons are not as affected by impact armor, and some energy weapons require no ammo, but require more energy to fire.',
'Warp Gates':'This technology will allow an empire to build warp gates on their planets. Warp gates are a critical industry as an empire grows in size as it allows ships, marines, and resources to be warped between two planets that have warp gates from anywhere on the galaxy map. One warp gate will provide a certain number of warp gate points which will stack with more warp gates on the same planet. In order to warp items between planets, both planets have to have warp points available which is visible near the planet names as a (warp points used / warp points available). Warp gates of friendly empires can also be used to transfer ships and resources if two empires have either a trade agreement or an alliance with each other.',
'Light Nuclear Infantry':'This technology allows an empire to build light nuclear infantry marine regiments for planet defense or planet invasion. Infantry are neutral to militia fortresses, strong against mechanized marines, and weak against artillery marines. As they are composed of AI robots, infantry marines only require the red (intelligence array) resource and credits to be constructed on a planet.',
'Light Nuclear Mechanized':'This technology allows an empire to build light nuclear mechanized marine regiments for planet defense or planet invasion. Mechanized are weaker to militia fortresses, strong against artillery marines, and weak to infantry marines. As they are composed of mechanized vehicles, these marine regiments require the blue (alloys) resource and credits to be constructed on a planet. ',
'Light Nuclear Artillery':'This technology allows an empire to build light artillery marine regiments for planet defense or planet invasion. Artillery is recommended for early expansion as they are strong against militia fortresses (which is the only defense of the neutral planets), and infantry regiments, however they are weak against mechanized regiments. Artillery regiments use a lot of power and require energy crystal (yellow) resource and credits to be constructed on a planet.',
'Synthetic Systems':'This technology allows an empire to build Synthetic Factories (Red Factories) which will stack on a planet that focuses its cities to build the Intelligence Arrays (the Red resource). ',
'Interceptors':'This technology will allow an empire to build Interceptors are a unique hull type in that they will bypass regular ships and target drone carriers. Although a risky strategy, in large numbers these ships could be an interesting counter to a heavily drone based enemy fleet. ',
'Light Nuclear Drones':'This technology will allow an empire to begin building light nuclear drone hulls. This hull type is useless unless the carrier or platform hull types have also been researched, as only carriers and platforms can insert drones as a weapon into their respective ship designs. Drones are a particularly powerful ship design when combined with a carrier or platform as they can be used as cannon fodder to distract an enemy fleet. The advantage of these ships is that they will regenerate assuming the carrier survives the battle. Drones are also useful as a counter to the larger direct fire based ship designs as they will focus these powerful ships on a small drone instead of on larger prey. Drones are more vulnerable to missile based ship designs as drones cannot carry AMS (anti missile) systems.',
'Graviton Gun':'This technology will allow an Empire to equip its ships with the Light Graviton Gun. This weapon has a short range and require low power to fire, but does require ammo. It is affected more by impact armor than reflective armor.',
'Nuclear Missiles':'This technology will allow an Empire to equip its ships with the Light Nuclear Missile Launcher. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by impact armor than reflective armor. ',
'Phasor Gun':'This technology will allow an Empire to equip its ships with the Light Phasor Gun. This weapon has a short range and require medium power to fire, but does not require ammo. It is affected more by reflective armor than impact armor. ',
'Nuclear Torpedoes':'This technology will allow an Empire to equip its ships with the Light Nuclear Torpedoes. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by reflective armor than impact armor. ',
'Simple Defensive Systems':'This is a key technology which opens up defensive technologies such as anti missile systems, armor and shields for starships. On its own this technology does not enable any components however.',
'Simple Starship Engines':'This key technology allows ships to equip nuclear engines. Engines allow a ship to move during battle, and every starship design needs at least one engine component to be considered a valid design. Engines do not affect warp capability for ships, as all ships warp at the same speed between adjacent planets or through warp gates.',
'Simple Rotation Thrusters':'This key technology allows ships to rotate faster during battle and every starship design needs at least one rotation component to be considered a valid design. Rotation is not as critical as Engines or Power Plants, as not as many components are needed to max out rotation on a ship. ',
'Simple Power Plants':'This key technology allows ships to power their weapons, anti-missile guns, shields, and batteries. Every starship design needs at least one power plant component to be considered a valid design. Power plants are critical as they allow weapons and anti-missile guns to fire at a fast rate. ',
'Simple Radar':'This technology allows a starship to equip radar scanners directly on a ship design. Radar scanners are often overlooked as they do not provide a ship with any offensive or defensive advantages. They do however provide an empire with two interesting intelligence bonuses: First, a ship with radar capability that is in a battle with an enemy fleet will provide the empire the ability to click and view the enemy ship components and how they react during the entire battle. Since every battle is saved, this can be invaluable information for an empire to plan a counter fleet design for future battles. Secondly, this component adds to the scanning ability of an empire when ships with radar scanners are hovering over an enemy fleet potentially providing Intel on the planet assuming the planet does not have sufficient jamming stations. ',
'Medium Nuclear Infantry':'This technology allows an empire to build medium nuclear infantry regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology.',
'Medium Nuclear Mechanized':'This technology allows an empire to build medium nuclear mechanized regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology',
'Medium Nuclear Artillery':'This technology allows an empire to build medium nuclear artillery regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology',
'Corvettes':'This technology will allow an empire to build corvette class ships. These ships are the second largest of the nuclear age and have a special design in that they target assault ships over other ship classes as a primary target making them a potentially good screen ship to protect larger more critical friendly ships from assault ship counters. ',
'Medium Nuclear Drones':'This technology allows an empire to build medium nuclear drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Medium Graviton Gun':'This technology allows an empire to build a medium Graviton Gun, this is similar to the light Graviton gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship.',
'Medium Nuclear Missiles':'This technology allows an empire to build a medium Nuclear Missile Launcher, this is similar to the light Nuclear Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Medium Phasor Gun':'This technology allows an empire to build a medium Phasor Gun, this is similar to the light Phasor gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship.',
'Medium Fusion Cannon':'This technology allows an empire to build a medium Fusion Cannon, this is similar to the Light Fusion Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship.',
'Medium Nuclear Torpedoes':'This technology allows an empire to build a medium Nuclear Torpedo Launcher, this is similar to the light Nuclear Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Simple StarShip Armor':'This technology does not enable any ship component, but leads to both reflective and impact armor technologies.',
'Simple Anti-Missile System':'This technology does not enable any ship component, but leads to both Anti Missile Technologies for AMS Graviton (needs ammo) and AMS Phasor (does not need ammo, but needs more power). ',
'Simple Engineering Stations':'This technology is often overlooked by starting empires, but can be quite powerful for more complicated empires with a larger demand of logistics around ship construction, repair and upgrades. These components can only be built on the platform hull type limiting them to orbit friendly empires, however, it does allow for an empire to build a mobile shipyard. When a platform design includes engineering stations of any great quantity that platform once constructed will allow any friendly planet that the platform orbits to act as if it had a shipyard constructed. The advantages of this arrangement are that the shipyards are now mobile and can follow a friendly fleet for easy repair and upgrade as well as ship construction. Planets will also not have to use cities to populate the shipyards, so they can be allocated to other industries. The disadvantage is that resources will have to follow the mobile shipyard through trade routes that will have to modify over time, the mobile shipyards are vulnerable to a fleet attack as they are not situated as part of the planet\'s infrastructure, and the mobile shipyard is considered a ship and therefore will require upkeep costs every round in the form of credits to its crew.',
'Simple Starship Batteries':'This powerful technology allows a starship design to have a backup of stored energy that is filled by free power plant energy when not being used by other components. Starship batteries greatly increase the power of shields and Anti-Missile components, and are especially effective on larger ships that have the component space to combine AMS with Large weapons, targeting computers, and shields. It is recommended that this advanced technology is tested throughouly when doing ship design and ship simulation to truly unlock its power in a well-designed medium to large capital ship class.',
'Heavy Nuclear Infantry':'This technology allows an empire to build heavy nuclear infantry regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology',
'Heavy Nuclear Mechanized':'This technology allows an empire to build heavy nuclear mechanized regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Nuclear Artillery':'This technology allows an empire to build heavy nuclear artillery regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Corvettes':'This technology allows an empire to build the most used ship hull type of the nuclear age: the Heavy Corvette. This all-around ship has the best number of component spaces of any lighter hull type, but as a lighter ship class it also enjoys more efficient engine and rotation bonuses when compared to heavier frigate or destroyer class ships. The heavy corvette also does not act as a specialized ship to target a specific ship type like the interceptor or regular corvette, which makes it a good ship-of-the-line for large engagements. It is not uncommon to see advanced fleets in later ages with Heavy Corvettes upgraded with fusion and plasma age technology.',
'Escort Carriers':'This technology will allow an empire to begin building carrier hulls, a very powerful, critical, and unique ship hull class. This hull type is useless unless the drone hulls have also been researched, as only carriers and platforms can insert drones as a weapon into their respective ship designs. Drones are a particularly powerful ship design when combined with a carrier or platform as they can be used as cannon fodder to distract an enemy fleet. The advantage of these ships is that they will regenerate assuming the carrier survives the battle. Drones are also useful as a counter to the larger direct fire based ship designs as they will focus these powerful ships on a small drone instead of on larger prey. Drones are more vulnerable to missile based ship designs as drones cannot carry AMS (anti missile) systems. Carriers are also vulnerable to interceptors that target them specifically',
'Heavy Nuclear Drones':'This technology allows an empire to build heavy nuclear drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Heavy Graviton Gun':'This technology allows an empire to build a Heavy Graviton Gun, this is similar to the medium Graviton gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Nuclear Missiles':'This technology allows an empire to build a Heavy Nuclear Missile Launcher, this is similar to the medium Nuclear Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Phasor Gun':'This technology allows an empire to build a Heavy Phasor Gun, this is similar to the medium Phasor gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Nuclear Torpedoes':'This technology allows an empire to build a Heavy Nuclear Torpedo Launcher, this is similar to the Medium Nuclear Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Simple Impact Armor':'This technology allows an empire to equip its ships with simple impact armor. Impact armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to impact based weapon hits. Impact armor cannot mix with reflective armor in the same ship quadrant.',
'Simple Reflective Armor':'This technology allows an empire to equip its ships with simple reflective armor. Reflective armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to energy based weapon hits. Reflective armor cannot mix with impact armor in the same ship quadrant. ',
'Simple Starship Shields':'This technology allows an empire to equip its ships with simple starship shield components. These components provide a ship with a regenerating shield protection, and combines well with ship batteries.',
'Simple Targeting Computers':'This technology when placed in any particular quadrant of a ship will provide any weapons or AMS systems with a lower targeting requirement, allowing ships to become more effective in offense and defense (from missile attack). When using targeting computers notice the weapon lock time (in brackets) will go down. Try to match this time to the overall power recharge time, and use simulations to see the ship design in action to make sure power requirements match targeting requirements for a ship design. ',
'AMS Graviton Gun':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Graviton Gun requires ammo, but takes less power.',
'AMS Phasor Gun':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Phasor Gun does not requires ammo, but takes more power.',
'Carrier Tech':'This technology does not provide any ship hull, but leads towards the path to the Escort Carrier technology which does provide a powerful ship class to an expanding empire.',
'Remote Tech':'This technology does not provide any ship hull, but leads towards the path to the Escort Carrier technology which does provide a powerful ship class to an expanding empire.',
'Simple Jamming':'This technology allows a ship design to build the Jamming Dishes component. This component does not affect a ships combat abilities, however it is a powerful tool as part of a larger fleet as it does two primary tasks: First, it can jam the radar scans of an enemy fleet during battle, making it more difficult for an enemy player to understand how the ship designs work for an empire\'s fleet. Second, it can jam the details of a fleet from the planetary level, and consequently also jam any information about a planet as the ships jamming will support the jamming at the planet level as well, if the ships with jamming components happen to be orbiting a friendly planet. ',
'Fusion Age of Technology':'This technology opens up the ability to research all the Fusion Era Technologies. Notice that there is a P:12 above this Tech Beaker. This means that 12 technologies from the Nuclear Age that connect to this technology have to be researched before and empire can start to research this Technology. This opens up planning options to skip certain technologies and get to the Fusion Age faster than a competing empire. ',
'Advanced Fortresses':' Similar to Simple Fortresses, but more militia will be available for planet defense per fortress constructed. ',
'Advanced Industry':'Although this technology does not allow for any industry to be constructed, it opens up for the three factory based technologies in the Fusion Age to be Researched. This should be made a priority when deciding what technologies to research early on, as increasing factory levels will greatly increase an empire\'s economy with more resources and credits being produced every turn to support an empire\'s expansion efforts',
'Advanced Starship Design':'This technology does not directly enable a new ship hull, but it is a key pre-technology that leads to the ability to research the Fusion Age ship hulls. ',
'Advanced Radar':'This technology will allow an empire to build Advanced Radar stations on a planet. Radar Stations on a planet will scan adjacent planets which allow an empire to view basic ship, marine, and planet information. If the planet has less jamming than an Empire with radar stations has radar. ',
'Advanced Simulation Centers':'Allows for the construction of advanced simulation centers on planets. Simulation Centers allow an empire to conduct simulations which are critical to determine good ship designs (that they function as designed). Simulations can also be used to set up large space battles to determine a powerful combination of ship designs working together. Simulation Centers are critical early game to make good ship designs for early expansion, and late game to determine the best fleet designs.',
'Progressive Starship Components':'Progressive Startship Components allow an Empire to begin to research the progressive based critical starship components required to build a starship such as Engines, Rotation Thrusters, and Power Plants. A critical technology that should be researched soon after Research Centers and Industry Factories.',
'Advanced Research Centers':'Research Centers let an Empire build research stations, which are critical to build research points. Remember that research is conducted by placing research into available (blue and yellow) technology beakers. When the round ends a percentage roll is conducted to determine if a research breakthrough occurs. The percentage is based on fraction of two numbers in the beaker (research being conducted / total research required).',
'Advanced Construction':'Construction will open up technology into building key military buildings that build ships, marines, and warp gates. ',
'Advanced Fleet Academy':'The Fleet Academy will allow an empire to build Fleet Academies on their planets. Fleet Academies will produce a certain number of Fleet Cadets per round that are stored on the planet. Fleet cadets cannot be transferred and are only activated when that planet builds ships. For every ship built a fleet cadet (if available) will be assigned to the ship in question. This gives the ship the rank of cadet instead of rookie. A cadet will have slightly better abilities when operating a ship, and will more quickly increase in rank through ship battles. You can view the number of fleet cadets available when you click one of your planets and click to build ships. ',
'Advanced Marine Academy':'The Marine Academy allows for further research into marines. The marine academy will also open up the ability of a planet to build marine academies. Much like fleet academies, marine academies will build a set number of marine cadets each round. These cadets cannot be transferred off the planet and will only activate if a marine regiment is built on the same planet. This will give that marine regiment the status of Trained, which gives a slight power increase, and allows a regiment to upgrade to the next experience levels as it successfully survives ground battles. You can view the number of marine cadets available when you click on one of your planets and click build marines. ',
'Advanced Alloy Factories':'A critical technology Alloy Factories will allow an empire to build advanced Allow Factories on a planet. These Factories will provide a certain percentage of increased alloy (blue resource) production if a planet has some of its cities focused on alloys. It is advised that an empire tries to keep planets focused on one resource type per planet to leverage the percentage bonuses of multiple factories boosting the production of a certain resource. The Blue resource is a key resource to build almost all industry and should be focused on when expanding or upgrading older industry on your planets. Make sure you transfer this resource from your Alloy focused planets to planets that do not make this industry in step with an increase of technology for key industry. ',
'Advanced Starship Hulls':'Starship Hulls do not provide any benefit other than moving an empire closer to the starship technologies that open up new and more powerful ship and platform hull types. ',
'Advanced Jamming':'In the early game Jamming is not important and should not be prioritized early. Jamming allows for the construction of Advanced Jamming Stations. These stations are important as an empire expands to the borders of other empires. Jamming stations will block other players radar stations from scanning your planet if they have radar stations. This can support hiding large fleets and armies, or other critical industry such as militia fortresses or warp gates from their intelligence (radar) supporting your efforts to deceive an upcoming attack or a strong defense. ',
'Fusion Starship Weapons':'Fusion Starship weapons does not open up any technologies, but allows an empire to begin to research the Fusion Energy and Fusion Impact weapon streams. ',
'Advanced Shipyards':'Shipyards is a basic technology that allows an empire to build Advanced Shipyards on their planets. Without shipyards being constructed a player cannot easily build ships (unless they have mobile shipyards, which you can learn about by clicking on engineering station technology). ',
'Advanced Marine Installations':'This technology allows a player to build advanced marine installations on a planet. These installations will allow an empire the capacity to build a certain number of marine regiments a turn, assuming the empire has the available credits and resources available. Remember, to learn how many of any industry you can build, click on your planet and click on Industry. Click on the industry in question and choose a technological age to see the effectiveness of that particular industry or installation. ',
'Fusion Star Marines':'This technology by itself does not activate the ability to build star marines, but it opens up the technology choices of the three marine types (artillery, mechanized, and infantry. These are critical if a player wants to eventually invade and capture any planets. Although ships are critical to an Empire\'s success, without marines an empire will not be able to take any planets. There is no colonization in this game, the only way to expand is through invasion with space marines. Space marines come with their own built in transport, however, when moving to a planet for an invasion, they are vulnerable to destruction in space if that planet has space defences (ships or platforms). ',
'Advanced Crystal Mines':'This technology allows for the construction of Advanced Crystal Mines, which is a factory that will increase the effectiveness of a planet in building Energy Crystals (yellow resource). This yellow resource is critical to building starships, advanced military industry, and Artillery marine regiments. ',
'Advanced Military Hulls':'This technology does not open up any construction ability but leads to the advanced starship hull technologies which do. ',
'Heavy Platforms':'This technology allows an empire to build Heavy Platform based ships. Platforms are a unique hull design which has a lot more component space to build powerful ships that are built for two purposes. The first purpose is to defend an empires planets from invasion, the second is to build a mobile shipyard. Platforms cannot attack enemy planets. Learn about mobile shipyards by clicking on the engineering stations technology beaker. ',
'Heavy Assault Ships':'This technology allows an empire to build Heavy Assault ship hulls. Assault ships are a unique ship type that allows a player to build an assault ship. These ships can be loaded with special marine pods that load up the ship with special space marines that do not invade planets, but instead invade other starships in the middle of a ship battle. The assault ship cannot carry any offensive weapons, however it can carry a combination of anti-missle guns, armor and shields as it tries to board an enemy ship. If the assault ship manages to board an enemy ship it will unload its space marines from their pods, and these marines will attempt to take over the enemy ship. ',
'Fusion Drones':'This technology will allow an empire to research Fusion carriers and drone hulls. ',
'Fusion Impact Weapons':'This technology will allow an empire to research direct fire impact weapons (Auto Cannons), and impact based missile launchers (Fusion missiles). The only difference between impact weapons and energy weapons is that impact weapons are not as affected by reflective armor, and impact weapons take more ammo requirements at a bonus of less energy required. ',
'Fusion Energy Weapons':'This technology will allow an empire to research direct fire energy weapons (Fusion Cannons), and energy based missile launchers (Fusion torpedoes). The only difference between energy weapons and impact weapons is that energy weapons are not as affected by impact armor, and some energy weapons require no ammo, but require more energy to fire.',
'Advanced Warp Gates':'This technology will allow an empire to build advanced warp gates on their planets. Warp gates are a critical industry as an empire grows in size as it allows ships, marines, and resources to be warped between two planets that have warp gates from anywhere on the galaxy map. One warp gate will provide a certain number of warp gate points which will stack with more warp gates on the same planet. In order to warp items between planets, both planets have to have warp points available which is visible near the planet names as a (warp points used / warp points available). Warp gates of friendly empires can also be used to transfer ships and resources if two empires have either a trade agreement or an alliance with each other. ',
'Light Fusion Infantry':'This technology allows an empire to build light fusion infantry marine regiments for planet defense or planet invasion. Infantry are neutral to militia fortresses, strong against mechanized marines, and weak against artillery marines. As they are composed of AI robots, infantry marines only require the red (intelligence array) resource and credits to be constructed on a planet. ',
'Light Fusion Mechanized':'This technology allows an empire to build light fusion mechanized marine regiments for planet defense or planet invasion. Mechanized are weaker to militia fortresses, strong against artillery marines, and weak to infantry marines. As they are composed of mechanized vehicles, these marine regiments require the blue (alloys) resource and credits to be constructed on a planet.',
'Light Fusion Artillery':'This technology allows an empire to build light fusion artillery marine regiments for planet defense or planet invasion. Artillery is recommended for early expansion as they are strong against militia fortresses (which is the only defense of the neutral planets), and infantry regiments, however they are weak against mechanized regiments. Artillery regiments use a lot of power and require energy crystal (yellow) resource and credits to be constructed on a planet.',
'Advanced Synthetic Systems':'This technology allows an empire to build Advanced Synthetic Factories (Red Factories) which will stack on a planet that focuses its cities to build the Intelligence Arrays (the Red resource). ',
'Frigates':'This technology allows an empire to build a good medium-class ship hull, the Frigate.',
'Light Fusion Drones':'This technology will allow an empire to begin building light fusion drone hulls. This hull type is useless unless the carrier or platform hull types have also been researched, as only carriers and platforms can insert drones as a weapon into their respective ship designs. Drones are a particularly powerful ship design when combined with a carrier or platform as they can be used as cannon fodder to distract an enemy fleet. The advantage of these ships is that they will regenerate assuming the carrier survives the battle. Drones are also useful as a counter to the larger direct fire based ship designs as they will focus these powerful ships on a small drone instead of on larger prey. Drones are more vulnerable to missile based ship designs as drones cannot carry AMS (anti missile) systems. ',
'Auto Cannon':'This technology will allow an Empire to equip its ships with the Light Auto Cannon. This weapon has a short range and require low power to fire, but does require ammo. It is affected more by impact armor than reflective armor. ',
'Fusion Missiles':'This technology will allow an Empire to equip its ships with the Light Fusion Missile Launcher. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by impact armor than reflective armor. ',
'Fusion Cannon':'This technology will allow an Empire to equip its ships with the Light Fusion Cannon. This weapon has a short range and require medium power to fire, but does not require ammo. It is affected more by reflective armor than impact armor. ',
'Fusion Torpedoes':'This technology will allow an Empire to equip its ships with the Light Fusion Torpedoes. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by reflective armor than impact armor. ',
'Progressive Defensive Systems':'This is a key technology which opens up defensive technologies such as anti missile systems, armor and shields for starships. On its own this technology does not enable any components however. ',
'Progressive Starship Engines':'This key technology allows ships to equip progressive engines. Engines allow a ship to move during battle, and every starship design needs at least one engine component to be considered a valid design. Engines do not affect warp capability for ships, as all ships warp at the same speed between adjacent planets or through warp gates. ',
'Progressive Rotation Thrusters':'This key technology allows ships to rotate faster during battle and every starship design needs at least one rotation component to be considered a valid design. Rotation is not as critical as Engines or Power Plants, as not as many components are needed to max out rotation on a ship. ',
'Progressive Power Plants':'This key technology allows ships to power their weapons, anti-missile guns, shields, and batteries. Every starship design needs at least one power plant component to be considered a valid design. Power plants are critical as they allow weapons and anti-missile guns to fire at a fast rate. ',
'Progressive Radar':'This technology allows a starship to equip progressive radar scanners directly on a ship design. Radar scanners are often overlooked as they do not provide a ship with any offensive or defensive advantages. They do however provide an empire with two interesting intelligence bonuses: First, a ship with radar capability that is in a battle with an enemy fleet will provide the empire the ability to click and view the enemy ship components and how they react during the entire battle. Since every battle is saved, this can be invaluable information for an empire to plan a counter fleet design for future battles. Secondly, this component adds to the scanning ability of an empire when ships with radar scanners are hovering over an enemy fleet potentially providing Intel on the planet assuming the planet does not have sufficient jamming stations. ',
'Medium Fusion Infantry':'This technology allows an empire to build medium fusion infantry regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology. ',
'Medium Fusion Mechanized':'This technology allows an empire to build medium fusion mechanized regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology ',
'Medium Fusion Artillery':'This technology allows an empire to build medium fusion artillery regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology ',
'Battle Frigates':'This Technology allows an empire to build the slightly improved Battle Frigate ship type.',
'Medium Fusion Drones':'This technology allows an empire to build medium fusion drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Medium Auto Cannon':'This technology allows an empire to build a medium Auto Cannon, this is similar to the light Auto Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Medium Plasma Cannon':'This technology allows an empire to build a medium Plasma Cannon, this is similar to the light Plasma Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Medium Fusion Missiles':'This technology allows an empire to build a medium Fusion Missile Launcher, this is similar to the light Fusion Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship.',
'Medium Fusion Torpedoes':'This technology allows an empire to build a medium Fusion Torpedo Launcher, this is similar to the light Fusion Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Progressive StarShip Armor':'This technology does not enable any ship component, but leads to both reflective and impact armor technologies. ',
'Progressive Anti-Missile System':'This technology does not enable any ship component, but leads to both Anti Missile Technologies for AMS Auto Cannon (needs ammo) and AMS Fusion Cannon (does not need ammo, but needs more power). ',
'Progressive Engineering Stations':'This technology is often overlooked by starting empires, but can be quite powerful for more complicated empires with a larger demand of logistics around ship construction, repair and upgrades. These components can only be built on the platform hull type limiting them to orbit friendly empires, however, it does allow for an empire to build a mobile shipyard. When a platform design includes engineering stations of any great quantity that platform once constructed will allow any friendly planet that the platform orbits to act as if it had a shipyard constructed. The advantages of this arrangement are that the shipyards are now mobile and can follow a friendly fleet for easy repair and upgrade as well as ship construction. Planets will also not have to use cities to populate the shipyards, so they can be allocated to other industries. The disadvantage is that resources will have to follow the mobile shipyard through trade routes that will have to modify over time, the mobile shipyards are vulnerable to a fleet attack as they are not situated as part of the planet\'s infrastructure, and the mobile shipyard is considered a ship and therefore will require upkeep costs every round in the form of credits to its crew. ',
'Progressive Starship Batteries':'This powerful technology allows a starship design to have a backup of stored energy that is filled by free power plant energy when not being used by other components. Starship batteries greatly increase the power of shields and Anti-Missile components, and are especially effective on larger ships that have the component space to combine AMS with Large weapons, targeting computers, and shields. It is recommended that this advanced technology is tested throughouly when doing ship design and ship simulation to truly unlock its power in a well-designed medium to large capital ship class. ',
'Heavy Fusion Infantry':'This technology allows an empire to build heavy fusion infantry regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Fusion Mechanized':'This technology allows an empire to build heavy fusion mechanized regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Fusion Artillery':'This technology allows an empire to build heavy fusion artillery regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Destroyers':'This technology allows an empire to build the largest of the Fusion Era of ship hulls, the Destroyer. A great all-around ship that is often seen in later stage fleets as a affordable support ship to the larger cruiser and dreadnought starships.',
'Heavy Carriers':'This technology allows for the construction of the largest carrier hull type in the Fusion Age.',
'Heavy Fusion Drones':'This technology allows an empire to build heavy Fusion drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Heavy Auto Cannon':'This technology allows an empire to build a Heavy Auto Cannon, this is similar to the Auto Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Fusion Missiles':'This technology allows an empire to build a Heavy Fusion Missile Launcher, this is similar to the medium Fusion Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Fusion Cannon':'This technology allows an empire to build a Heavy Fusion Cannon, this is similar to the medium Fusion Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Fusion Torpedoes':'This technology allows an empire to build a Heavy Nuclear Torpedo Launcher, this is similar to the Medium Nuclear Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Progressive Impact Armor':'This technology allows an empire to equip its ships with progressive impact armor. Impact armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to impact based weapon hits. Impact armor cannot mix with reflective armor in the same ship quadrant. ',
'Progressive Reflective Armor':'This technology allows an empire to equip its ships with progressive reflective armor. Reflective armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to energy based weapon hits. Reflective armor cannot mix with impact armor in the same ship quadrant. ',
'Progressive Starship Shields':'This technology allows an empire to equip its ships with progressive starship shield components. These components provide a ship with a regenerating shield protection, and combines well with ship batteries. ',
'Progressive Targeting Computers':'This technology when placed in any particular quadrant of a ship will provide any weapons or AMS systems with a lower targeting requirement, allowing ships to become more effective in offense and defense (from missile attack). When using targeting computers notice the weapon lock time (in brackets) will go down. Try to match this time to the overall power recharge time, and use simulations to see the ship design in action to make sure power requirements match targeting requirements for a ship design. ',
'AMS Auto Cannon':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Auto Cannon requires ammo, but takes less power. ',
'AMS Fusion Cannon':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Fusion Cannon does not requires ammo, but takes more power. ',
'Progressive Jamming':'This technology allows a ship design to build the Progressive Jamming Dishes component. This component does not affect a ships combat abilities, however it is a powerful tool as part of a larger fleet as it does two primary tasks: First, it can jam the radar scans of an enemy fleet during battle, making it more difficult for an enemy player to understand how the ship designs work for an empire\'s fleet. Second, it can jam the details of a fleet from the planetary level, and consequently also jam any information about a planet as the ships jamming will support the jamming at the planet level as well, if the ships with jamming components happen to be orbiting a friendly planet. ',
'Plasma Age of Technology':'This technology opens up the ability to research all the Plasma Era Technologies. Notice that there is a P:12 above this Tech Beaker. This means that 12 technologies from the Fusion Age that connect to this technology have to be researched before and empire can start to research this Technology. This opens up planning options to skip certain technologies and get to the Plasma Age faster than a competing empire. ',
'Intelligent Fortresses':'Similar to Advanced Fortresses, but more militia will be available for planet defense per fortress constructed. ',
'Intelligent Industry':'Although this technology does not allow for any industry to be constructed, it opens up for the three factory based technologies in the Plasma Age to be Researched. This should be made a priority when deciding what technologies to research early on, as increasing factory levels will greatly increase an empire\'s economy with more resources and credits being produced every turn to support an empire\'s expansion efforts.',
'Intelligent Starship Design':'This technology does not directly enable a new ship hull, but it is a key pre-technology that leads to the ability to research the Plasma Age ship hulls.  ',
'Intelligent Radar':'This technology will allow an empire to build Intelligent Radar stations on a planet. Radar Stations on a planet will scan adjacent planets which allow an empire to view basic ship, marine, and planet information. If the planet has less jamming than an Empire with radar stations has radar. ',
'Intelligent Simulation Centers':'Allows for the construction of intelligent simulation centers on planets. Simulation Centers allow an empire to conduct simulations which are critical to determine good ship designs (that they function as designed). Simulations can also be used to set up large space battles to determine a powerful combination of ship designs working together. Simulation Centers are critical early game to make good ship designs for early expansion, and late game to determine the best fleet designs.',
'Ultra Starship Components':'Ultra Startship Components allow an Empire to begin to research the ultra critical starship components required to build a starship such as Engines, Rotation Thrusters, and Power Plants. A critical technology that should be researched soon after Research Centers and Industry Factories. ',
'Intelligent Research Centers':'Research Centers let an Empire build research stations, which are critical to build research points. Remember that research is conducted by placing research into available (blue and yellow) technology beakers. When the round ends a percentage roll is conducted to determine if a research breakthrough occurs. The percentage is based on fraction of two numbers in the beaker (research being conducted / total research required).',
'Intelligent Construction':'Construction will open up technology into building key military buildings that build ships, marines, and warp gates. ',
'Intelligent Fleet Academy':'The Fleet Academy will allow an empire to build Fleet Academies on their planets. Fleet Academies will produce a certain number of Fleet Cadets per round that are stored on the planet. Fleet cadets cannot be transferred and are only activated when that planet builds ships. For every ship built a fleet cadet (if available) will be assigned to the ship in question. This gives the ship the rank of cadet instead of rookie. A cadet will have slightly better abilities when operating a ship, and will more quickly increase in rank through ship battles. You can view the number of fleet cadets available when you click one of your planets and click to build ships. ',
'Intelligent Marine Academy':'The Marine Academy allows for further research into marines. The marine academy will also open up the ability of a planet to build marine academies. Much like fleet academies, marine academies will build a set number of marine cadets each round. These cadets cannot be transferred off the planet and will only activate if a marine regiment is built on the same planet. This will give that marine regiment the status of Trained, which gives a slight power increase, and allows a regiment to upgrade to the next experience levels as it successfully survives ground battles. You can view the number of marine cadets available when you click on one of your planets and click build marines. ',
'Intelligent Alloy Factories':'A critical technology Alloy Factories will allow an empire to build Intelligent Allow Factories on a planet. These Factories will provide a certain percentage of increased alloy (blue resource) production if a planet has some of its cities focused on alloys. It is advised that an empire tries to keep planets focused on one resource type per planet to leverage the percentage bonuses of multiple factories boosting the production of a certain resource. The Blue resource is a key resource to build almost all industry and should be focused on when expanding or upgrading older industry on your planets. Make sure you transfer this resource from your Alloy focused planets to planets that do not make this industry in step with an increase of technology for key industry. ',
'Intelligent Starship Hulls':'Starship Hulls do not provide any benefit other than moving an empire closer to the starship technologies that open up new and more powerful ship and platform hull types. ',
'Intelligent Jamming':'In the early game Jamming is not important and should not be prioritized early. Jamming allows for the construction of Intelligent Jamming Stations. These stations are important as an empire expands to the borders of other empires. Jamming stations will block other players radar stations from scanning your planet if they have radar stations. This can support hiding large fleets and armies, or other critical industry such as militia fortresses or warp gates from their intelligence (radar) supporting your efforts to deceive an upcoming attack or a strong defense. ',
'Plasma Starship Weapons':'Plasma Starship weapons does not open up any technologies, but allows an empire to begin to research the Plasma Energy and Plasma Impact weapon streams. ',
'Intelligent Shipyards':'Shipyards is a basic technology that allows an empire to build Intelligent Shipyards on their planets. Without shipyards being constructed a player cannot easily build ships (unless they have mobile shipyards, which you can learn about by clicking on engineering station technology). ',
'Intelligent Marine Installations':'This technology allows a player to build intelligent marine installations on a planet. These installations will allow an empire the capacity to build a certain number of marine regiments a turn, assuming the empire has the available credits and resources available. Remember, to learn how many of any industry you can build, click on your planet and click on Industry. Click on the industry in question and choose a technological age to see the effectiveness of that particular industry or installation. ',
'Plasma Star Marines':'This technology by itself does not activate the ability to build star marines, but it opens up the technology choices of the three marine types (artillery, mechanized, and infantry. These are critical if a player wants to eventually invade and capture any planets. Although ships are critical to an Empire\'s success, without marines an empire will not be able to take any planets. There is no colonization in this game, the only way to expand is through invasion with space marines. Space marines come with their own built in transport, however, when moving to a planet for an invasion, they are vulnerable to destruction in space if that planet has space defences (ships or platforms). ',
'Intelligent Crystal Mines':'This technology allows for the construction of Intelligent Crystal Mines, which is a factory that will increase the effectiveness of a planet in building Energy Crystals (yellow resource). This yellow resource is critical to building starships, advanced military industry, and Artillery marine regiments. ',
'Intelligent Military Hulls':'This technology does not open up any construction ability but leads to the plasma level starship hull technologies which do. ',
'Battle Platforms':'This technology allows an empire to build Battle Platform based ships. Platforms are a unique hull design which has a lot more component space to build powerful ships that are built for two purposes. The first purpose is to defend an empires planets from invasion, the second is to build a mobile shipyard. Platforms cannot attack enemy planets. Learn about mobile shipyards by clicking on the engineering stations technology beaker. ',
'Battle Assault Ships':'This technology allows an empire to build Battle Assault ship hulls. Assault ships are a unique ship type that allows a player to build an assault ship. These ships can be loaded with special marine pods that load up the ship with special space marines that do not invade planets, but instead invade other starships in the middle of a ship battle. The assault ship cannot carry any offensive weapons, however it can carry a combination of anti-missle guns, armor and shields as it tries to board an enemy ship. If the assault ship manages to board an enemy ship it will unload its space marines from their pods, and these marines will attempt to take over the enemy ship. ',
'Plasma Drones':'This technology will allow an empire to research plasma carriers and drone hulls. ',
'Plasma Impact Weapons':'This technology will allow an empire to research direct fire impact weapons (Rail guns), and impact based missile launchers (plasma missiles). The only difference between impact weapons and energy weapons is that impact weapons are not as affected by reflective armor, and impact weapons take more ammo requirements at a bonus of less energy required. ',
'Plasma Energy Weapons':'This technology will allow an empire to research direct fire energy weapons (Plasma Cannons), and energy based missile launchers (Plasma torpedoes). The only difference between energy weapons and impact weapons is that energy weapons are not as affected by impact armor, and some energy weapons require no ammo, but require more energy to fire. ',
'Intelligent Warp Gates':'This technology will allow an empire to build intelligent warp gates on their planets. Warp gates are a critical industry as an empire grows in size as it allows ships, marines, and resources to be warped between two planets that have warp gates from anywhere on the galaxy map. One warp gate will provide a certain number of warp gate points which will stack with more warp gates on the same planet. In order to warp items between planets, both planets have to have warp points available which is visible near the planet names as a (warp points used / warp points available). Warp gates of friendly empires can also be used to transfer ships and resources if two empires have either a trade agreement or an alliance with each other. ',
'Light Plasma Infantry':'This technology allows an empire to build light plasma infantry marine regiments for planet defense or planet invasion. Infantry are neutral to militia fortresses, strong against mechanized marines, and weak against artillery marines. As they are composed of AI robots, infantry marines only require the red (intelligence array) resource and credits to be constructed on a planet. ',
'Light Plasma Mechanized':'This technology allows an empire to build light plasma mechanized marine regiments for planet defense or planet invasion. Mechanized are weaker to militia fortresses, strong against artillery marines, and weak to infantry marines. As they are composed of mechanized vehicles, these marine regiments require the blue (alloys) resource and credits to be constructed on a planet. ',
'Light Plasma Artillery':'This technology allows an empire to build light plasma artillery marine regiments for planet defense or planet invasion. Artillery is recommended for early expansion as they are strong against militia fortresses (which is the only defense of the neutral planets), and infantry regiments, however they are weak against mechanized regiments. Artillery regiments use a lot of power and require energy crystal (yellow) resource and credits to be constructed on a planet. ',
'Intelligent Synthetic Systems':'This technology allows an empire to build Intelligent Synthetic Factories (Red Factories) which will stack on a planet that focuses its cities to build the Intelligence Arrays (the Red resource). ',
'Cruisers':'This technology will allow an empire to build cruiser hull types, the first of the capital ship class of starships.',
'Light Plasma Drones':'This technology will allow an empire to begin building light plasma drone hulls. This hull type is useless unless the carrier or platform hull types have also been researched, as only carriers and platforms can insert drones as a weapon into their respective ship designs. Drones are a particularly powerful ship design when combined with a carrier or platform as they can be used as cannon fodder to distract an enemy fleet. The advantage of these ships is that they will regenerate assuming the carrier survives the battle. Drones are also useful as a counter to the larger direct fire based ship designs as they will focus these powerful ships on a small drone instead of on larger prey. Drones are more vulnerable to missile based ship designs as drones cannot carry AMS (anti missile) systems. ',
'Rail Gun':'This technology will allow an Empire to equip its ships with the Light Rail Gun. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by impact armor than reflective armor. ',
'Plasma Missiles':'This technology will allow an Empire to equip its ships with the Light Plasma Missile Launcher. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by impact armor than reflective armor. ',
'Plasma Cannon':'This technology will allow an Empire to equip its ships with the Light Plasma Cannon. This weapon has a short range and require medium power to fire, but does not require ammo. It is affected more by reflective armor than impact armor. ',
'Plasma Torpedoes':'This technology will allow an Empire to equip its ships with the Light Plasma Torpedoes. This weapon has a short range and requires low power to fire, but does require ammo. It is affected more by reflective armor than impact armor. ',
'Ultra Defensive Systems':'This is a key technology which opens up defensive technologies such as anti missile systems, armor and shields for starships. On its own this technology does not enable any components however. ',
'Ultra Starship Engines':'This key technology allows ships to equip ultra engines. Engines allow a ship to move during battle, and every starship design needs at least one engine component to be considered a valid design. Engines do not affect warp capability for ships, as all ships warp at the same speed between adjacent planets or through warp gates. ',
'Ultra Rotation Thrusters':'This key technology allows ships to rotate faster during battle and every starship design needs at least one rotation component to be considered a valid design. Rotation is not as critical as Engines or Power Plants, as not as many components are needed to max out rotation on a ship. ',
'Ultra Power Plants':'This key technology allows ships to power their weapons, anti-missile guns, shields, and batteries. Every starship design needs at least one power plant component to be considered a valid design. Power plants are critical as they allow weapons and anti-missile guns to fire at a fast rate. ',
'Ultra Radar':'This technology allows a starship to equip ultra radar scanners directly on a ship design. Radar scanners are often overlooked as they do not provide a ship with any offensive or defensive advantages. They do however provide an empire with two interesting intelligence bonuses: First, a ship with radar capability that is in a battle with an enemy fleet will provide the empire the ability to click and view the enemy ship components and how they react during the entire battle. Since every battle is saved, this can be invaluable information for an empire to plan a counter fleet design for future battles. Secondly, this component adds to the scanning ability of an empire when ships with radar scanners are hovering over an enemy fleet potentially providing Intel on the planet assuming the planet does not have sufficient jamming stations. ',
'Medium Plasma Infantry':'This technology allows an empire to build medium plasma infantry regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology. ',
'Medium Plasma Mechanized':'This technology allows an empire to build medium plasma mechanized regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology ',
'Medium Plasma Artillery':'This technology allows an empire to build medium plasma artillery regiments. A medium regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Light regiments cannot be upgraded to medium or heavy regiments. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) from a new age of technology ',
'Heavy Cruisers':'This technology allows an empire to build the Heavy Cruiser Capital Ship, the next in a line of Ship-of-the-line Hull types from the plasma age. ',
'Medium Plasma Drones':'This technology allows an empire to build medium plasma drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Medium Rail Gun':'This technology allows an empire to build a medium Rail Gun, this is similar to the light Rail Gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Medium Plasma Missiles':'This technology allows an empire to build a medium Plasma Missile Launcher, this is similar to the light Plasma Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Medium Plasma Torpedoes':'This technology allows an empire to build a medium Plasma Torpedo Launcher, this is similar to the light Plasma Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Ultra StarShip Armor':'This technology does not enable any ship component, but leads to both reflective and impact armor technologies. ',
'Ultra Anti-Missile System':'This technology does not enable any ship component, but leads to both Anti Missile Technologies for AMS Rail Gun (needs ammo) and AMS Plasma Cannon (does not need ammo, but needs more power). ',
'Ultra Engineering Stations':'This technology is often overlooked by starting empires, but can be quite powerful for more complicated empires with a larger demand of logistics around ship construction, repair and upgrades. These components can only be built on the platform hull type limiting them to orbit friendly empires, however, it does allow for an empire to build a mobile shipyard. When a platform design includes engineering stations of any great quantity that platform once constructed will allow any friendly planet that the platform orbits to act as if it had a shipyard constructed. The advantages of this arrangement are that the shipyards are now mobile and can follow a friendly fleet for easy repair and upgrade as well as ship construction. Planets will also not have to use cities to populate the shipyards, so they can be allocated to other industries. The disadvantage is that resources will have to follow the mobile shipyard through trade routes that will have to modify over time, the mobile shipyards are vulnerable to a fleet attack as they are not situated as part of the planet\'s infrastructure, and the mobile shipyard is considered a ship and therefore will require upkeep costs every round in the form of credits to its crew. ',
'Ultra Starship Batteries':'This powerful technology allows a starship design to have a backup of stored energy that is filled by free power plant energy when not being used by other components. Starship batteries greatly increase the power of shields and Anti-Missile components, and are especially effective on larger ships that have the component space to combine AMS with Large weapons, targeting computers, and shields. It is recommended that this advanced technology is tested well when doing ship design and ship simulation to truly unlock its power in a well-designed medium to large capital ship class. ',
'Heavy Plasma Infantry':'This technology allows an empire to build heavy plasma infantry regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Plasma Mechanized':'This technology allows an empire to build heavy plasma mechanized regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Heavy Plasma Artillery':'This technology allows an empire to build heavy plasma artillery regiments. A heavy regiment has more power and better odds of surviving battle then a lighter regiment, and does not cost any more to construct making this technology quite valuable to an expanding empire. Regiments can only be upgraded from the same weight class (light to light) (medium to medium) (heavy to heavy) from a new age of technology ',
'Battle Cruisers':'This Technology allows for the construction of Battle Cruisers, the third and final cruiser class Ship-of-the line hull type. ',
'Battle Carriers':'This Technology allows for the construction of the largest Carrier Hull type ',
'Heavy Plasma Drones':'This technology allows an empire to build heavy plasma drones which are larger drones capable of carrying larger weapons and shields/armor. ',
'Heavy Rail Gun':'This technology allows an empire to build a Heavy Rail Gun, this is similar to the medium Rail gun, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Plasma Missiles':'This technology allows an empire to build a Heavy Plasma Missile Launcher, this is similar to the medium Plasma Missile Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Heavy Plasma Cannon':'This technology allows an empire to build a Heavy Plasma Cannon, this is similar to the medium Plasma Cannon, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship.  ',
'Heavy Plasma Torpedoes':'This technology allows an empire to build a Heavy Plasma Torpedo Launcher, this is similar to the Medium Plasma Torpedo Launcher, but has a longer range, does more damage, requires more power, and takes longer to target an enemy ship. ',
'Ultra Impact Armor':'This technology allows an empire to equip its ships with ultra impact armor. Impact armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to impact based weapon hits. Impact armor cannot mix with reflective armor in the same ship quadrant. ',
'Ultra Reflective Armor':'This technology allows an empire to equip its ships with ultra reflective armor. Reflective armor provides protection to a quadrant of a ship, and while active will translate 50 percent damage reduction to energy based weapon hits. Reflective armor cannot mix with impact armor in the same ship quadrant. ',
'Ultra Starship Shields':'This technology allows an empire to equip its ships with ultra starship shield components. These components provide a ship with a regenerating shield protection, and combines well with ship batteries. ',
'Ultra Targeting Computers':'This technology when placed in any particular quadrant of a ship will provide any weapons or AMS systems with a lower targeting requirement, allowing ships to become more effective in offense and defense (from missile attack). When using targeting computers notice the weapon lock time (in brackets) will go down. Try to match this time to the overall power recharge time, and use simulations to see the ship design in action to make sure power requirements match targeting requirements for a ship design. ',
'Dreadnoughts':'This powerful technology allows an empire to build the first of two super-capital ship hull types, the dreadnought. ',
'Super Dreadnoughts':'This ultimate technology allows an empire to build the largest super-capital ship hull type, the super-dreadnought. ',
'AMS Rail Gun':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Rail Gun requires ammo, but takes less power. ',
'AMS Plasma Cannon':'This technology allows an empire to equip its ships with Anti-Missile-Systems or (AMS). These defensive guns are critical to protect a ship from incoming missile fire. Since missiles lock onto targets until they are destroyed AMS systems are critical to protect a ship from a large volley of incoming missiles or torpedoes. The AMS Plasma Cannon does not requires ammo, but takes more power. ',
'Ultra Jamming':'This technology allows a ship design to build the Ultra Jamming Dishes component. This component does not affect a ships combat abilities, however it is a powerful tool as part of a larger fleet as it does two primary tasks: First, it can jam the radar scans of an enemy fleet during battle, making it more difficult for an enemy player to understand how the ship designs work for an empire\'s fleet. Second, it can jam the details of a fleet from the planetary level, and consequently also jam any information about a planet as the ships jamming will support the jamming at the planet level as well, if the ships with jamming components happen to be orbiting a friendly planet. ',
'Capital Ship Drives':'This special Plasma Age technology allows an empire to build the ultra-advanced Capital ship drives. These drives greatly increase the engine power for capital ships, allowing them to free up a large number of components for more offensive and defensive components, making them much more powerful. '
}






