#Clean some garbage I dont need

import os, sys, shutil

# Deletes unnesesery files. Set 'USERNAME'

USERNAME = ""

if __name__ == "__main__":
    try:
        userName = sys.argv[1] #cmd line argument
    except IndexError:
        userName = None
        
    if userName is not None:
        USERNAME = userName
    
    dirs = f"""C:\\Users\\{USERNAME}\\AppData\\Local\\Microsoft\\vscode-cpptools
    C:\\Users\\{USERNAME}\\AppData\\Local\\notion-updater
    C:\\Users\\{USERNAME}\\AppData\\Local\\NuGet\\v3-cache
    C:\\Users\\{USERNAME}\\AppData\\Local\\NVIDIA\\GLCache
    C:\\Users\\{USERNAME}\\AppData\\Local\\NVIDIA\\DXCache
    C:\\Users\\{USERNAME}\\AppData\\Local\\pip\\cache
    C:\\Users\\{USERNAME}\\AppData\\Local\\Steam\\htmlcache
    C:\\Users\\{USERNAME}\\AppData\\Local\\Temp
    C:\\Users\\{USERNAME}\\AppData\\Local\\unityhub-updater""".split()

    for fold in dirs:
        try:
            shutil.rmtree(fold) #remove inners
            
        except FileNotFoundError:
            pass

        except PermissionError:
            for root, dirs, files in os.walk(fold):
                for file in files:
                    path = os.path.join(root, file)
                    try:
                        os.remove(path)
                    except PermissionError:
                        print(f"{path} - permission error")  
                for dir in dirs:
                    try:
                        path = os.path.join(root, dir)
                        shutil.rmtree(path)
                    except PermissionError:
                        print(f"{path} - permission error")
