import sys
import re
from string import Template

"""Prints all assigned shortkeys without <unassigned> ones"""
"""Tested on 3ds max 2020"""
"""Place script into your PATH, run python -m PrintMaxHotkeys <hsx-file-path>\
    or create symbollink of python.exe with script path (or -m approach) and drag hsx file (win10)"""

#FUTURE: key value parse implementatios is trivial and not fully correct, if autodesk will change something, problems may appear. xml parser is prefered
TEMPLATE_REGEX = r"(?i:$key) *= *\"(?'value'[^\r\n\"]*)\""

def getValueSpan(shortcutIndex, line) -> tuple:
    def isBegin(quoteCount):
        return quoteCount == 1
    def isQuoteEnd(quoteCount):
        return quoteCount == 2

    begin = int()
    end = int()

    quoteCount = 0
    for count, char in enumerate(line[shortcutIndex:]):
        
        if char == "\"":
            quoteCount += 1
            if isBegin(quoteCount):
                begin = count
            if isQuoteEnd(quoteCount):
                end = count
                break
    else:
        return None
    assert(type(begin) is int and type(end) is int)
    return (begin + shortcutIndex, end + shortcutIndex)

def getValueFrom(key, line) -> str:
    shortcutIndex = line.find(key)
    begin, end = getValueSpan(shortcutIndex, line)
    return line[begin + 1 : end]

if __name__ == "__main__":
    hotkeysFilePath = sys.argv[1]

    with open(hotkeysFilePath, "r") as hotkeysFIle:
        fileBuffer = hotkeysFIle.readlines()

        for line in fileBuffer:
            if "Assign_Hotkey" in line:
                shortcutStr = getValueFrom("Shortcut", line)
                descriptionStr =  getValueFrom("Description", line)
                print(f"\"{shortcutStr}\" - {descriptionStr}")
    input()
        

