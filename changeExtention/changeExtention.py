import sys, os, pathlib

#for all files in dir change extention
def changeExtentionOfFilesIn(dir, oldExt, newExt):
    for root, dirs, files in os.walk(dir):
        for file in files:
            file = pathlib.Path(root).joinpath(file)
            extentions = file.suffixes
            if len(extentions) > 0 and extentions.pop() == oldExt:
                newFileName = file.with_suffix(newExt)
                file.rename(newFileName)

    #check file extention to txt match
    #change to md
    pass

def parseCmdLine():
    
    directory = sys.argv[1]

    try: 
        oldExtention = sys.argv[2]
    except IndexError:
        oldExtention = None

    try: 
        newExtention = sys.argv[3]
    except IndexError:
        newExtention = None

    return directory, oldExtention, newExtention

if __name__ == "__main__":

    directory, oldExtention, newExtention = parseCmdLine()

    changeExtentionOfFilesIn(directory, oldExtention or '.txt', newExtention or '.md')