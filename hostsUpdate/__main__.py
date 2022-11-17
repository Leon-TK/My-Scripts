import sys
import os
from pathlib import Path
from typing import TextIO

HOSTS_FILEPATH = "C:\\Windows\\System32\\drivers\\etc\\hosts"

def retrieveDnsStringFrom(ip, domain):
    return ip + ' ' + domain + '\n'

def extractIpFromArgs():
    return sys.argv[1]
def extractDnsFromArgs():
    return sys.argv[2]

def fromListToString(List: list):

    string = ''

    for index, elem in enumerate(List):
        if index == 0:
            string = elem
        else:
            string += ' ' + elem
    
    return string

def createBackupFile(file, backupPath):
    backupPath += ".backup"
    with open(backupPath, 'w') as backup:
        file.seek(0)
        backup.writelines(file.readlines())
        backup.flush()

def writeBufferIntoFile(buffer, file: TextIO):
    createBackupFile(file, HOSTS_FILEPATH)
    file.truncate()
    file.seek(0)
    file.writelines(buffer)

def processBuffer(buffer, file, cmdIpAddress, dns):

    for index, line in enumerate(buffer):
        # DNS entry exists. Changing it.
        if dns in line:
            partsOfLine  = line.split()

            if len(partsOfLine) > 2: # domain alias is here
                buffer[index] = retrieveDnsStringFrom(cmdIpAddress, fromListToString(partsOfLine[1:]))
            elif len(partsOfLine) == 2:
                buffer[index] = retrieveDnsStringFrom(cmdIpAddress, partsOfLine[1])
            
            writeBufferIntoFile(buffer, file)

            break
    # DNS entry does't exist
    else:
        buffer.append('\n')
        buffer.append(retrieveDnsStringFrom(cmdIpAddress, dns))

        writeBufferIntoFile(buffer, file)

    return

def processHostsFile(cmdIpAddress, dns):

    if not Path(HOSTS_FILEPATH).is_file():
        print("Path refereces to non file, exiting...")
        sys.exit(1)

    with open(HOSTS_FILEPATH, "r+") as hostsFile:

            fileBuffer = hostsFile.readlines()
            
            processBuffer(fileBuffer, hostsFile, cmdIpAddress, dns)

if __name__ == "__main__":

    cmdIpAddress = extractIpFromArgs()
    dns = extractDnsFromArgs()

    processHostsFile(cmdIpAddress, dns)