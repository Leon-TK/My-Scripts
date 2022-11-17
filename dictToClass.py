d = {"variable1": 1, "variable2": "hello", "variable3": {"innerVar1": 2}}
#TODO: loop recursively to subtitute all dictionaries

def findDictIn(dictionary: dict) -> str|None:
    for k in d:
        if isinstance(d[k], dict):
            return k

def constructClassFromDict(dictionary: dict, name):
    return type(name, (object,), dictionary)

def subtitudeDictAsObjectIn(dictionary: dict):
    innerObjectKey = findDictIn(dictionary)
    if innerObjectKey is not None:
        cl = constructClassFromDict(d[innerObjectKey], innerObjectKey)
        del d[innerObjectKey]
        dictionary[innerObjectKey] = cl
        
#
subtitudeDictAsObjectIn(d)
print (d["variable3"])