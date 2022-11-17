import json
import trigger as PTrigger

class ConfigParser:
    def __init__(self, cfgPath) -> None:
        cfgFile = open(cfgPath)
        self.deserializedFile = json.load(cfgFile)
    def Parse(self):
        triggers = []
        for trigger in self.deserializedFile["Triggers"]:
            if trigger == "atStartup":
                timer = PTrigger.AtStartup_Timer()
                triggers.append(timer)
            if trigger == "onceAfterRandom":
                timer = PTrigger.OnceAfterRandom_Timer()
                triggers.append(timer)
            if trigger == "timerRandom":
                timer = PTrigger.RepeatRandom_Timer()
                triggers.append(timer)
        return triggers
        