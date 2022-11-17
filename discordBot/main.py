import time 
from requests import get
from threading import Thread

import hikari

BOT_CHANNEL_ID = 988191397322563594

def getMachineIP():
    return get('https://checkip.amazonaws.com').content.decode('utf8')

class IpResolver:
    def __init__(self, bot) -> None:
        self._lastIP = ''
        self._timer = 600
        self._bot = bot
        self.bRun = True

        self._subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def _notifySubscribers(self, event, *args):
        for sub in self._subscribers:
            sub.notify(event, *args)

    def run(self):
        while(self.bRun):
            time.sleep(self.timer)
            
            if self.lastIP == '':
                self.lastIP = getMachineIP()
                return

            realIp = getMachineIP()

            if self.lastIP != realIp:
                self.lastIP = realIp
                self._notifySubscribers("ipChanged", realIp)

class MyBot():
    def __init__(self) -> None:
        self.bot = None
    def initBot(self):
        self.bot = hikari.GatewayBot(config['token'])
    
    def notify(self, event, *args):
        if event == "ipNotify":
            pass
    
    def run(self):
        self.bot.run()

    @hikari.GatewayBot.listen(hikari.GuildMessageCreateEvent)
    async def ping(event) -> None:
        if event.is_bot or not event.content:
            return

        if event.content.startswith("hk.ping"):
            await event.message.respond("Pong!")

config = {
    'token': 'OTU3MzgyNjUxOTU2ODM0MzM0.Yj9-Ew.QOYpn1rKESCxPQKd7I9xeUaFU7I',
    'prefix': '!',
}

bot = MyBot()

ipResolver = IpResolver()
ipResolver.subscribe(bot)

IpResolveThread = Thread(target=ipResolver.run) #TODO: daemon?
IpResolveThread.run()

bot.run()