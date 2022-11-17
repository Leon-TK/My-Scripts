def Enter(obj):
    print("Enter")
def Out(self, exc_type, exc_val, exc_tb):
    print("Out")

def __getattr__(name: str):
    if name == "__enter__":
        return Enter
    if name == "__exit__":
        return Out