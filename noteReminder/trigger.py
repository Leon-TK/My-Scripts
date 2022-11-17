import random

class ITrigger:
    def IsTriggered(self):
        pass
    def Enable(self):
        pass
    def Disable(self):
        pass

class ITickable():
    def Tick(self, deltaTime: float):
        pass

class AtStartup_Timer(ITrigger, ITickable):
    def __init__(self) -> None:
        self.bEnable = False
    def Tick(self, deltaTime: float):
        pass
    def IsTriggered(self):
        return True if self.bEnable else False
    def Enable(self):
        self.bEnable = True
    def Disable(self):
        self.bEnable = False

class OnceAfter_Timer(ITrigger, ITickable):
    def __init__(self, initialTime: float):
        self.initialTime: float = initialTime
        self.bTimeRemained: float = initialTime
        self.bEnable = False
    def Tick(self, deltaTime: float):
        if self.bEnable:
            self.bTimeRemained -= deltaTime
    def IsTriggered(self):
        if self.bEnable:
            if self.bTimeRemained < 0:
                return True
            return False
        return False
    def Enable(self):
        self.bEnable = True
    def Disable(self):
        self.bEnable = False

class OnceAfterRandom_Timer(OnceAfter_Timer):
	def __init__(self, min: float, max: float):
		OnceAfter_Timer.__init__(self, random.uniform(min, max))

class Repeat_Timer(ITrigger, ITickable):
    def __init__(self, initialTime: float):
        self.initialTime: float = initialTime
        self.bTimeRemained: float = initialTime
        self.bEnable = False
    def Tick(self, deltaTime: float):
        if self.bEnable:
            self.bTimeRemained = self.bTimeRemained - deltaTime
    def IsTriggered(self):
        if self.bEnable:
            if self.bTimeRemained < 0:
                self.bTimeRemained = self.initialTime
                return True
            return False
        return False
    def Enable(self):
        self.bEnable = True
    def Disable(self):
        self.bEnable = False

class RepeatRandom_Timer(Repeat_Timer):
	def __init__(self, min: float, max: float):
		Repeat_Timer.__init__(self, random.uniform(min, max))