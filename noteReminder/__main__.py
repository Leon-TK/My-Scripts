import os, sys
from time import sleep, time

import noteFetcher
import notePresence
import config as PConfig
import trigger as PTrigger
import const as PConst

#DEV: WIP
def RetrieveTriggers():
    triggers = []
    if "Repeat_Timer" in PConst.TRIGGERS:
        triggers.append(PTrigger.Repeat_Timer(600.))
    return triggers

def EnableTriggers(triggers):
    for trigger in triggers:
        trigger.Enable()

#DEV: forward slash is not tested
#DEV: need to change working directory before that line
#gConfig = PConfig.ConfigParser("config/user/config.json")

gTriggers = RetrieveTriggers()
EnableTriggers(gTriggers)

cTime: float = time()
eTime: float = time()

def changeWorkingDirectory():
    os.chdir(os.path.dirname(sys.argv[0]))
    
def updCurrentTime():
    global cTime
    cTime = time()
def updEndTime():
    global eTime
    eTime = time()
def getElapsedTime() -> float:
    global eTime
    return time() - eTime

def TickTriggers(elapsedTime):
    global gTriggers
    for trigger in gTriggers:
        trigger.Tick(elapsedTime)
def CheckIsTriggered():
    global gTriggers
    for trigger in gTriggers:
        if trigger.IsTriggered():
            return True
    return False

def ProcessTrigger():
    note = noteFetcher.fetchNote2(PConst.NOTE_DIR)
    notePresence.show(note)

def mainLoop():
    while(True):
        sleep(60.)
        bTriggered = False

        TickTriggers(getElapsedTime())
        bTriggered = CheckIsTriggered()

        if bTriggered:
            ProcessTrigger()
        
        updEndTime()

if __name__ == '__main__':
    changeWorkingDirectory()
    mainLoop()
