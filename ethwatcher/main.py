from difflib import Match
from time import sleep
import requests
import re

REGEX_TEXT_STRING = "<div class=\"priceValue \"><span> aaa </span></div>"

REGEX = r'<div class="priceValue "><span>(?P<price> *[^\r\n] *(?:[\d\.,]*) *)</span></div>'
ENDPOINT = "https://coinmarketcap.com/currencies/ethereum/"

class RegexHandler:
    def __init__(self, regex) -> None:
        self.regex = regex
        self.compiledRegex = re.compile(self.regex)

    def searchRegexMatch(self, string):
        return self.compiledRegex.search(string)

    def extractGroup(self, group, regexMatchResult):
        return regexMatchResult.group(group)

class ResponceHandler:
    def __init__(self, endpoint) -> None:
        self.endpoint = endpoint
        
    def getResponce(self):
        return requests.get(self.endpoint)

    def decodeContentAsUTF8(self, responce):
        return responce.content.decode('utf8')

regexHandler = RegexHandler(REGEX)
responceHandler = ResponceHandler(ENDPOINT)

def tick():
    responce = responceHandler.getResponce()
    content = responceHandler.decodeContentAsUTF8(responce)
    regexResult = regexHandler.searchRegexMatch(content)
    extractedPrice = regexHandler.extractGroup('price', regexResult)
    print(extractedPrice)

def loop(sleepSeconds):
    while (True):
        tick()
        sleep(sleepSeconds)

loop(300)