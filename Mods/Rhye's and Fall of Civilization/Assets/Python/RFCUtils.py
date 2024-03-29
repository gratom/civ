# Rhye's and Fall of Civilization - Utilities

from CvPythonExtensions import *
import CvUtil
import PyHelpers
import Consts as con
import pickle

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer


iNumPlayers = con.iNumPlayers
iNumMajorPlayers = con.iNumMajorPlayers
iNumActivePlayers = con.iNumActivePlayers
iIndependent = con.iIndependent
iIndependent2 = con.iIndependent2
iNumTotalPlayers = con.iNumTotalPlayers
iBarbarian = con.iBarbarian

iSettler = con.iSettler

iNumBuildingsPlague = con.iNumBuildingsPlague
iNumBuildingsEmbassy = con.iNumBuildingsEmbassy

tCol = (
'255,255,255',
'200,200,200',
'150,150,150',
'128,128,128')

class RFCUtils:

        #Rise and fall, stability
        def getLastTurnAlive( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLastTurnAlive'][iCiv]

        def setLastTurnAlive( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lLastTurnAlive'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #Victory
        def getGoal( self, i, j ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGoals'][i][j]

        def setGoal( self, i, j, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGoals'][i][j] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #Stability
        
        def getTempFlippingCity( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['tempFlippingCity']

        def setTempFlippingCity( self, tNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['tempFlippingCity'] = tNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) ) 

        def getStability( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStability'][iCiv]

        def setStability( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStability'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getBaseStabilityLastTurn( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lBaseStabilityLastTurn'][iCiv]

        def setBaseStabilityLastTurn( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lBaseStabilityLastTurn'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getStabilityParameters( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lStabilityParameters'][iParameter]

        def setStabilityParameters( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lStabilityParameters'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        def getGreatDepressionCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lGreatDepressionCountdown'][iCiv]

        def setGreatDepressionCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lGreatDepressionCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                                
        def getLastRecordedStabilityStuff( self, iParameter ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lLastRecordedStabilityStuff'][iParameter]

        def setLastRecordedStabilityStuff( self, iParameter, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lLastRecordedStabilityStuff'][iParameter] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )
                
        #Plague
        def getPlagueCountdown( self, iCiv ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['lPlagueCountdown'][iCiv]

        def setPlagueCountdown( self, iCiv, iNewValue ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                scriptDict['lPlagueCountdown'][iCiv] = iNewValue
                gc.getGame().setScriptData( pickle.dumps(scriptDict) )

        #Communications
        def getSeed( self ):
                scriptDict = pickle.loads( gc.getGame().getScriptData() )
                return scriptDict['iSeed']

#######################################

        #Stability, RiseNFall, CvFinanceAdvisor
        def setParameter(self, iPlayer, iParameter, bPreviousAmount, iAmount):
            if (gc.getPlayer(iPlayer).isHuman()):
                    if (bPreviousAmount):
                            self.setStabilityParameters(iParameter, self.getStabilityParameters(iParameter) + iAmount)
                    else:
                            self.setStabilityParameters(iParameter, 0 + iAmount)

        #CvFinanceAdvisor
        def getParCities(self):
            if (self.getStabilityParameters(con.iParCitiesE) > 7):
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParCitiesE) < -7):
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParCities3) + self.getStabilityParameters(con.iParCitiesE)

        def getParCivics(self):
            if (self.getStabilityParameters(con.iParCivicsE) > 7):
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParCivicsE) < -7):
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParCivics3) + self.getStabilityParameters(con.iParCivics1) + self.getStabilityParameters(con.iParCivicsE)

        def getParDiplomacy(self):
            if (self.getStabilityParameters(con.iParDiplomacyE) > 7):
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParDiplomacyE) < -7):
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParDiplomacy3) + self.getStabilityParameters(con.iParDiplomacyE)

                
        def getParEconomy(self):
            #print ("ECO", self.getStabilityParameters(con.iParEconomy3), self.getStabilityParameters(con.iParEconomy1), self.getStabilityParameters(con.iParEconomyE))
            if (self.getStabilityParameters(con.iParEconomyE) > 7):
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParEconomyE) < -7):
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParEconomy3) + self.getStabilityParameters(con.iParEconomy1) + self.getStabilityParameters(con.iParEconomyE)
                
        def getParExpansion(self):
            if (self.getStabilityParameters(con.iParExpansionE) > 7):
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) - gc.getActivePlayer().getCurrentEra()
            elif (self.getStabilityParameters(con.iParExpansionE) < -7):
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE) + gc.getActivePlayer().getCurrentEra()
            else:
                    return self.getStabilityParameters(con.iParExpansion3) + self.getStabilityParameters(con.iParExpansion1) + self.getStabilityParameters(con.iParExpansionE)

        def getArrow(self, iParameter):
            if (iParameter == 0):
                    if (self.getStability(self.getHumanID()) >= self.getLastRecordedStabilityStuff(iParameter) + 6):
                            return 1
                    elif (self.getStability(self.getHumanID()) <= self.getLastRecordedStabilityStuff(iParameter) - 6):
                            return -1
                    else:
                            return 0
            else:
                    if (iParameter == 1):
                            iNewValue = self.getParCities()
                    elif (iParameter == 2):
                            iNewValue = self.getParCivics()
                    elif (iParameter == 3):
                            iNewValue = self.getParEconomy()
                    elif (iParameter == 4):
                            iNewValue = self.getParExpansion()
                    elif (iParameter == 5):
                            iNewValue = self.getParDiplomacy()
                    if (iNewValue >= self.getLastRecordedStabilityStuff(iParameter) + 4):
                            return 1
                    elif (iNewValue <= self.getLastRecordedStabilityStuff(iParameter) - 4):
                            return -1
                    else:
                            return 0

        #Victory
        def countAchievedGoals(self, iPlayer):
                iResult = 0
                for j in range(3):                        
                        #iTemp = self.getGoal(iPlayer, j)
                        #if (iTemp < 0):
                        #        iTemp = 0
                        #iResult += iTemp
                        if (self.getGoal(iPlayer, j) == 1):
                                iResult += 1
                return iResult
                
        def getGoalsColor(self, iPlayer): #by CyberChrist
                iCol = 0
                for j in range(3):
                        if (self.getGoal(iPlayer, j) == 0):
                                iCol += 1
                return tCol[iCol]

            
        #Plague
        def getRandomCity(self, iPlayer):
                cityList = []
                apCityList = PyPlayer(iPlayer).getCityList()
                for pCity in apCityList:
                        cityList.append(pCity.GetCy())
                if (len(cityList)):           
                        return cityList[gc.getGame().getSorenRandNum(len(cityList), 'random city')]
                else:
                        return -1                   
                                            

        def isMortalUnit(self, unit):
                if (unit.isHasPromotion(42)): #leader
                        if (not gc.getPlayer(unit.getOwner()).isHuman()):
                                return False
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 50):
                                        return False              
                iUnitType = unit.getUnitType()
                if (iUnitType <= con.iKhmerBallistaElephant \
                     and iUnitType != con.iSettler and iUnitType != con.iMechanizedInfantry):
                        return True
                if (iUnitType >= con.iCatapult and iUnitType <= con.iMobileArtillery ):
                        if (gc.getPlayer(unit.getOwner()).isHuman()):
                                return True
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 30):
                                        return True
                if (iUnitType == con.iSettler ):
                        if (gc.getPlayer(unit.getOwner()).isHuman()):
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 50):
                                        return True
                        else:
                                if (gc.getGame().getSorenRandNum(100, 'random modifier') >= 20):
                                        return True
                return False

        def isDefenderUnit(self, unit):
                iUnitType = unit.getUnitType()
                if (iUnitType >= con.iSpearman and iUnitType <= con.iChinaChokonu):
                        return True
                return False

        #AIWars
        def checkUnitsInEnemyTerritory(self, iCiv1, iCiv2): 
                unitList = PyPlayer(iCiv1).getUnitList()
                if(len(unitList)):
                        for unit in unitList:
                                iX = unit.getX()
                                iY = unit.getY()
                                if (gc.getMap().plot( iX, iY ).getOwner() == iCiv2):
                                        return True
                return False

        #AIWars
        def restorePeaceAI(self, iMinorCiv, bOpenBorders):
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                for iActiveCiv in range( iNumActivePlayers ):
                        if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
                                if (teamMinor.isAtWar(iActiveCiv)):
                                        bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
                                        bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)                                                                  
                                        if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):            
                                                teamMinor.makePeace(iActiveCiv)
                                                if (bOpenBorders):
                                                        teamMinor.signOpenBorders(iActiveCiv)
        #AIWars
        def restorePeaceHuman(self, iMinorCiv, bOpenBorders): 
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                for iActiveCiv in range( iNumActivePlayers ):
                        if (gc.getPlayer(iActiveCiv).isHuman()):
                                if (gc.getPlayer(iActiveCiv).isAlive()):
                                        if (teamMinor.isAtWar(iActiveCiv)):
                                                bActiveUnitsInIndependentTerritory = self.checkUnitsInEnemyTerritory(iActiveCiv, iMinorCiv)
                                                bIndependentUnitsInActiveTerritory = self.checkUnitsInEnemyTerritory(iMinorCiv, iActiveCiv)                                                                  
                                                if (not bActiveUnitsInIndependentTerritory and not bIndependentUnitsInActiveTerritory):            
                                                        teamMinor.makePeace(iActiveCiv)
                                return
        #AIWars
        def minorWars(self, iMinorCiv):
                teamMinor = gc.getTeam(gc.getPlayer(iMinorCiv).getTeam())
                apCityList = PyPlayer(iMinorCiv).getCityList()
                for pCity in apCityList:
                        city = pCity.GetCy()
                        x = city.getX()
                        y = city.getY()
                        for iActiveCiv in range( iNumActivePlayers ):
                                if (gc.getPlayer(iActiveCiv).isAlive() and not gc.getPlayer(iActiveCiv).isHuman()):
                                        if (gc.getPlayer(iActiveCiv).getSettlersMaps( 67-y, x ) >= 90):
                                                if (not teamMinor.isAtWar(iActiveCiv)):
                                                        teamMinor.declareWar(iActiveCiv, False, WarPlanTypes.WARPLAN_LIMITED)
                                                        print ("Minor war", city.getName(), gc.getPlayer(iActiveCiv).getCivilizationAdjective(0))



            
        #RiseAndFall, Stability
        def calculateDistance(self, x1, y1, x2, y2):
                dx = abs(x2-x1)
                dy = abs(y2-y1)
                return max(dx, dy)


            
        #RiseAndFall
        def debugTextPopup(self, strText):
                popup = Popup.PyPopup()
                popup.setBodyString( strText )
                popup.launch()		

        #RiseAndFall
        def updateMinorTechs( self, iMinorCiv, iMajorCiv):                
                for t in range(con.iNumTechs):
                        if (gc.getTeam(gc.getPlayer(iMajorCiv).getTeam()).isHasTech(t)):
                                    gc.getTeam(gc.getPlayer(iMinorCiv).getTeam()).setHasTech(t, True, iMinorCiv, False, False)


        #RiseAndFall, Religions, Congresses, UniquePowers
        def makeUnit(self, iUnit, iPlayer, tCoords, iNum): #by LOQ
                'Makes iNum units for player iPlayer of the type iUnit at tCoords.'
                for i in range(iNum):
                        player = gc.getPlayer(iPlayer)
                        player.initUnit(iUnit, tCoords[0], tCoords[1], UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

        #RiseAndFall, Religions, Congresses
        def getHumanID(self):
##                for iCiv in range(iNumPlayers):
##                        if (gc.getPlayer(iCiv).isHuman()):
##                                return iCiv     
                return gc.getGame().getActivePlayer()



        #RiseAndFall
        def flipUnitsInCityBefore(self, tCityPlot, iNewOwner, iOldOwner):
                #print ("tCityPlot Before", tCityPlot)
                plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = plotCity.getPlotCity()    
                iNumUnitsInAPlot = plotCity.getNumUnits()
                j = 0
                for i in range(iNumUnitsInAPlot):                        
                        unit = plotCity.getUnit(j)
                        unitType = unit.getUnitType()
                        if (unit.getOwner() == iOldOwner):
                                unit.kill(False, con.iBarbarian)
                                if (iNewOwner < con.iNumActivePlayers or unitType > con.iSettler):
                                        self.makeUnit(unitType, iNewOwner, [0, 67], 1)
                        else:
                                j += 1
        #RiseAndFall
        def flipUnitsInCityAfter(self, tCityPlot, iCiv):
                #moves new units back in their place
                print ("tCityPlot After", tCityPlot)
                tempPlot = gc.getMap().plot(0,67)
                if (tempPlot.getNumUnits() != 0):
                        iNumUnitsInAPlot = tempPlot.getNumUnits()
                        #print ("iNumUnitsInAPlot", iNumUnitsInAPlot)                        
                        for i in range(iNumUnitsInAPlot):
                                unit = tempPlot.getUnit(0)
                                unit.setXYOld(tCityPlot[0],tCityPlot[1])
                #cover plots revealed
                gc.getMap().plot(0, 67).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(0, 66).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(1, 66).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(1, 67).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(123, 67).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(123, 66).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 67).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 66).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(2, 65).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(1, 65).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(0, 65).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(122, 67).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(122, 66).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(122, 65).setRevealed(iCiv, False, True, -1);
                gc.getMap().plot(123, 65).setRevealed(iCiv, False, True, -1);

        def killUnitsInArea(self, tTopLeft, tBottomRight, iCiv):
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                killPlot = gc.getMap().plot(x,y)
                                iNumUnitsInAPlot = killPlot.getNumUnits()
                                if (iNumUnitsInAPlot):
                                        for i in range(iNumUnitsInAPlot):                                                        
                                                unit = killPlot.getUnit(0)
                                                if (unit.getOwner() == iCiv):
                                                        unit.kill(False, con.iBarbarian)

                                                        
        #RiseAndFall
        def flipUnitsInArea(self, tTopLeft, tBottomRight, iNewOwner, iOldOwner, bSkipPlotCity, bKillSettlers):
                """Deletes, recreates units in 0,67 and moves them to the previous tile.
                If there are units belonging to others in that plot and the new owner is barbarian, the units aren't recreated.
                Settlers aren't created.
                If bSkipPlotCity is True, units in a city won't flip. This is to avoid converting barbarian units that would capture a city before the flip delay"""
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                killPlot = gc.getMap().plot(x,y)
                                iNumUnitsInAPlot = killPlot.getNumUnits()
                                if (iNumUnitsInAPlot):
                                        bRevealedZero = False
                                        if (gc.getMap().plot(0, 67).isRevealed(iNewOwner, False)):
                                                bRevealedZero = True
                                        #print ("killplot", x, y)
                                        if (bSkipPlotCity == True) and (killPlot.isCity()):
                                                #print (killPlot.isCity())
                                                #print 'do nothing'
                                                pass
                                        else:
                                                j = 0
                                                for i in range(iNumUnitsInAPlot):                                                        
                                                        unit = killPlot.getUnit(j)
                                                        #print ("killplot", x, y, unit.getUnitType(), unit.getOwner(), "j", j)
                                                        if (unit.getOwner() == iOldOwner):
                                                                unit.kill(False, con.iBarbarian)
                                                                if (bKillSettlers):
                                                                        if ((unit.getUnitType() > iSettler)):
                                                                                self.makeUnit(unit.getUnitType(), iNewOwner, [0, 67], 1)
                                                                else:
                                                                        if ((unit.getUnitType() >= iSettler)): #skip animals
                                                                                self.makeUnit(unit.getUnitType(), iNewOwner, [0, 67], 1)
                                                        else:
                                                                j += 1
                                                tempPlot = gc.getMap().plot(0,67)
                                                #moves new units back in their place
                                                if (tempPlot.getNumUnits() != 0):
                                                        iNumUnitsInAPlot = tempPlot.getNumUnits()
                                                        for i in range(iNumUnitsInAPlot):
                                                                unit = tempPlot.getUnit(0)
                                                                unit.setXYOld(x,y)
                                                        iCiv = iNewOwner
                                                        if (bRevealedZero == False):
                                                                gc.getMap().plot(0, 67).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(0, 66).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(1, 66).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(1, 67).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(123, 67).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(123, 66).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 67).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 66).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(2, 65).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(1, 65).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(0, 65).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(122, 67).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(122, 66).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(122, 65).setRevealed(iCiv, False, True, -1);
                                                                gc.getMap().plot(123, 65).setRevealed(iCiv, False, True, -1);
                                




        #Congresses, RiseAndFall
        def flipCity(self, tCityPlot, bFlipType, bKillUnits, iNewOwner, iOldOwners):
                """Changes owner of city specified by tCityPlot.
                bFlipType specifies if it's conquered or traded.
                If bKillUnits != 0 all the units in the city will be killed.
                iRetainCulture will determine the split of the current culture between old and new owner. -1 will skip
                iOldOwners is a list. Flip happens only if the old owner is in the list.
                An empty list will cause the flip to always happen."""
                pNewOwner = gc.getPlayer(iNewOwner)
                city = gc.getMap().plot(tCityPlot[0], tCityPlot[1]).getPlotCity()
                if (gc.getMap().plot(tCityPlot[0], tCityPlot[1]).isCity()):
                        if not city.isNone():
                                iOldOwner = city.getOwner()
                                if (iOldOwner in iOldOwners or not iOldOwners):

                                        if (bKillUnits):
                                                killPlot = gc.getMap().plot( tCityPlot[0], tCityPlot[1] )
                                                for i in range(killPlot.getNumUnits()):
                                                        unit = killPlot.getUnit(0)
                                                        unit.kill(False, iNewOwner)
                                                        
                                        if (bFlipType): #conquest
                                                if (city.getPopulation() == 2):
                                                        city.setPopulation(3)
                                                if (city.getPopulation() == 1):
                                                        city.setPopulation(2)
                                                pNewOwner.acquireCity(city, True, False)
                                        else: #trade
                                                pNewOwner.acquireCity(city, False, True)
                                                
                                        return True
                return False


        #Congresses, RiseAndFall
        def cultureManager(self, tCityPlot, iCulturePercent, iNewOwner, iOldOwner, bBarbarian2x2Decay, bBarbarian2x2Conversion, bAlwaysOwnPlots):
                """Converts the culture of the city and of the surrounding plots to the new owner of a city.
                iCulturePercent determine the percentage that goes to the new owner.
                If old owner is barbarian, all the culture is converted"""

                pCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = pCity.getPlotCity()                

                #city
                if (pCity.isCity()):
                        iCurrentCityCulture = city.getCulture(iOldOwner)
                        city.setCulture(iOldOwner, iCurrentCityCulture*(100-iCulturePercent)/100, False)
                        if (iNewOwner != con.iBarbarian):
                                city.setCulture(con.iBarbarian, 0, True)
                        city.setCulture(iNewOwner, iCurrentCityCulture*iCulturePercent/100, False)
                        if (city.getCulture(iNewOwner) <= 10):
                                city.setCulture(iNewOwner, 20, False)

                #halve barbarian culture in a broader area
                if (bBarbarian2x2Decay or bBarbarian2x2Conversion):
                        if (iNewOwner != con.iBarbarian and iNewOwner != con.iIndependent and iNewOwner != con.iIndependent2):
                                for x in range(tCityPlot[0]-2, tCityPlot[0]+3):        # from x-2 to x+2
                                        for y in range(tCityPlot[1]-2, tCityPlot[1]+3):	# from y-2 to y+2                                
                                                iPlotBarbCulture = gc.getMap().plot(x, y).getCulture(con.iBarbarian)
                                                if (iPlotBarbCulture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iBarbarian, iPlotBarbCulture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iBarbarian, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotBarbCulture, True)
                                                iPlotIndependentCulture = gc.getMap().plot(x, y).getCulture(con.iIndependent)
                                                if (iPlotIndependentCulture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent, iPlotIndependentCulture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependentCulture, True)
                                                iPlotIndependent2Culture = gc.getMap().plot(x, y).getCulture(con.iIndependent2)
                                                if (iPlotIndependent2Culture > 0):
                                                        if (gc.getMap().plot(x, y).getPlotCity().isNone() or (x==tCityPlot[0] and y==tCityPlot[1])):
                                                                if (bBarbarian2x2Decay):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent2, iPlotIndependent2Culture/4, True)
                                                                if (bBarbarian2x2Conversion):
                                                                        gc.getMap().plot(x, y).setCulture(con.iIndependent2, 0, True)
                                                                        gc.getMap().plot(x, y).setCulture(iNewOwner, iPlotIndependent2Culture, True)
                                                                        
                #plot                               
                for x in range(tCityPlot[0]-1, tCityPlot[0]+2):        # from x-1 to x+1
                        for y in range(tCityPlot[1]-1, tCityPlot[1]+2):	# from y-1 to y+1
                                pCurrent = gc.getMap().plot(x, y)
                                
                                iCurrentPlotCulture = pCurrent.getCulture(iOldOwner)

                                if (pCurrent.isCity()):                                
                                        pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/100, True)
                                        pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent)/100, True)
                                else:
                                        pCurrent.setCulture(iNewOwner, iCurrentPlotCulture*iCulturePercent/3/100, True)
                                        pCurrent.setCulture(iOldOwner, iCurrentPlotCulture*(100-iCulturePercent/3)/100, True)

                                #cut other players culture
##                                for iCiv in range(iNumPlayers):
##                                        if (iCiv != iNewOwner and iCiv != iOldOwner):
##                                                iPlotCulture = gc.getMap().plot(x, y).getCulture(iCiv)
##                                                if (iPlotCulture > 0):
##                                                        gc.getMap().plot(x, y).setCulture(iCiv, iPlotCulture/3, True)
                                                        
                                #print (x, y, pCurrent.getCulture(iNewOwner), ">", pCurrent.getCulture(iOldOwner))

                                if (not pCurrent.isCity()):
                                        if (bAlwaysOwnPlots):
                                                pCurrent.setOwner(iNewOwner)
                                        else:
                                                if (pCurrent.getCulture(iNewOwner)*4 > pCurrent.getCulture(iOldOwner)):
                                                        pCurrent.setOwner(iNewOwner)                                        
                                        #print ("NewOwner", pCurrent.getOwner())



        #handler
        def spreadMajorCulture(self, iMajorCiv, iX, iY):                
                for x in range(iX-4, iX+5):        # from x-4 to x+4
                        for y in range(iY-4, iY+5):	# from y-4 to y+4
                                pCurrent = gc.getMap().plot(x, y)
                                if (pCurrent.isCity()):
                                        city = pCurrent.getPlotCity()
                                        if (city.getOwner() >= iNumMajorPlayers):
                                                iMinor = city.getOwner()
                                                iDen = 25
                                                if (gc.getPlayer(iMajorCiv).getSettlersMaps( 67-y, x ) >= 400):
                                                        iDen = 10
                                                elif (gc.getPlayer(iMajorCiv).getSettlersMaps( 67-y, x ) >= 150):
                                                        iDen = 15
                                                        
                                                iMinorCityCulture = city.getCulture(iMinor)
                                                city.setCulture(iMajorCiv, iMinorCityCulture/iDen, True)
                                                
                                                iMinorPlotCulture = pCurrent.getCulture(iMinor)
                                                pCurrent.setCulture(iMajorCiv, iMinorPlotCulture/iDen, True)                                

        #UniquePowers
        def convertPlotCulture(self, pCurrent, iCiv, iPercent, bOwner):
                
                if (pCurrent.isCity()):
                        city = pCurrent.getPlotCity()
                        iCivCulture = city.getCulture(iCiv)
                        iLoopCivCulture = 0
                        for iLoopCiv in range(iNumTotalPlayers):
                                if (iLoopCiv != iCiv):
                                        iLoopCivCulture += city.getCulture(iLoopCiv)                                
                                        city.setCulture(iLoopCiv, city.getCulture(iLoopCiv)*(100-iPercent)/100, True)
                        city.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)  
        
##                for iLoopCiv in range(iNumTotalPlayers):
##                        if (iLoopCiv != iCiv):
##                                iLoopCivCulture = pCurrent.getCulture(iLoopCiv)
##                                iCivCulture = pCurrent.getCulture(iCiv)
##                                pCurrent.setCulture(iLoopCiv, iLoopCivCulture*(100-iPercent)/100, True)
##                                pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture*iPercent/100, True)
                iCivCulture = pCurrent.getCulture(iCiv)
                iLoopCivCulture = 0
                for iLoopCiv in range(iNumTotalPlayers):
                        if (iLoopCiv != iCiv):
                                iLoopCivCulture += pCurrent.getCulture(iLoopCiv)                                
                                pCurrent.setCulture(iLoopCiv, pCurrent.getCulture(iLoopCiv)*(100-iPercent)/100, True)
                pCurrent.setCulture(iCiv, iCivCulture + iLoopCivCulture, True)                                
                if (bOwner == True):
                        pCurrent.setOwner(iCiv)



                                




        #Congresses, RiseAndFall
        def pushOutGarrisons(self, tCityPlot, iOldOwner):
                tDestination = (-1, -1)
                for x in range(tCityPlot[0]-2, tCityPlot[0]+3):
                        for y in range(tCityPlot[1]-2, tCityPlot[1]+3):
                                pDestination = gc.getMap().plot(x, y)
                                if (pDestination.getOwner() == iOldOwner and (not pDestination.isWater()) and (not pDestination.isImpassable())):
                                        tDestination = (x, y)
                                        break
                                        break
                if (tDestination != (-1, -1)):
                        plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                        iNumUnitsInAPlot = plotCity.getNumUnits()
                        j = 0
                        for i in range(iNumUnitsInAPlot):                        
                                unit = plotCity.getUnit(j)
                                if (unit.getDomainType() == 2): #land unit
                                        unit.setXYOld(tDestination[0], tDestination[1])
                                else:
                                        j = j + 1
                                
        #Congresses, RiseAndFall
        def relocateSeaGarrisons(self, tCityPlot, iOldOwner):
                tDestination = (-1, -1)
                cityList = PyPlayer(iOldOwner).getCityList()
                for pyCity in cityList:
                        if (pyCity.GetCy().isCoastalOld()):
                                tDestination = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                if (tDestination == (-1, -1)):                    
                        for x in range(tCityPlot[0]-12, tCityPlot[0]+12):
                                for y in range(tCityPlot[1]-12, tCityPlot[1]+12):
                                        pDestination = gc.getMap().plot(x, y)
                                        if (pDestination.isWater()):
                                                tDestination = (x, y)
                                                break
                                                break
                if (tDestination != (-1, -1)):
                        plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                        iNumUnitsInAPlot = plotCity.getNumUnits()
                        j = 0
                        for i in range(iNumUnitsInAPlot):
                                unit = plotCity.getUnit(j)
                                if (unit.getDomainType() == 0): #sea unit
                                        unit.setXYOld(tDestination[0], tDestination[1])
                                else:
                                        j = j + 1


        #Congresses, RiseAndFall
        def createGarrisons(self, tCityPlot, iNewOwner, iNumUnits):
                plotCity = gc.getMap().plot(tCityPlot[0], tCityPlot[1])
                city = plotCity.getPlotCity()    
                iNumUnitsInAPlot = plotCity.getNumUnits()
                pCiv = gc.getPlayer(iNewOwner)

                if (gc.getTeam(pCiv.getTeam()).isHasTech(con.iAssemblyLine) and gc.getTeam(pCiv.getTeam()).isHasTech(con.iRifling)):
                        iUnitType = con.iInfantry
                elif (gc.getTeam(pCiv.getTeam()).isHasTech(con.iRifling)):
                        if (iNewOwner != con.iEngland):
                                iUnitType = con.iRifleman
                        else:
                                iUnitType = con.iEnglishRedcoat
                elif (gc.getTeam(pCiv.getTeam()).isHasTech(con.iGunpowder)):
                        if (iNewOwner != con.iFrance):
                                iUnitType = con.iMusketman
                        else:
                                iUnitType = con.iFrenchMusketeer
                else:
                        iUnitType = con.iLongbowman

                self.makeUnit(iUnitType, iNewOwner, [tCityPlot[0], tCityPlot[1]], iNumUnits)



        #RiseAndFall, Stability

        def killCiv(self, iCiv, iNewCiv):
                self.clearPlague(iCiv)
                for pyCity in PyPlayer(iCiv).getCityList():
                        tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                        self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                        self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv]) #by trade because by conquest may raze the city
                        #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                self.flipUnitsInArea([0,0], [123,67], iNewCiv, iCiv, False, True)
                #self.killUnitsInArea([0,0], [123,67], iNewCiv, iCiv) ?
                if (iCiv < iNumMajorPlayers):
                        self.clearEmbassies(iCiv)
                self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())
                self.resetUHV(iCiv)

        def killAndFragmentCiv(self, iCiv, iNewCiv1, iNewCiv2, iNewCiv3, bAssignOneCity):
                self.clearPlague(iCiv)
                iNumLoyalCities = 0
                iCounter = gc.getGame().getSorenRandNum(6, 'random start')
                for pyCity in PyPlayer(iCiv).getCityList():
                        tCoords = (pyCity.GetCy().getX(), pyCity.GetCy().getY())
                        pCurrent = gc.getMap().plot(tCoords[0], tCoords[1])
                        #1 loyal city for the human player
                        if (bAssignOneCity and iNumLoyalCities < 1 and pyCity.GetCy().isCapital()):
                                iNumLoyalCities += 1
                                gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iNewCiv1, False, -1) #too dangerous?
                                gc.getTeam(gc.getPlayer(iCiv).getTeam()).declareWar(iNewCiv2, False, -1)
                                continue
                        #assign to neighbours first
                        bNeighbour = False
                        iRndnum = gc.getGame().getSorenRandNum(iNumPlayers, 'starting count')
                        for j in range(iRndnum, iRndnum + iNumPlayers): #only major players
                                iLoopCiv = j % iNumPlayers
                                if (gc.getPlayer(iLoopCiv).isAlive() and iLoopCiv != iCiv and not gc.getPlayer(iLoopCiv).isHuman()):
                                        if (pCurrent.getCulture(iLoopCiv) > 0):
                                                if (pCurrent.getCulture(iLoopCiv)*100 / (pCurrent.getCulture(iLoopCiv) + pCurrent.getCulture(iCiv) + pCurrent.getCulture(iBarbarian) + pCurrent.getCulture(iIndependent) + pCurrent.getCulture(iIndependent2)) >= 5): #change in vanilla
                                                        self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iLoopCiv, iCiv)                            
                                                        self.setTempFlippingCity((tCoords[0],tCoords[1]))
                                                        self.flipCity(tCoords, 0, 0, iLoopCiv, [iCiv])
                                                        #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                                                        self.flipUnitsInArea([tCoords[0]-2,tCoords[1]-2], [tCoords[0]+2,tCoords[1]-2], iLoopCiv, iCiv, False, True)
                                                        self.flipUnitsInCityAfter(self.getTempFlippingCity(), iLoopCiv)
                                                        bNeighbour = True
                                                        break
                        if (bNeighbour):
                                continue
                        #fragmentation in 2
                        if (iNewCiv3 == -1):
                                if (iCounter % 2 == 0):
                                        iNewCiv = iNewCiv1
                                elif (iCounter % 2 == 1):
                                        iNewCiv = iNewCiv2
                                self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iNewCiv, iCiv)                            
                                self.setTempFlippingCity((tCoords[0],tCoords[1]))                                                        
                                self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                                self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
                                #pyCity.GetCy().setHasRealBuilding(con.iPlague, False)  #buggy
                                self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
                                iCounter += 1
                                self.flipUnitsInArea([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1], iNewCiv, iCiv, False, True)
                        #fragmentation with barbs
                        else:
                                if (iCounter % 3 == 0):
                                        iNewCiv = iNewCiv1
                                elif (iCounter % 3 == 1):
                                        iNewCiv = iNewCiv2
                                elif (iCounter % 3 == 2):
                                        iNewCiv = iNewCiv3
                                self.flipUnitsInCityBefore((tCoords[0],tCoords[1]), iNewCiv, iCiv)                            
                                self.setTempFlippingCity((tCoords[0],tCoords[1]))         
                                self.cultureManager(tCoords, 50, iNewCiv, iCiv, False, False, False)
                                self.flipCity(tCoords, 0, 0, iNewCiv, [iCiv])
                                #pyCity.GetCy().setHasRealBuilding(con.iPlague, False) #buggy
                                self.flipUnitsInCityAfter(self.getTempFlippingCity(), iNewCiv)
                                iCounter += 1                                      
                                self.flipUnitsInArea([tCoords[0]-1,tCoords[1]-1], [tCoords[0]+1,tCoords[1]+1], iNewCiv, iCiv, False, True)
                if (bAssignOneCity == False):
                        #self.flipUnitsInArea([0,0], [123,67], iNewCiv1, iCiv, False, True) #causes a bug: if a unit was inside another city's civ, when it becomes independent or barbarian, may raze it
                        self.killUnitsInArea([0,0], [123,67], iCiv)
                        self.resetUHV(iCiv)
                if (iCiv < iNumMajorPlayers):
                        self.clearEmbassies(iCiv)
                self.setLastTurnAlive(iCiv, gc.getGame().getGameTurn())

                
        def resetUHV(self, iPlayer):
                if (iPlayer < iNumMajorPlayers):
                        if (self.getGoal(iPlayer, 0) == -1):
                                self.setGoal(iPlayer, 0, 0)
                        if (self.getGoal(iPlayer, 1) == -1):
                                self.setGoal(iPlayer, 1, 0)
                        if (self.getGoal(iPlayer, 2) == -1):
                                self.setGoal(iPlayer, 2, 0)
                                                
        def clearEmbassies(self, iDeadCiv):
                for i in range (iNumTotalPlayers):
                        for pyCity in PyPlayer(i).getCityList():
                                if (pyCity.GetCy().hasBuilding(iNumBuildingsPlague + iDeadCiv)):
                                        pyCity.GetCy().setHasRealBuilding(iNumBuildingsPlague + iDeadCiv, False)
                                        continue


        def clearPlague(self, iCiv):
                for pyCity in PyPlayer(iCiv).getCityList():
                        if (pyCity.GetCy().hasBuilding(con.iPlague)):
                                pyCity.GetCy().setHasRealBuilding(con.iPlague, False)




        #AIWars, by CyberChrist

        def isNoVassal(self, iCiv):
                iMaster = 0
                for iMaster in range (iNumTotalPlayers):
                        if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster)):
                                return False
                return True

        def isAVassal(self, iCiv):
                iMaster = 0
                for iMaster in range (iNumTotalPlayers):
                        if (gc.getTeam(gc.getPlayer(iCiv).getTeam()).isVassal(iMaster)):
                                return True
                return False

        #Barbs, RiseAndFall
        def squareSearch( self, tTopLeft, tBottomRight, function, argsList ): #by LOQ
                """Searches all tile in the square from tTopLeft to tBottomRight and calls function for
                every tile, passing argsList. The function called must return a tuple: (1) a result, (2) if
                a plot should be painted and (3) if the search should continue."""
                tPaintedList = []
                result = None
                for x in range(tTopLeft[0], tBottomRight[0]+1):
                        for y in range(tTopLeft[1], tBottomRight[1]+1):
                                result, bPaintPlot, bContinueSearch = function((x, y), result, argsList)
                                if bPaintPlot:			# paint plot
                                        tPaintedList.append((x, y))
                                if not bContinueSearch:		# goal reached, so stop
                                        return result, tPaintedList
                return result, tPaintedList

        #Barbs, RiseAndFall
        def outerInvasion( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        if (pCurrent.countTotalCulture() == 0 ):
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #Barbs
        def innerSeaSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's water and it isn't occupied by any unit. Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isWater()):
                        if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                iClean = 0
                                for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                        for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                if (pCurrent.getNumUnits() != 0):
                                                        iClean += 1
                                if ( iClean == 0 ):   
                                        # this is a good plot, so paint it and continue search
                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #Barbs
        def outerSeaSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's water and it isn't occupied by any unit and if it isn't a civ's territory. Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isWater()):
                        if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                if (pCurrent.countTotalCulture() == 0 ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):   
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #Barbs
        def outerSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory.
                Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):
                                                if (pCurrent.countTotalCulture() == 0 ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)                                        

        #RiseAndFall
        def innerInvasion( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        if (pCurrent.getOwner() in argsList ):
                                                # this is a good plot, so paint it and continue search
                                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)
            
        def innerSpawn( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't marsh or jungle, it isn't occupied by a unit or city and if it isn't a civ's territory"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                        iClean = 0
                                        for x in range(tCoords[0] - 1, tCoords[0] + 2):        # from x-1 to x+1
                                                for y in range(tCoords[1] - 1, tCoords[1] + 2):	# from y-1 to y+1
                                                        if (pCurrent.getNumUnits() != 0):
                                                                iClean += 1
                                        if ( iClean == 0 ):  
                                                if (pCurrent.getOwner() in argsList ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #RiseAndFall
        def goodPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands, it isn't desert, tundra, marsh or jungle; it isn't occupied by a unit or city and if it isn't a civ's territory.
                Unit check extended to adjacent plots"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if ( not pCurrent.isImpassable()):
                                if ( not pCurrent.isUnit() ):
                                        if (pCurrent.getTerrainType() != con.iDesert) and (pCurrent.getTerrainType() != con.iTundra) and (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                                if (pCurrent.countTotalCulture() == 0 ):
                                                        # this is a good plot, so paint it and continue search
                                                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        #RiseAndFall
        def ownedCityPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it contains a city belonging to the civ"""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if (pCurrent.getOwner() == argsList ):
                        if (pCurrent.isCity()):
                                # this is a good plot, so paint it and continue search
                                return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue) 

        def ownedPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it is in civ's territory."""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if (pCurrent.getOwner() == argsList ):
                        # this is a good plot, so paint it and continue search
                        return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)

        def goodOwnedPlots( self, tCoords, result, argsList ):
                """Checks validity of the plot at the current tCoords, returns plot if valid (which stops the search).
                Plot is valid if it's hill or flatlands; it isn't marsh or jungle, it isn't occupied by a unit and if it is in civ's territory."""
                bPaint = True
                bContinue = True
                pCurrent = gc.getMap().plot( tCoords[0], tCoords[1] )
                if ( pCurrent.isHills() or pCurrent.isFlatlands() ):
                        if (pCurrent.getTerrainType() != con.iMarsh) and (pCurrent.getFeatureType() != con.iJungle):
                                if ( not pCurrent.isCity() and not pCurrent.isUnit() ):
                                            if (pCurrent.getOwner() == argsList ):
                                                    # this is a good plot, so paint it and continue search
                                                    return (None, bPaint, bContinue)
                # not a good plot, so don't paint it but continue search
                return (None, not bPaint, bContinue)
            
            
