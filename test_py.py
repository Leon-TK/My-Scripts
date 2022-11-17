from re import A
import enterModule

def test():
    print("hello")

def functionDebug():
    print("debug function")

class Test:
    def __init__(self) -> None:
        pass

def Enter(obj):
    print("Enter")
def Out(self, exc_type, exc_val, exc_tb):
    print("Out")
    
#make function with context manager
Test.__enter__ = Enter
Test.__exit__ = Out

with enterModule:
    print("")

a = 1
a = a << 1
